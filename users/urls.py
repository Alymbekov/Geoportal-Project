from django.urls import path
from users import views as core_views

urlpatterns = [
    path('signup/', core_views.signup, name="signup")
]
