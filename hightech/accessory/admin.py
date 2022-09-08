from django.contrib import admin
from .models import Accessory


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'company')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'model', 'company')
    fields = ('model', 'content', 'photo', 'company', 'price')


admin.site.register(Accessory, AccessoryAdmin)
