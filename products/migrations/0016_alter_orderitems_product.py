# Generated by Django 4.1.5 on 2023-03-15 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_all_orders_item_remove_all_orders_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cart'),
        ),
    ]
