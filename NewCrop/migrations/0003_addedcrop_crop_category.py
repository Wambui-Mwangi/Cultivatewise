# Generated by Django 4.2.3 on 2023-07-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewCrop', '0002_addedcrop_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedcrop',
            name='crop_category',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
