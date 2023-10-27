from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('RESTAURANT_OWNER', 'Restaurant Owner'),
        ('RESTAURANT_STAFF', 'Restaurant Staff'),
        ('DELIVERY_AGENT', 'Delivery Agent'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username


class DeliveryAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100, unique=True)
    restaurant_address = models.CharField(max_length=100)
    owner = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'RESTAURANT_OWNER'}
    )

    def __str__(self):
        return self.restaurant_name


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, max_length=50, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


class Cart(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
