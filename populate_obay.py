import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obay_project.settings')

import django
django.setup()

from obay.models import Item, Bid

def populate():
    bnb_item = add_item('Oslo BnB', 'NotO')

    add_bid(item=bnb_item,
        amount=20) 
    add_bid(item=bnb_item,
        amount=22) 
    add_bid(item=bnb_item,
        amount=35) 
    add_bid(item=bnb_item,
        amount=60) 

    jersey_item = add_item('Signed TG jersey', 'O')

    add_bid(item=jersey_item,
        amount=50) 
    add_bid(item=jersey_item,
        amount=122) 
    add_bid(item=jersey_item,
        amount=319) 
    add_bid(item=jersey_item,
        amount=1322) 

    for i in Item.objects.all():
        for b in Bid.objects.filter(item=i):
            print "- {0} - {1}".format(str(i), str(b))

def add_item(name, cat):
    i = Item.objects.get_or_create(name=name, category=cat)[0]
    return i

def add_bid(item, amount):
    b = Bid.objects.get_or_create(item=item, amount=amount)[0]
    b.save()

if __name__ == '__main__':
    print 'Starting Obay population script...'
    populate()