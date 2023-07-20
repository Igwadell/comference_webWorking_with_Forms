from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    photo = models.ImageField(upload_to='speakers/', null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.name