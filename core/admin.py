from django.contrib import admin
from .models import *

# admin.site.register(UserProfile)
# admin.site.register(DeliveryAddress)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)

