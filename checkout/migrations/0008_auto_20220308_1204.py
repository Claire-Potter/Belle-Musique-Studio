# Generated by Django 3.2.5 on 2022-03-08 12:04

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_subscribedcustomer_subscriptionlineitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedcustomer',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='subscribedcustomer',
            name='street_address1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='subscribedcustomer',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
