from django.urls import path
from .views import *


urlpatterns = [
    path('', PhonePage.as_view(), name='phone'),
    path('createadvert/', CreatePhonePage.as_view(), name='create_phone'),
    path('phone/<str:slug>/', DetailPhonePage.as_view(), name='detailphone')
]