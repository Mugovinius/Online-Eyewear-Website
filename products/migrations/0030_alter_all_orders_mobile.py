# Generated by Django 4.1.5 on 2023-03-27 14:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_all_orders_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_orders',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
