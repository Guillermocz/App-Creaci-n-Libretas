import csv
import os
import django
from django.core.exceptions import ObjectDoesNotExist

# Cargar configuraciones de Django (ajusta la ruta si es necesario)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pacifico_libretas.settings')
django.setup()

from students.models import Course, Student

# Función para cargar cursos desde el CSV
def cargar_cursos(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Saltar la primera fila si es un encabezado
        next(reader, None)
        
        # Leer y procesar los cursos
        for row in reader:
            # En este caso, asumimos que la columna del curso es la primera en el CSV
            nombre_curso = row[0].strip()  # Eliminamos espacios adicionales

            # Crear el curso si no existe
            curso, created = Course.objects.get_or_create(nombre_de_curso=nombre_curso)
            if created:
                print(f"Curso '{nombre_curso}' creado.")
            else:
                print(f"Curso '{nombre_curso}' ya existía.")

# Función para cargar estudiantes desde el CSV
def cargar_estudiantes(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Si los campos están delimitados por punto y coma
        print(f"Encabezados del CSV: {reader.fieldnames}")
        
        for row in reader:
            nombre_completo = row['nombre_completo']
            id_canvas = row['id_canvas']
            nombre_curso = row['curso']

            try:
                curso = Course.objects.get(nombre_de_curso=nombre_curso)
                student, created = Student.objects.get_or_create(
                    nombre_completo=nombre_completo,
                    id_canvas=id_canvas,
                    curso=curso
                )
                if created:
                    print(f"Estudiante '{nombre_completo}' creado.")
                else:
                    print(f"Estudiante '{nombre_completo}' ya existía.")
            except ObjectDoesNotExist:
                print(f"Error: el curso '{nombre_curso}' no existe.")

# Ruta de los archivos CSV
ruta_cursos = r'C:\Users\calva\Documents\ProyectosING\App-Creación Libretas\Carga-csv\Courses.csv'
ruta_estudiantes = r'C:\Users\calva\Documents\ProyectosING\App-Creación Libretas\Carga-csv\Students.csv'

# Cargar los datos
cargar_cursos(ruta_cursos)
cargar_estudiantes(ruta_estudiantes)