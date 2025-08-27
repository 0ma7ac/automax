from django.urls import path

from main.views import landing_main, home_view, list_view



urlpatterns = [
    path('', landing_main, name='main'),
    path('home/', home_view, name='home'), 
    path('list/', list_view, name='list')
]
