from . import views
from geoportal.views import (
        post_list,
        PostDetailView,
        maps,
        CreatePostView,
        PostUpdateView,
        PostDeleteView,

)

from django.urls import path, include
app_name = 'cities'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('blog-post/', post_list, name="blog-post"),
    path('blog-post/<int:pk>/', PostDetailView.as_view(), name="blog-single"),
    path('maps/', maps, name="maps"),
    path('city/', views.CitiesListView.as_view(), name="city-list"),
    path('city/<int:pk>/', views.CitiesDetailView.as_view(), name="city-detail"),
    path('blog-post/create/', CreatePostView.as_view(), name="post-create"),
    path('blog-post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('blog-post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
]
