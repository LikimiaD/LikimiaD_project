from django.db import models
from django.urls import reverse

class City(models.Model): # Create BD "City"
    name = models.CharField(max_length=100, unique=True, verbose_name="Город")
    # verbose_name -> Russification of the "Name" field

    def __str__(self): # Change ID to Name
        return self.name

    class Meta: #Change name tab
        verbose_name = 'City' # Name for tab
        verbose_name_plural = 'Cities' # Name for Class
        ordering = ['name'] # Alphabetical sorting

    # After creating/adding a city, we will go to the detail page
    def get_absolute_url(self):
        return reverse("cities:detail", kwargs={"pk": self.pk})
    