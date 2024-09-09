from django.db import models
from students.models import Course

class Subject(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Course)  # Relación muchos a muchos con cursos

    def __str__(self):
        return self.nombre