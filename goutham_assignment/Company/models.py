from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse


class Company(models.Model):
    """using models to create Company data"""
    name = models.CharField(max_length=240)
    logo = models.ImageField(default='logo.jpg', upload_to='media/logos')
    address = models.TextField()
    current_viewers = models.PositiveIntegerField(default=0)
    total_viewers = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'pk': self.pk})


def save_post(sender, instance, **kwargs):
    print(f'{instance} is created!')


post_save.connect(save_post, sender=Company)
