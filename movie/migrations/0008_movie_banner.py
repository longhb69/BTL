# Generated by Django 3.2.13 on 2022-11-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movies_banner'),
            preserve_default=False,
        ),
    ]
