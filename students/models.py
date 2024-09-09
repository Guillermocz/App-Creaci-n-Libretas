from django.db import models

# Create your models here.

class Course(models.Model):
    nombre_de_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_de_curso
    

class Student(models.Model):
    nombre_completo = models.CharField(max_length=255)
    id_canvas = models.CharField(max_length=100, unique=True)  # Identificador único en Canvas
    curso = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo
    

