from django.db import models
from students.models import Student, Course
from subjects.models import Subject



class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Boletín de {self.student} - {self.course}"

class Grade(models.Model):
    report_card = models.ForeignKey(ReportCard, related_name='grades', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Nota de {self.subject} para {self.report_card.student}"
    

# Create your models here. 
# Explicación de los modelos:
# ReportCard:

# Este modelo tiene una relación con un estudiante (ForeignKey a Student) y con un curso (ForeignKey a Course).
# Cada boletín tendrá una fecha de creación (created_at) y una fecha de última actualización (updated_at).
# El método __str__() devuelve una representación legible del boletín, mostrando el nombre del estudiante y el curso.
# Grade:

# Cada instancia del modelo Grade representa una nota para una materia específica de un boletín.
# Se relaciona con un boletín mediante un ForeignKey a ReportCard y también con una materia mediante otro ForeignKey a Subject.
# El campo grade es un número decimal que almacena la calificación (hasta dos decimales).
# También se puede agregar un campo comments para agregar observaciones o comentarios sobre la nota.

  # Esto asume que ya tienes un modelo de Subject en la app de subjects