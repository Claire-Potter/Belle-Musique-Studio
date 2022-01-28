# Generated by Django 3.2 on 2022-01-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220128_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
