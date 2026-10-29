from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/gry/', views.api_gry, name='api_gry'),
]