# Generated by Django 4.0.3 on 2022-09-06 10:42

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='model')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('content', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('company', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['model'],
            },
        ),
    ]