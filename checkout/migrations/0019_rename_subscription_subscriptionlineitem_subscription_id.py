# Generated by Django 3.2.5 on 2022-03-15 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_auto_20220315_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptionlineitem',
            old_name='subscription',
            new_name='subscription_id',
        ),
    ]