# Generated by Django 3.2.5 on 2022-03-18 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_contact_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='username',
        ),
    ]