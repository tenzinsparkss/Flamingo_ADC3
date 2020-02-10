# Generated by Django 3.0.1 on 2020-01-26 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200126_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=50)),
                ('recipe_description', models.TextField()),
                ('recipe_category', models.CharField(max_length=50)),
                ('recipe_images', models.ImageField(upload_to='images')),
                ('recipe_videos', models.FileField(upload_to='videos')),
                ('recipe_favorites', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Recipe')),
            ],
        ),
    ]