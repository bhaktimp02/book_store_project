# Generated by Django 3.2 on 2021-04-21 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0003_auto_20210415_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='PassWord1',
            new_name='PassWord',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='PassWord2',
        ),
    ]
