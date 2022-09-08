from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Charger(models.Model):
    model = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='model')
    content = models.TextField(blank=True)
    power = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='company_charger')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    types = models.ForeignKey('Type', on_delete=models.PROTECT, related_name='type')
    price = models.FloatField(default=0)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['model']

    def get_absolute_url(self):
        return reverse('detailcharger', kwargs={'slug': self.slug})

class Type(models.Model):
    types = models.CharField(max_length=150)

    def __str__(self):
        return self.types