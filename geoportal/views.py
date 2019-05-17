from .models import WorldBorder
from django.shortcuts import render
from django.views.generic import ListView,DetailView


class CitiesListView(ListView):
    template_name = 'cities/city-list.html'
    model = WorldBorder

class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = WorldBorder

def index(request):
    return render(request, 'index.html', {})
