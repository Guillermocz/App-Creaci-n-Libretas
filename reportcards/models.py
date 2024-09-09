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

    # Campos para el 1er parcial
    tai_1parcial = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="TAI 1er Parcial", default=0)
    aic_1parcial = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="AIC 1er Parcial", default=0)
    agc_1parcial = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="AGC 1er Parcial", default=0)
    lec_1parcial = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="LEC 1er Parcial", default=0)
    eva_1parcial = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="EVA 1er Parcial", default=0)
    
    # Promedio del 1er parcial
    promedio_1parcial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Promedio 1er Parcial")

    # Método para calcular el promedio del 1er parcial
    def calcular_promedio_1parcial(self):
        return (self.tai_1parcial + self.aic_1parcial + self.agc_1parcial + self.lec_1parcial + self.eva_1parcial) / 5

    # Sobrescribir el método save para calcular el promedio automáticamente al guardar
    def save(self, *args, **kwargs):
        self.promedio_1parcial = self.calcular_promedio_1parcial()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Notas de {self.subject} para {self.report_card.student}"
    

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