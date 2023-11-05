from django.db import models
from authentication.models import User
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100, unique=True)
    restaurant_address = models.CharField(max_length=100)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
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
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


class Cart(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    address = models.CharField(max_length=1000)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
