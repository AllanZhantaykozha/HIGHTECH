from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Phone(models.Model):
    model = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='model')
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='company_phone')
    front_camera = models.PositiveIntegerField(default=0, null=True)
    back_camera = models.PositiveIntegerField(default=0, null=True)
    cpu = models.CharField(max_length=200, null=True)
    ram = models.PositiveIntegerField(default=0, null=True)
    memory = models.PositiveIntegerField(default=0, null=True)
    battery = models.PositiveIntegerField(default=0, null=True)
    os = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['company']

    def get_absolute_url(self):
        return reverse('detailphone', kwargs={'slug': self.slug})

        