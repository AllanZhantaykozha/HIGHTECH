# Generated by Django 4.0.3 on 2022-09-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charger',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
