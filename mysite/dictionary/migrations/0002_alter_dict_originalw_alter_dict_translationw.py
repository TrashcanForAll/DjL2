# Generated by Django 4.2.16 on 2024-10-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='originalW',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='dict',
            name='translationW',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]