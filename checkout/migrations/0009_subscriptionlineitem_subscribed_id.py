# Generated by Django 3.2.5 on 2022-03-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20220308_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionlineitem',
            name='subscribed_id',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
