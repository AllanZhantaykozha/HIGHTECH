from django.urls import path
from .views import *


urlpatterns = [
    path('', PhonePage.as_view(), name='computer')
]