# Generated by Django 4.1.5 on 2023-04-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_rename_order_id_payments_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.orderitems'),
        ),
    ]