# Generated by Django 4.0.5 on 2022-07-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_alter_product_altarnative_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='altarnative_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='altarnative_products+', through='source.AltarnativeProduct', to='source.product'),
        ),
    ]
