from django.contrib import admin
from myApp.models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    l=['item','itemCategory','quantity','price']

admin.site.register(Item,ItemAdmin)