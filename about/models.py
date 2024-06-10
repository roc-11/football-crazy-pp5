from django.db import models

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text and profile image
    """
    title = models.CharField(max_length=200)
    profile_image_url = models.URLField(max_length=1024, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
