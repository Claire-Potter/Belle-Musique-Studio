# Generated by Django 3.2 on 2022-03-01 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_subscribeduser_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribeduser',
            name='subscription_type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_type', to='lessons.subscription'),
        ),
    ]