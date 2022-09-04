from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse


class Phone(models.Model):
    model = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='model')
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    company = models.CharField(max_length=150)
    front_camera = models.PositiveIntegerField(default=0)
    back_camera = models.PositiveIntegerField(default=0)
    cpu = models.CharField(max_length=200)
    ram = models.PositiveIntegerField(default=0)
    memory = models.PositiveIntegerField(default=0)
    battery = models.PositiveIntegerField(default=0)
    os = models.CharField(max_length=50)

    class Meta:
        ordering = ['company']

    def get_absolute_url(self):
        return reverse('detailphone', kwargs={'slug': self.slug})

        