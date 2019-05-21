from django.urls import path
from . import views
from geoportal.views import PostListView, PostDetailView
from django.urls import path, include
app_name = 'cities'

urlpatterns = [
    path('', views.index, name="index"),
    path('blog-post/', PostListView.as_view(), name="blog-post"),
    path('blog-post/<int:pk>/', PostDetailView.as_view(), name="blog-single"),
    path('city/', views.CitiesListView.as_view(), name="city-list"),
    path('city/<int:pk>/', views.CitiesDetailView.as_view(), name="city-detail"),
]
