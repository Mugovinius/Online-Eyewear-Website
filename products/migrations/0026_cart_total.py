# Generated by Django 4.1.5 on 2023-03-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_orderitems_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
