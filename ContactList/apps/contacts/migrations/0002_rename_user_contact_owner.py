# Generated by Django 4.0 on 2021-12-28 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='owner',
        ),
    ]
