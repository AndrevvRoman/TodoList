# Generated by Django 3.1.5 on 2021-01-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210123_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='mail',
        ),
    ]
