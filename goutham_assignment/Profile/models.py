from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


class Profile(models.Model):
    """This class creates Profile objects"""
    name = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='media/profile_picture')
    job = models.CharField(max_length=50)
    company = models.ForeignKey('Company.Company', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Using special methods we can identify the profile
        object byt it's name attribute"""
        return f"{self.name}'s profile"

    def save(self, *args, **kwargs):
        """this method helps us to create a profile one a new user is created"""
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
