from django.contrib import admin
from obay.models import Item, Bid, UserProfile

class BidAdmin(admin.ModelAdmin):
    list_display = ('item', 'time', 'amount')

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(UserProfile)

