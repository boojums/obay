from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.forms.formsets import formset_factory

from obay.models import Item, Bid, Auction
from obay.forms import ItemForm, BidForm, UserForm, UserProfileForm

# TODO: use js countdown such as: http://keith-wood.name/countdown.html
def index(request):
    # Only show approved items from current auction
    current_auction = Auction.objects.filter(is_active=True)[0]
    item_list = Item.objects.filter(auction=current_auction, approved=True).order_by('name')[:] 

    bidformset = formset_factory(BidForm, extra=len(item_list))
    formset = bidformset()
    context_dict = {'items': item_list, 'current_auction': current_auction, 'formset': formset}

    return render(request, 'obay/index.html', context_dict)

def indexbid(request, item_name_slug):
    BidFormset = formset_factory(BidForm)
    if request.method == 'POST':
        formset = BidFormset(request.POST)
        for form in formset.forms:
            if form.is_valid():
                if item:
                    # Need to do a bit more work before we commit
                    bid = form.save(commit=False)
                    bid.item = item
                    bid.user = request.user
                    bid.save()
                    return itemview(request, item_name_slug)
    return render(request, '')

def about(request):
    context_dict = {'boldmessage': "this is a different bold message"}

    return render(request, 'obay/about.html', context_dict)
    
def itemview(request, item_name_slug):
    context_dict = {}
    try:
        item = Item.objects.get(slug=item_name_slug)
        context_dict['item_name'] = item.name

        # Retrieve all of the bids
        bids = Bid.objects.filter(item=item).order_by('amount')
        context_dict['bids'] = bids

        # Add this to dict to have a check that the item exists
        context_dict['item'] = item
        context_dict['item_name_slug'] = item_name_slug
    except Item.DoesNotExist:
        pass

    return render(request, 'obay/item.html', context_dict)

@permission_required('obay.can_add_item', raise_exception=False)
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = ItemForm()

    return render(request, 'obay/add_item.html', {'form': form})

@login_required()
def add_bid(request, item_name_slug):
    try:
        item = Item.objects.get(slug=item_name_slug)
    except:
        item = None

    if request.method == 'POST':
        form = BidForm(request.POST, item=item)
        if form.is_valid():
            if item:
                # Need to do a bit more work before we commit
                bid = form.save(commit=False)
                bid.item = item
                bid.user = request.user
                bid.save()
                return itemview(request, item_name_slug)
        else:
            print form.errors
    else:
        form = BidForm()

    context_dict = {'form': form, 'item': item, 'item_name_slug': item_name_slug}
    return render(request, 'obay/add_bid.html', context_dict)
