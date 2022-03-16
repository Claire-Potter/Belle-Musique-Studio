# Generated by Django 3.2.5 on 2022-03-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220310_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userlineitem',
            options={'get_latest_by': ['date'], 'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='userlineitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]