# Generated by Django 4.2.3 on 2023-07-30 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewCrop', '0002_addedcrop_crop'),
        ('Feedback', '0002_review_delete_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='new_crop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='NewCrop.addedcrop'),
            preserve_default=False,
        ),
    ]
