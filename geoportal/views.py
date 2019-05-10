from .models import WorldBorder
from django.shortcuts import render
from django.views.generic import DetailView


class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = WorldBorder
# Create your views here.
