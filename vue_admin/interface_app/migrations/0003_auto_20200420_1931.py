# Generated by Django 3.0.4 on 2020-04-20 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0002_interface'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descript',
            new_name='description',
        ),
    ]
