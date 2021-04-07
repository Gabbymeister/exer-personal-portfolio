from django.db import models

# This is where you make your database variables
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
