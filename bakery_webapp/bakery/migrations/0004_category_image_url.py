# Generated by Django 5.1.4 on 2025-01-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0003_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
