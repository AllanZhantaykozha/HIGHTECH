# Generated by Django 4.0.3 on 2022-09-05 16:08

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='model')),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('phone_model', models.CharField(max_length=150)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['model'],
            },
        ),
    ]