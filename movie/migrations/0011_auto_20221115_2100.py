# Generated by Django 3.2.13 on 2022-11-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_alter_movie_flim'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='subtitle',
            field=models.FileField(default='', upload_to='subs'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
