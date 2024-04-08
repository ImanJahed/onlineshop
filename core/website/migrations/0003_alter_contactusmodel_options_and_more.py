# Generated by Django 4.2.11 on 2024-04-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contactusmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactusmodel',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AddField(
            model_name='contactusmodel',
            name='is_subscribed',
            field=models.BooleanField(default=False, verbose_name='Is Subscribe?'),
        ),
    ]
