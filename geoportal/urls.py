from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.index, name="index"),
    path('city/', views.CitiesListView.as_view(), name="city-list"),
    path('city/<int:pk>/', views.CitiesDetailView.as_view(), name="city-detail"),
]
