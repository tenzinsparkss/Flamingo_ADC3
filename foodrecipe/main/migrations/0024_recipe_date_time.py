# Generated by Django 3.0.2 on 2020-02-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]