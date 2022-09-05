from django.contrib import admin
from .models import *


class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'phone_model')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'model', 'phone_model')
    fields = ('model', 'content', 'photo', 'phone_model', 'price')


admin.site.register(Case, CaseAdmin)
