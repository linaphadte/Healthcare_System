# Generated by Django 4.0.6 on 2022-08-17 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_devices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='author',
            new_name='Author',
        ),
    ]
