# Generated by Django 4.1.1 on 2022-10-14 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_remove_userauth_enofn_userauth_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAUTH',
        ),
        migrations.AlterModelOptions(
            name='pageadmin',
            options={'verbose_name_plural': 'PageAdministrator'},
        ),
    ]