# Generated by Django 4.2.11 on 2024-04-26 07:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_productimagemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='display_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'نمایش'), (2, 'عدم نمایش')], default=1, verbose_name='Display Status'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'موجود'), (2, 'ناموجود')], default=1, verbose_name='Status'),
        ),
    ]
