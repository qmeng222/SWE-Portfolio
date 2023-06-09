# Generated by Django 4.0.6 on 2022-08-13 02:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='static/img')),
                ('members', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
