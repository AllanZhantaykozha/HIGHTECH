from django.urls import path 
from .views import *


urlpatterns = [
    path('', AccessoryPage.as_view(), name='accessory'),
    path('create/', CreateAccessoryPage.as_view(), name='create_accessory'),
    path('<str:slug>/', DetailAccessoryPage.as_view(), name='detailaccessory')
]