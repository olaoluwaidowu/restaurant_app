from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', homePage, name='Home'),
    path('menu', Menu, name='Menu'),
    path('update-profile/', update_profile, name='update-profile'),
    path('update-restaurant/', update_restaurant, name='update-restaurant'),
]