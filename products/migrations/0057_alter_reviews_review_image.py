# Generated by Django 4.1.5 on 2023-04-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_alter_reviews_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
