
from django.contrib.gis import admin
from django.urls import path, include

urlpatterns = [
    path('geoportal/', include('geoportal.urls')),
    path('accounts/auth/', include('users.urls')),
    path('admin/', admin.site.urls),
]
