from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
