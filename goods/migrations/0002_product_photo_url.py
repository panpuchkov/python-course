# Generated by Django 3.0.6 on 2020-05-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_url',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
