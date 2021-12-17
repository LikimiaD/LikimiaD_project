from django.urls import path

from trains.views import *

urlpatterns = [
    #path('', home, name = 'home'),
    path('', TrainListView.as_view(), name = 'home'),
    # The name of the function that allows you to generate the address dynamically
    path('detail/<int:pk>/', TrainDetailView.as_view(), name = 'detail'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name = 'delete'),
    # Can get an integer representation as "pk" and pass it

    path('add/', TrainCreateView.as_view(), name = 'create'),
    
]