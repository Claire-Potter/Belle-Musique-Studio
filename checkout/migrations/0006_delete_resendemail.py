# Generated by Django 3.2 on 2022-03-01 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_resendemail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResendEmail',
        ),
    ]