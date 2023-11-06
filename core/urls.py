from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', homePage, name='Home'),
    path('menu', Menu, name='Menu'),
    path('update-profile/', update_profile, name='update-profile'),
    path('update-restaurant/', update_restaurant, name='update-restaurant'),
    path('add-menu/', add_menu, name='add-menu' ),
    path('delete/<int:id>/', delete_menu_confirmation, name='delete-menu-item'),
    path('owner/home/', owner_home, name='owner-home' ),
    path('select-restaurant/', select_restaurant, name='select-restaurant'),
    path('menu-list/', menu_list, name='menu-list'),
]