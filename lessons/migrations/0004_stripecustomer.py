# Generated by Django 3.2 on 2022-02-10 10:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0003_auto_20220209_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripeCustomerId', models.CharField(max_length=255)),
                ('stripeSubscriptionId', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
