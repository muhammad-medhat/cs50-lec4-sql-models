# Generated by Django 4.0.1 on 2022-02-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_rename_commwns_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_listing',
            old_name='img',
            new_name='img_url',
        ),
        migrations.RenameField(
            model_name='auction_listing',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='description',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]
