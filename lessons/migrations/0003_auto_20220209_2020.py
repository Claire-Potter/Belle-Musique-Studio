# Generated by Django 3.2 on 2022-02-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20220209_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
