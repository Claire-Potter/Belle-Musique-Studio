# Generated by Django 3.2.5 on 2022-03-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_alter_customer_balance'),
        ('checkout', '0023_alter_subscriptionlineitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_customer', to='checkout.subscribedcustomer'),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='end_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='latest_invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_invoice', to='djstripe.invoice'),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='lineitem_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='original_lesson_bag',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='start_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='student',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='subscribed_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_lineitems', to='djstripe.subscription'),
        ),
        migrations.AlterField(
            model_name='subscriptionlineitem',
            name='subscription_name',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]