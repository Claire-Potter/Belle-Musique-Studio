# Generated by Django 3.2.5 on 2022-03-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_alter_customer_balance'),
        ('checkout', '0020_subscriptionlineitem_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionlineitem',
            name='subscription_id',
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_lineitems', to='djstripe.subscription'),
            preserve_default=False,
        ),
    ]
