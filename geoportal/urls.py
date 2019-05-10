from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('city/<int:pk>/', views.CitiesDetailView.as_view(), name="city-detail"),
]
