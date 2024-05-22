from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
User = get_user_model()

# Create your models here.
class ReviewStatus(models.IntegerChoices):
    pending = 1, 'در انتظار تایید'
    accepted = 2, 'تایید شده'
    rejected = 3, 'رد شده'


class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("shop.productModel", on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.SmallIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])

    status = models.SmallIntegerField(default=ReviewStatus.pending, choices=ReviewStatus.choices)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.pk}-{self.product.pk}'
    
    def get_status(self):
        return {
            "id":self.status,
            "title":ReviewStatus(self.status).name,
            "label":ReviewStatus(self.status).label,
        }