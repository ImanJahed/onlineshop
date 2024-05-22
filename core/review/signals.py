from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg
from .models import ReviewModel

@receiver(post_save, sender=ReviewModel)
def calculate_product_rating(sender, instance, **kwargs):
    product = instance.product
    reviews = ReviewModel.objects.filter(product=product, status=2)
    ave_rating = reviews.aggregate(Avg('rate'))['rate__avg']
    ave_rating = round(ave_rating, 1)
    product.avg_rate = ave_rating

    product.save()
