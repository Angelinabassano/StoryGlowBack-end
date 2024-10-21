from django.db import models
from cloudinary.models import CloudinaryField


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    cover_photo = CloudinaryField('image', folder='cover_photo', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

