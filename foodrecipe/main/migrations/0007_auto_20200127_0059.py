# Generated by Django 3.0.1 on 2020-01-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment_item_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipes',
        ),
        migrations.AddField(
            model_name='comment',
            name='recipes',
            field=models.ManyToManyField(to='main.Recipe'),
        ),
    ]
