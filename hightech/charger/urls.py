from django.urls import path
from .views import *


urlpatterns = [
    path('', ChargerPage.as_view(), name='charger'),
    path('create/', CreateChargerPage.as_view(), name='create_charger'),
    path('<str:slug>/', DetailChargerPage.as_view(), name='detailcharger')
]