from django.contrib import admin
from obay.models import Auction, Item, Bid, UserProfile

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end', 'description', 'is_active')

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class BidAdmin(admin.ModelAdmin):
    list_display = ('item', 'time', 'amount', 'user')


# Register your models here.
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(UserProfile)

