from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
        # watch_list = models.ManyToManyField(Auction_Listing, blank=True, related_name='watch_list' )
        pass

'''
    Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
'''
class Auction_Listing(models.Model):
    title = models.CharField(max_length=256)
    price = models.FloatField()
    img_url = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, default='')
    user  = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='users',  default=1)
    starting_bid = models.DecimalField(
        decimal_places=2, max_digits=4, default=1.0)

    def __str__(self):
        return f"({self.id}): {self.title}"


class Bids(models.Model):
    pass


class Comments(models.Model):
    pass

