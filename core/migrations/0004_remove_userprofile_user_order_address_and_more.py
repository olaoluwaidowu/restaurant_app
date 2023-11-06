# Generated by Django 4.2.6 on 2023-10-27 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_remove_userprofile_type_userprofile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.OneToOneField(limit_choices_to={'user_type': 'RESTAURANT_OWNER'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
