from django.db import models

# Create your models here.
class PaymentStatus(models.IntegerChoices):
    pending = 1, 'در انتظار پرداخت'
    success = 2, 'پرداخت موفق'
    failed = 3, 'پرداخت ناموفق'


class PaymentModel(models.Model):
    authority_id = models.CharField(max_length=250)
    ref_id = models.BigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    response_json = models.JSONField(default=dict)
    response_code = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=PaymentStatus.choices, default=PaymentStatus.pending)

    created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'