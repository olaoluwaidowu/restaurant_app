from django.shortcuts import render

from authentication.models import User
from .forms import RegisterForm
# Create your views here.


def CustomerRegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.validated_data.get('email')
            password = form.validated_data.get('password')
            user = User.objects.create_customer(email=email, password=password)
            user.save()
            send_mail()
    pass