# Generated by Django 3.2.5 on 2022-03-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_alter_customer_balance'),
        ('home', '0008_auto_20220303_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscription',
            field=models.ManyToManyField(blank=True, to='djstripe.Subscription'),
        ),
    ]
