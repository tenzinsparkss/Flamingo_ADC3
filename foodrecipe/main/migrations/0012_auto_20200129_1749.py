# Generated by Django 3.0.1 on 2020-01-29 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_comment_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_images',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_videos',
        ),
    ]
