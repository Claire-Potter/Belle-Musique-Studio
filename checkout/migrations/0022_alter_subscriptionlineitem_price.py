# Generated by Django 3.2.5 on 2022-03-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0021_auto_20220315_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]