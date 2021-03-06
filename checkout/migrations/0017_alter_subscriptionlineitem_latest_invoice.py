# Generated by Django 3.2.5 on 2022-03-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_alter_customer_balance'),
        ('checkout', '0016_alter_subscriptionlineitem_latest_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='latest_invoice',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_invoice', to='djstripe.invoice'),
        ),
    ]
