# Generated by Django 4.2.3 on 2023-07-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='category',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]