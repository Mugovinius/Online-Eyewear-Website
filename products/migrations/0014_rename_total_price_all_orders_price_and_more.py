# Generated by Django 4.1.5 on 2023-03-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_all_orders_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all_orders',
            old_name='total_price',
            new_name='price',
        ),
        migrations.AddField(
            model_name='all_orders',
            name='shipping_details',
            field=models.CharField(default='Nairobi, Kenya', max_length=50),
        ),
        migrations.AlterField(
            model_name='all_orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
