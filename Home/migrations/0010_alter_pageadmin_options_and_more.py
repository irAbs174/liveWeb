# Generated by Django 4.1.1 on 2022-10-14 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_delete_userauth_alter_pageadmin_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageadmin',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='pageadmin',
            unique_together={('created_on', 'slug', 'title', 'author')},
        ),
    ]
