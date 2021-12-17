from django.shortcuts import render
from cities.models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from cities.forms import CityForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

#Lets you import everything instead of a list
__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    #if pk:
        # Since the name is unique, we can use the "first" method
        # filter() is an error handler
        # If you use the get() function, you can get into "does not exits" errors
        # There is a get_obcject_or_404() function, but it gives a "404" error
        # city = City.objects.filter(id=pk).first()
        # context = {'object': city}
        # return render(request, 'cities/detail.html', context)
    form = CityForm()
    queryset = City.objects.all()

    lst = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form' : form}
    return render(request, 'cities/home.html', context)

# The condensed form of the entry "if pk"
class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    

class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно добавлен"

class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    #template_name = "cities/delete.html"
    success_url = reverse_lazy('cities:home')

    # Corrects an error with request.GET()
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)
    
class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context