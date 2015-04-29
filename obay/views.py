from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

from obay.models import Item, Bid, Auction
from obay.forms import ItemForm, BidForm, UserForm, UserProfileForm

def index(request):
    item_list = Item.objects.order_by('name')[:]
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
        form = BidForm(request.POST)
        if form.is_valid():
            if item:
                # Need to do a bit more work before we commit
                bid = form.save(commit=False)
                bid.item = item
                bid.save()
                return itemview(request, item_name_slug)
        else:
            print form.errors
    else:
        form = BidForm()

    context_dict = {'form': form, 'item': item, 'item_name_slug': item_name_slug}
    return render(request, 'obay/add_bid.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile.form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'obay/register.html', 
        {'user_form': user_form, 'profile_form': profile_form, 'registered':registered})


def user_login(request):

    if request.method == 'POST':
        
        # Use request.POST.get('<var>') as opposed to request.POST['<var>']
        # because request.POST.get('<var>') returns None if the value doesn't exist
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/obay/')
            else:
                return HttpResponse("Your Obay account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'obay/login.html', {})
