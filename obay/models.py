import datetime as dt

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
       
# TODO: implement custom manager for active Auction stuff
class Auction(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Only one auction active at a time, in current implementation
        if self.is_active:
            Auction.objects.filter(
                is_active=True).update(is_active=False)
        super(Auction, self).save(*args, **kwargs)

    def time_left(self):
        ''' Return timedelta until end of auction.'''
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

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pic = models.ImageField(upload_to='item_images/')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    auction = models.ForeignKey(Auction)
    donor = models.ForeignKey(User)
    approved = models.BooleanField(default=True)

    CATEGORY_CHOICES = (
        ('O', 'Orienteering'),
        ('NotO', 'Not Orienteering'),
    )
    category = models.CharField(max_length=4,
                                choices=CATEGORY_CHOICES,
                                default='O')

    def top_bid(self):
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
