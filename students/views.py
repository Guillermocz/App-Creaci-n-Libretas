from django.shortcuts import render
from .models import Course, Student
from subjects.models import Subject

def estudiantes_por_curso(request):
    # Obtener todos los cursos
    cursos = Course.objects.all()

    # Crear un diccionario para pasar los datos a la plantilla
    datos_cursos = []
    for curso in cursos:
        # Obtener los estudiantes de cada curso
        estudiantes = Student.objects.filter(curso=curso)
        
        # Obtener las materias que tienen los estudiantes en ese curso
        materias = Subject.objects.filter(cursos=curso)

        datos_cursos.append({
            'curso': curso,
            'estudiantes': estudiantes,
            'materias': materias
        })

    # Renderizar la plantilla con los datos
    return render(request, 'estudiantes_por_curso.html', {'datos_cursos': datos_cursos})