# Generated by Django 3.2 on 2022-03-01 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('resend', models.BooleanField(default=False)),
                ('username', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='resend_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
