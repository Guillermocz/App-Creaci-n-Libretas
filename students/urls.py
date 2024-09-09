# students/urls.py
from django.urls import path
from .views import estudiantes_por_curso

urlpatterns = [
    path('estudiantes-por-curso/', estudiantes_por_curso, name='estudiantes_por_curso'),
]
