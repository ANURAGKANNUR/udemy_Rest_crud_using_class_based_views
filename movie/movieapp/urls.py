
from django.urls import path,include
from .views import MovieListAV,MovieDetailAV

urlpatterns = [
    path('list/',MovieListAV.as_view()),
    path('<int:pk>',MovieDetailAV.as_view())
]
