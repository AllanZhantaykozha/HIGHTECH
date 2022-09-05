from django.urls import path
from .views import *


urlpatterns = [
    path('', ChargerPage.as_view(), name='charger')
]