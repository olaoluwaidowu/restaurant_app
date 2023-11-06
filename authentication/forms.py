from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from .models import User

#User = settings.AUTH_USER_MODEL


class RegisterForm(forms.Form):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('restaurant_owner', 'Restaurant Owner'),
        ('delivery_agent', 'Delivery Agent'),
    )

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_confirm_password(self):
        
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            print("password dont match")
            raise forms.ValidationError("Passwords do not match")
        return confirm_password
        
        
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
