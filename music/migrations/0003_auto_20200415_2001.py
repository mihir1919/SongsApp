# Generated by Django 3.0.5 on 2020-04-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_songs_isfav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
