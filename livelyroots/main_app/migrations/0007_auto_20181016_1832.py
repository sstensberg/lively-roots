# Generated by Django 2.1.1 on 2018-10-16 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20181013_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='member',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='members',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='member',
            new_name='user',
        ),
    ]
