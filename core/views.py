from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RestaurantUpdateForm, UserProfileUpdateForm, ProductForm
from authentication.models import User
from .models import Restaurant, Product


# Create your views here.
def homePage(request):
    print('home now')
    return render(request, 'core/landingPage.html')

@login_required(login_url='Login')
def Menu(request):
    
    food_items = Product.objects.all()
    context = {
        'food_items': food_items,
    }
    return render(request, 'core/menu.html', context)

@login_required(login_url='authentication:Login')
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


@login_required(login_url='authentication:Login')
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
    
@login_required(login_url='authentication:Login')
def add_menu(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():

            product = form.save(commit=False)
            product.restaurant = request.user.restaurant
            product.save()
            return redirect('core:Menu')

    else:
        form = ProductForm()

    return render(request, 'core/add_menu.html', {'form': form})

@login_required(login_url='authentication:Login')
def delete_menu_confirmation(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect('core:Menu') 

    if request.method == 'POST':
        
        product.delete()
        return redirect('core:Menu')

    return render(request, 'core/delete_menu_confirmation.html', {'product': product})

@login_required(login_url='authentication:Login')
def owner_home(request):
    return render(request, 'core/owner_home.html')


def select_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'core/select_restaurant.html', {'restaurants': restaurants})

@login_required(login_url='authentication:Login')
def menu_list(request):
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant')
        
        restaurant = Restaurant.objects.get(restaurant_name=restaurant_id)
        #products = restaurant.restaurant_name
        products = Product.objects.get(restaurant=restaurant)
        
        return render(request, 'menu_list.html', {'restaurant': restaurant, 'menu_items': products})
    else:
        return redirect('select-restaurant')