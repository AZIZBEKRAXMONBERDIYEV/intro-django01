from django.urls import path
from .views import home, about


urlpatterns = [
    path('home/', home),  # 'api/home' endpoint
    path('about/', about),  # 'api/home' endpoint
]
