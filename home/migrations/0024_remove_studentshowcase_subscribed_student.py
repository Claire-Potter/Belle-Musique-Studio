# Generated by Django 3.2.5 on 2022-03-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20220318_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentshowcase',
            name='subscribed_student',
        ),
    ]
