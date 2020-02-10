# Generated by Django 3.0.2 on 2020-01-31 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_comment_item_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=models.FileField(default=django.utils.timezone.now, upload_to='recipes/'),
            preserve_default=False,
        ),
    ]
