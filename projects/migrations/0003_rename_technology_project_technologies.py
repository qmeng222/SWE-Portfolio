# Generated by Django 4.0.6 on 2022-08-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_technology'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technology',
            new_name='technologies',
        ),
    ]
