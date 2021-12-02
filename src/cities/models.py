from django.db import models

class City(models.Model): # Create BD "City"
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): # Change ID to Name
        return self.name
    class Meta: #Change name tab
        verbose_name = 'City' # Name for tab
        verbose_name_plural = 'Cities' # Name for Class
        ordering = ['name'] # Alphabetical sorting