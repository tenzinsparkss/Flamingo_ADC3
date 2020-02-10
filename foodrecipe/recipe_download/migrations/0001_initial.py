# Generated by Django 3.0.2 on 2020-02-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe_Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=200)),
                ('videos', models.FileField(upload_to='recipe_videos/')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]