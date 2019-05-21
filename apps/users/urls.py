from django.contrib import admin
from django.urls import path, include
from .views import signup, home, secret_page


urlpatterns = [
    path('home/', home, name="home"),
    path('signup/', signup, name="signup"),
    path('secret/', secret_page, name="secret_page"),
]
