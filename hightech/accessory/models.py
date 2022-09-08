from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Accessory(models.Model):
    model = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='model')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='company_accessory')
    content = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
            return self.model

    class Meta:
        ordering = ['model']
        
    def get_absolute_url(self):
        return reverse('detailaccessory', kwargs={'slug': self.slug})
