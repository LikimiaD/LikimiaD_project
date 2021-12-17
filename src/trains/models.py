from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City

class Train(models.Model):
    name = models.CharField(max_length=50,unique=True,
                            verbose_name='Номер поезда')
    travel_time = models.PositiveBigIntegerField(verbose_name='Время в пути')
    # CASCADE removal from the city table then all other references are removed
    # from_city = models.ForeignKey(City, on_delete=models.CASCADE)
    # PROTECT will not let you delete as long as there is at least one entry in another
    # from_city = models.ForeignKey(City, on_delete=models.PROTECT)
    # SET_NULL when deleting from the city table within a given entry sets the value to NULL
    # from_city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,blank=True)


    # related_name -> Created to get a certain set of information from one model, 
    # not all at once
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, 
                                        related_name='from_city_set',
                                        verbose_name='Из какого города')
    # Alternative models.ForeignKey(City...) => models.ForeignKey('cities.city'...)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                        related_name='to_city_set',
                                        verbose_name='В какой город')

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def clean(self) -> None:
        if self.from_city == self.to_city: raise ValidationError('Изменить город прибытия')
        # Train == self.__class__
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city,
                                    travel_time=self.travel_time).exclude(pk=self.pk)
        # If it is a new entry, the exclude() function does not work
        # If we edit, the ID will be removed from the queryset

        # If there is at least one entry
        if qs.exists():
            raise ValidationError('Изменить время в пути')
        

    def save(self,*args,**kwargs):
        self.clean()
        super().save(*args,**kwargs)
