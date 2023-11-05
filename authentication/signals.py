from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from core.models import Restaurant

@receiver(post_save, sender=User)
def create_restaurant_for_owner(sender, instance, created, **kwargs):
    print('creator detected')
    if created and instance.is_restaurant_owner:
        print('working on creating restaurant')
        # Create a Restaurant object associated with the owner
        Restaurant.objects.create(owner=instance)