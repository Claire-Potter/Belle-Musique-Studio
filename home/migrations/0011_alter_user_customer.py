# Generated by Django 3.2.5 on 2022-03-09 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_alter_customer_balance'),
        ('home', '0010_auto_20220308_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.customer', unique=True),
        ),
    ]