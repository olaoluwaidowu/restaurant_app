from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RestaurantUpdateForm, UserProfileUpdateForm
from authentication.models import User
from .models import Restaurant


# Create your views here.
def homePage(request):
    print('home now')
    return render(request, 'core/landingPage.html')


def Menu(request):
    return render(request, 'core/menu.html')


@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the user's profile page.
            return redirect('authentication:profile_page')  # Replace with your URL pattern name for the profile page.

    else:
        form = UserProfileUpdateForm(instance=user)

    return render(request, 'core/update_profile.html', {'form': form})


@login_required
def update_restaurant(request):
    user = request.user
    if user.is_restaurant_owner:
        restaurant = Restaurant.objects.get(owner=user)

        if request.method == 'POST':
            form = RestaurantUpdateForm(request.POST, instance=restaurant)
            if form.is_valid():
                form.save()

                return redirect('authentication:profile_page')

        else:
            form = RestaurantUpdateForm(instance=restaurant)

        return render(request, 'core/restaurant_update.html', {'form': form})