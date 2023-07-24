from django.urls import path
from .views import home, about, get_data


urlpatterns = [
    path('home/', home),  # 'api/home' endpoint
    path('about/', about),  # 'api/home' endpoint
    path('get-data/', get_data),  # 'api/get-data' endpoint
]
