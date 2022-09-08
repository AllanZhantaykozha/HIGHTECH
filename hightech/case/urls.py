from django.urls import path 
from .views import *


urlpatterns = [
    path('', CasePage.as_view(), name='case'),
    path('create/', CreateCasePage.as_view(), name='create_case'),
    path('<str:slug>/', DetailCasePage.as_view(), name='detailcase')
]