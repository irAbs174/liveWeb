# Generated by Django 3.2.13 on 2022-10-13 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_userauth_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userauth',
            old_name='Email/Phone',
            new_name='EnOFn',
        ),
        migrations.RenameField(
            model_name='userauth',
            old_name='username',
            new_name='UN',
        ),
    ]
