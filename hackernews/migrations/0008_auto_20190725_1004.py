# Generated by Django 2.2.3 on 2019-07-25 04:04

from django.db import migrations, models
import hackernews.models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0007_auto_20190724_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=hackernews.models.upload_to),
        ),
    ]