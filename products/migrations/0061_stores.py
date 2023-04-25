# Generated by Django 4.1.5 on 2023-04-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0060_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('physical_address', models.CharField(max_length=80)),
                ('office_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('basic_desc', models.TextField(max_length=200)),
            ],
        ),
    ]
