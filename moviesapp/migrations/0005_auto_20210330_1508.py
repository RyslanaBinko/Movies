# Generated by Django 3.1.7 on 2021-03-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0004_auto_20210330_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='moviesapp.Genre'),
        ),
    ]