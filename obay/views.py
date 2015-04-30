from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from obay.models import Item, Bid, Auction
from obay.forms import ItemForm, BidForm, UserForm, UserProfileForm

def index(request):
    item_list = Item.objects.order_by('name')[:]
    top_bids = {}

    context_dict = {'items': item_list}

    return render(request, 'obay/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "this is a different bold message"}

    return render(request, 'obay/about.html', context_dict)
    
    #return HttpResponse("This is the Obay auction site. <a href='/obay/'>Home</a>")

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
