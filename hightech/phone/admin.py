from django.contrib import admin
from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'company')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'model', 'company')
    fields = ('model', 'content', 'photo', 'company', 'front_camera', 'back_camera', 'cpu', 'ram', 'memory', 'battery', 'os')


admin.site.register(Phone, PhoneAdmin)