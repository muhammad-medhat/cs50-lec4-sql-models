# Generated by Django 4.0.1 on 2022-02-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_rename_img_auction_listing_img_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watch_list',
            field=models.ManyToManyField(blank=True, related_name='watch_list', to='auction.Auction_Listing'),
        ),
    ]