# Generated by Django 3.0.2 on 2020-02-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.FileField(default=111, upload_to='items/'),
            preserve_default=False,
        ),
    ]
