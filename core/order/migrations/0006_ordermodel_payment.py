# Generated by Django 4.2.11 on 2024-05-04 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('order', '0005_alter_orderitemmodel_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.paymentmodel'),
        ),
    ]
