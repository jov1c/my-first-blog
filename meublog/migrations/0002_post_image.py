# Generated by Django 2.2.24 on 2021-11-07 16:36

from django.db import migrations, models
import meublog.models


class Migration(migrations.Migration):

    dependencies = [
        ('meublog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=meublog.models.upload_image),
        ),
    ]
