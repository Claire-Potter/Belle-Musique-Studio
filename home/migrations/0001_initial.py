import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('home_image', models.ImageField(upload_to='', verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deletable', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Home',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deletable', models.BooleanField(default=True, editable=False)),
                ('username', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Contact Requests',
                'ordering': ['-created_on'],
            },
        ),
    ]