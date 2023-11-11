from django.urls import path
from .views import evaluacion_ambiental, resultados

urlpatterns = [
    path('',evaluacion_ambiental, name='evaluacion_ambiental'),
    path('resultados/',resultados, name='resultados'),
]
