from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pic = models.ImageField(upload_to='item_images')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    #auction = models.ForeignKey(Auction)
    #donor = models.ForeignKey(User)
    #suggested bid/required increment
    # approved
    CATEGORY_CHOICES = (
        ('O', 'Orienteering'),
        ('NotO', 'Not Orienteering'),
    )
    category = models.CharField(max_length=4,
                                choices=CATEGORY_CHOICES,
                                default='O')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Bid(models.Model):
    item = models.ForeignKey(Item)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    #bidderid = models.ForeignKey()

    def __unicode__(self):
        return '{0} - {1}'.format(self.time, self.amount)

class Auction(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    club = models.TextField(max_length=50, blank=True)
    isteam = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
