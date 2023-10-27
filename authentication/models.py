from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, 
    PermissionsMixin, Group
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.contrib.auth.hashers import make_password


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
    
    def create_customer(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_customer", True)

        if extra_fields.get("is_customer") is not True:
            raise ValueError("CCustomer must have is_customer=True.")

        return self._create_user(email, password, **extra_fields)
    
    def create_owner(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_restaurant_owner", True)

        if extra_fields.get("is_customer") is not True:
            raise ValueError("Restaurant Owner must have is_restaurant_owner=True.")

        return self._create_user(email, password, **extra_fields)
    
    def create_rider(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_rider", True)

        if extra_fields.get("is_customer") is not True:
            raise ValueError("Rider must have is_rider=True.")

        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True, error_messages={
            "unique": _("A user with that email already exists."),
        },)
    address = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=15)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_rider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_restaurant_owner = models.BooleanField(default=False)
    otp_field = models.CharField(max_length=5)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
    objects = UserManager()
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]