# Generated by Django 4.1.5 on 2023-04-02 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_remove_all_orders_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='order_no',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='products.payments'),
            preserve_default=False,
        ),
    ]
