# Generated by Django 4.1.1 on 2022-09-17 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_title_desc_w_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desc',
            old_name='w_title',
            new_name='title',
        ),
    ]