from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City

class Route(models.Model):
    name = models.CharField(max_length=50,unique=True,
                            verbose_name='Название маршрута')
    travel_times = models.PositiveBigIntegerField(verbose_name='Общее время в пути')
    # CASCADE removal from the city table then all other references are removed
    # from_city = models.ForeignKey(City, on_delete=models.CASCADE)
    # PROTECT will not let you delete as long as there is at least one entry in another
    # from_city = models.ForeignKey(City, on_delete=models.PROTECT)
    # SET_NULL when deleting from the city table within a given entry sets the value to NULL
    # from_city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,blank=True)


    # related_name -> Created to get a certain set of information from one model, 
    # not all at once
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, 
                                        related_name='route_from_city_set',
                                        verbose_name='Из какого города')
    # Alternative models.ForeignKey(City...) => models.ForeignKey('cities.city'...)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                        related_name='route_to_city_set',
                                        verbose_name='В какой город')
    # ManyToManyField - several pointers to an external table
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']