# Generated by Django 4.1 on 2022-08-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_devices', '0004_alter_device_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='image',
        ),
        migrations.AddField(
            model_name='device',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='device/'),
        ),
    ]
