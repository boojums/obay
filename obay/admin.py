from django.contrib import admin
from obay.models import Auction, Item, Bid, UserProfile

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end', 'description', 'is_active')

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'auction', 'donor', 'approved', 'category')

class BidAdmin(admin.ModelAdmin):
    list_display = ('item', 'time', 'amount', 'user')
    list_filter = ('item',)

# Register your models here.
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(UserProfile)
