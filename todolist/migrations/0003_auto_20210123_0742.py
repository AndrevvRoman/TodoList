# Generated by Django 3.1.5 on 2021-01-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='login',
            new_name='user',
        ),
    ]
