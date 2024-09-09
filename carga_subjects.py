import csv
import os
import django
from django.core.exceptions import ObjectDoesNotExist

# Cargar configuraciones de Django (ajusta la ruta si es necesario)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pacifico_libretas.settings')
django.setup()

from subjects.models import Subject
from students.models import Course

# Función para cargar subjects desde el CSV
def cargar_subjects(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")        
        for row in reader:
            nombre_asignatura = row['nombre']
            nombres_cursos = row['cursos'].split('|')  # Separar los cursos por el delimitador '|'
            print(row['nombre'], row['cursos'])

             # Crear o obtener la asignatura
            subject, created = Subject.objects.get_or_create(nombre=nombre_asignatura)
            if created:
                print(f"Asignatura '{nombre_asignatura}' creada.")
            else:
                print(f"Asignatura '{nombre_asignatura}' ya existía.")

             # Limpiar las relaciones existentes (opcional)
            subject.cursos.clear()

            # # Relacionar los cursos
            for nombre_curso in nombres_cursos:
                try:
                    curso = Course.objects.get(nombre_de_curso=nombre_curso.strip())
                    subject.cursos.add(curso)  # Relacionar curso con la asignatura
                    print(f"Curso '{nombre_curso}' relacionado con la asignatura '{nombre_asignatura}'.")
                except ObjectDoesNotExist:
                    print(f"Error: el curso '{nombre_curso}' no existe.")
            
             # Guardar las relaciones en la base de datos
            subject.save()

# Ruta del archivo CSV
ruta_subjects = r'C:\Users\calva\Documents\ProyectosING\App-Creación Libretas\Carga-csv\Subjects.csv'

# Cargar los datos
cargar_subjects(ruta_subjects)