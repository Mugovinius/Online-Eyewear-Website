# Generated by Django 4.1.5 on 2023-03-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
