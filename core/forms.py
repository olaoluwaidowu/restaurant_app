from django import forms
from authentication.models import User
from .models import Restaurant, Product


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
class RestaurantUpdateForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'restaurant_address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']