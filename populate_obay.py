import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obay_project.settings')

import django
django.setup()

from obay.models import Item, Bid
from django.contrib.auth.models import User

def populate():
    
    bnb_item = add_item('Oslo BnB', 'NotO', 'kikigigi.jpg')

    add_bid(item=bnb_item,
        amount=20, user=user[0]) 
    add_bid(item=bnb_item,
        amount=22, user=user) 
    add_bid(item=bnb_item,
        amount=35, user=user) 
    add_bid(item=bnb_item,
        amount=60, user=user) 

    jersey_item = add_item('Signed TG jersey', 'O', 'tgmiddlefinal.jpg')

    add_bid(item=jersey_item,
        amount=50, user=user) 
    add_bid(item=jersey_item,
        amount=122, user=user) 
    add_bid(item=jersey_item,
        amount=319, user=user) 
    add_bid(item=jersey_item,
        amount=1322, user=user) 

    for i in Item.objects.all():
        for b in Bid.objects.filter(item=i):
            print "- {0} - {1}".format(str(i), str(b)))

def add_item(name, cat):
    i = Item.objects.get_or_create(name=name, category=cat)[0]
    return i

def add_bid(item, amount, user):
    b = Bid.objects.get_or_create(item=item, amount=amount, user=user)[0]
    b.save()

if __name__ == '__main__':
    print 'Starting Obay population script...'
    populate()