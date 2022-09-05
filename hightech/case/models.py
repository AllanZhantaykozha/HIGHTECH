from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse


class Case(models.Model):
    model = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='model')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    phone_model = models.CharField(max_length=150)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['model']

    def get_absolute_url(self):
        return reverse('detailcase', kwargs={'slug': self.slug})