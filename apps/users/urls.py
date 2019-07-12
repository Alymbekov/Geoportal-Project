from django.contrib import admin
from django.urls import path, include
from .views import signup, home, secret_page, update_profile


urlpatterns = [
    path('home/', home, name="home"),
    path('signup/', signup, name="signup"),
    path('secret/', secret_page, name="secret_page"),
    path('profiles/', update_profile, name="profile"),
]
