from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, UserManager

admin.site.register(User)
# admin.site.register(UserManager)
