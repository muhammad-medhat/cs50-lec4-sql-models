# Generated by Django 4.0.1 on 2022-02-18 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_user_watch_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watch_list',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
