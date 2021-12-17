from django import forms

from cities.models import City

# Class-Based Search Model\Recordings
class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Введите название города'
        }))
    class Meta:
        model = City
        fields = ('name',)