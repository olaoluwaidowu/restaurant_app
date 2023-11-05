from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

app_name = 'authentication'

urlpatterns = [
    path('Reg/', register, name='Registration'),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate_account'),
    path('activation/success/', activation_success, name='activation_success'),
    path('activation/failed/', activation_failed, name='activation_failed'),
    path('profile/', profile, name='profile_page'),
    path('confirm/', confirm_email_view, name='ConfirmEmail'),
    path('login/', custom_login, name='Login'),
    #path('login/', CustomLoginView.as_view(template_name='authentication/login.html'), name='login'),
]