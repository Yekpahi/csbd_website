# Generated by Django 4.1.4 on 2022-12-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_welcomemessage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcomemessage',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=20), max_length=200, unique=True),
        ),
    ]
