# Generated by Django 3.2 on 2022-02-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='price',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='subscription',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('subscription', models.CharField(choices=[('Annually', 'Annually'), ('Monthly', 'Monthly'), ('Weekly', 'Weekly')], default='Monthly', max_length=15)),
                ('time_duration', models.CharField(choices=[('30 minutes', '30 minutes'), ('45 minutes', '45 minutes')], default='30 minutes', max_length=15)),
                ('price', models.CharField(choices=[('£ 25.00', '£ 25.00'), ('£ 37.50', '£ 37.50'), ('£ 100.00', '£ 100.00'), ('£ 150.00', '£ 150.00'), ('£ 1200.00', '£ 1200.00'), ('£ 1800.00', '£ 1800.00')], default='£ 25.00', max_length=15)),
                ('lesson', models.ManyToManyField(blank=True, related_name='lesson', to='lessons.Lesson')),
            ],
        ),
    ]
