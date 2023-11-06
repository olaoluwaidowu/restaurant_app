from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from authentication.models import User
from .forms import RegisterForm, LoginForm
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .utils import send_confirmation_email
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.views import LoginView
from core.models import Restaurant

# Create your views here.
#User = settings.AUTH_USER_MODEL

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def confirm_email_view(request):
    return render(request, 'authentication/confirm_email.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user_type = form.cleaned_data.get('user_type')

            if user_type == 'customer':
                user = User.objects.create_customer(email=email, password=password)
            elif user_type == 'restaurant_owner':
                user = User.objects.create_owner(email=email, password=password, is_restaurant_owner=True)
                print('user created')
            elif user_type == 'delivery_agent':
                user = User.objects.create_rider(email=email, password=password)

            user.save()

            send_confirmation_email(request, user)
            
            return redirect('authentication:ConfirmEmail')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'authentication/registration.html', context)


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'authentication/activation_success.html')
        else:
            return render(request, 'authentication/activation_failed.html')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request, 'authentication/activation_failed.html')


def activation_success(request):
    return render(request, 'authentication/activation_success.html')

def activation_failed(request):
    return render(request, 'authentication/activation_failed.html')


def custom_login(request):
    print('login is called')
    if request.method == 'POST':
        print('method is post')
        form = LoginForm(request, request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.get_user()
            print(user)
            login(request, user)
            print('user logged in')

            return redirect('authentication:profile_page')  
        else:
            print('form is invalid')
    else:
        
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def profile(request):
    if request.user.is_customer:

        return redirect('core:select-restaurant')
    elif request.user.is_rider:

        return render(request, 'profile_rider.html', {'user': request.user})
    elif request.user.is_restaurant_owner:
            restaurant = Restaurant.objects.get(owner=request.user)
            
            if restaurant.restaurant_name:
                context = {
                    'user': request.user,
                    'restaurant' : restaurant
                }
            else:
                context = {
                    'user': request.user,
                }
            return render(request, 'authentication/profile_restaurant_owner.html', context)
    else:
        return redirect('Login')


def confirm_email_view(request):
    return render(request, 'authentication/confirm_email.html')


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    
def logout_user(request):
    logout(request)
    
    return redirect('authentication:Login')