from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from obay.models import Item, Bid, Auction
from obay.forms import ItemForm, BidForm, UserForm, UserProfileForm

# TODO: use js countdown such as: http://keith-wood.name/countdown.html
def index(request):
    # Only show approved items from current auction
    current_auction = Auction.objects.filter(is_active=True)[0]

    # Some people will only want to see non-orienteering stuff!
    show = request.GET.get('show')
    if show == 'noo':
        item_list = Item.objects.filter(auction=current_auction, 
            category='NotO',
            approved=True).order_by('name')[:]
    else:
        item_list = Item.objects.filter(auction=current_auction, approved=True).order_by('name')[:] 
    
    paginator = Paginator(item_list, 3, orphans=2)
    page = request.GET.get('page')    
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # send first page of items in case of invalid page
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    pagenums = range(1, paginator.num_pages+1)

    context_dict = {'items': items, 'current_auction': current_auction, 'pagenums':pagenums}

    return render(request, 'obay/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "this is a different bold message"}

    return render(request, 'obay/about.html', context_dict)
    
def itemview(request, item_name_slug):
    try:
        item = Item.objects.get(slug=item_name_slug)
    except:
        item = None

    # Retrieve all of the bids
    bids = Bid.objects.filter(item=item).order_by('-amount')

    form = BidForm(request.POST or None, item=item)
    if form.is_valid():
        if item:
            # Need to do a bit more work before we commit
            bid = form.save(commit=False)
            bid.item = item
            bid.user = request.user
            bid.save()
            message = 'Bid added!'
            return redirect('item', item_name_slug) 
    else:
        print form.errors

    context_dict = {'form': form, 'bids': bids, 'item': item, 'item_name_slug': item_name_slug}

    return render(request, 'obay/item.html', context_dict)

def my_bids(request):
    ''' Show all of the current user's bids.'''
    bids = Bid.objects.filter(user=request.user).order_by('item', '-amount')

    context_dict = {'bids': bids}
    return render(request, 'obay/my_bids.html', context_dict)

def my_items(request):
    ''' Show all of the current user's items.'''
    items = Item.objects.filter(contact=request.user).order_by('name')

    context_dict = {'items': items}
    return render(request, 'obay/my_items.html', context_dict)

@permission_required('obay.can_add_item', raise_exception=False)
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.auction = Auction.objects.get(is_active=True)
            item.contact = request.user
            item.save()
            return redirect('index')
        else:
            print form.errors
    else:
        form = ItemForm()

    return render(request, 'obay/add_item.html', {'form': form})

@permission_required('obay.can_edit_item', raise_exception=False)
def edit_item(request, item_name_slug=None):
    if item_name_slug:
        item = get_object_or_404(Item, slug=item_name_slug)
        if item.contact != request.user:
            return HttpResponseForbidden()
    else:
        item = Item(contact=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
            item.auction = Auction.objects.get(is_active=True)
            #item.contact = request.user
            item.save()
            return redirect('index')
        else:
            print form.errors
    else:
        form = ItemForm(instance=item)

    return render(request, 'obay/add_item.html', {'form': form})
