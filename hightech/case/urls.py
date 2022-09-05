from django.urls import path 
from .views import *


urlpatterns = [
    path('', CasePage.as_view(), name='case'),
]