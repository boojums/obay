import datetime as dt

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# TODO: implement custom manager for active Auction stuff
class Auction(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    bidding_open = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Only one auction active at a time, in current implementation
        if self.is_active:
            Auction.objects.filter(
                is_active=True).update(is_active=False)
        super(Auction, self).save(*args, **kwargs)

    def time_left(self):
        ''' Return timedelta until end of auction for more customization.'''
        # Need to both be aware or naive, so set now to have same tz as used in Auction
        tz = self.end.tzinfo
        now = dt.datetime.now(tz=tz)
        diff = self.end - now
        days = diff.days
        hours = diff.seconds / (60*60)
        minutes = (diff.seconds % (60*60)) / 60
        context = {'days': days, 'hours': hours, 'minutes': minutes}
        return context

    def current(self):
        return Auction.objects.filter(is_active=True)

    def is_open(self):
        tz = self.end.tzinfo
        now = dt.datetime.now(tz)
        return self.bidding_open and (self.start < now) and (self.end > now)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=128, unique=False)
    # TODO: media directory for each auction
    pic = ResizedImageField(size=[1000,1000], 
                quality=75, upload_to='item_images/')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    auction = models.ForeignKey(Auction)
    contact = models.ForeignKey(User)
    donor = models.CharField(max_length=128, null=True)
    approved = models.BooleanField(default=True)

    CATEGORY_CHOICES = (
        ('O', 'Orienteering'),
        ('NotO', 'Not Orienteering'),
    )
    category = models.CharField(max_length=4,
                                choices=CATEGORY_CHOICES,
                                default='O')

    def num_bids(self):
        ''' Return number of bids on this item.'''
        num = len(Bid.objects.filter(item=self))
        return num

    def top_bid(self):
        ''' Return the current wining bid for this item.'''
        try:
            top = Bid.objects.filter(item=self).order_by('-amount')[0]
        except:
            return None
        return top

    def save(self, *args, **kwargs):
         self.slug = slugify(self.name)
         super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Bid(models.Model):
    item = models.ForeignKey(Item)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '{0} - {1}'.format(self.time, self.amount)

# TODO: support unicode username admin field 
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    club = models.TextField(max_length=50, blank=True)
    isteam = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
