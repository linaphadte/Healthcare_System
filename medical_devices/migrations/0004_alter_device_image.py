# Generated by Django 4.1 on 2022-08-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_devices', '0003_device_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='device_pic/'),
        ),
    ]
