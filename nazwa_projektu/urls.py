from django.urls import path
from frontend_demo import views  # Upewnij się, że importujesz widoki ze swojej aplikacji

urlpatterns = [
    path('', views.index, name='index'),
]