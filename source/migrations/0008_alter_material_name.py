# Generated by Django 4.0.5 on 2022-07-08 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0007_alter_material_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=2500),
        ),
    ]
