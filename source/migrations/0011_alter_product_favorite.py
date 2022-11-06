# Generated by Django 4.0.5 on 2022-09-17 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0010_remove_product_favourite_product_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]