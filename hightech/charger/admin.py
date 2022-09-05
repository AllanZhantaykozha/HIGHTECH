from django.contrib import admin
from .models import *


class ChargerAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'types', 'company')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'model', 'company', 'power', 'types')
    fields = ('model', 'content', 'photo', 'company', 'types', 'power', 'price')

class ChargerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'types')
    list_display_links = ('id', 'types')
    search_fields = ('id', 'types')
    fields = ('types', )


admin.site.register(Charger, ChargerAdmin)
admin.site.register(Type, ChargerTypeAdmin)
