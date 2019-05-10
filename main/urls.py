
from django.contrib.gis import admin
from django.urls import path, include

urlpatterns = [
    path('geoportal/', include('geoportal.urls')),
    path('admin/', admin.site.urls),
]
