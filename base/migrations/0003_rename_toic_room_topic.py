# Generated by Django 3.2.18 on 2023-04-28 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230428_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='toic',
            new_name='topic',
        ),
    ]
