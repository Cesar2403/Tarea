"""Usted ha sido contratado para desarrollar un programa que le ayude a controlar las notas de los
estudiantes de los 3 cursos de Introducción a la Programación, cada curso cuenta con 5
estudiantes. La aplicación tiene por objetivo que una vez que esté ingresadas las notas, la
aplicación nos brinde algunos datos.
- Se debe solicitar la nota final del curso de todos los estudiantes y ubicarlos en un arreglo de dos
dimensiones.
- A partir de los datos presentes en el arreglo, debe calcular la nota promedio de todos los
estudiantes y mostrarla al usuario.
- A partir de los datos presentes en el arreglo, debe calcular la nota promedio por cada uno de los
grupos y mostrar los promedio al usuario informando el grupo al que pertenece.
- A partir de los datos presentes en el arreglo, debe mostrar al usuario por cada grupo cuál es el
porcentaje de estudiantes aprobados, recuerde que los estudiantes aprobados son aquellos que
obtuvieron al menos una nota de 70.
- A partir de los datos presentes en el arreglo, debe mostrar al usuario cuál ha sido la nota mayor y
la menor por cada uno de los grupos.
- Cada una de las opciones mencionadas debe ser creada en un sub proceso"""

def obtener_notas():
    lista_notas = [],[],[]
    numero_grupo = 1
    numero_estudiante = 1
    i = 1
    for i in range (1,5):
        for j in range (1,5):
            notas = int(input("Introducir la nota del estudiante"))
            lista_notas.append(notas)
            numero_estudiante = numero_estudiante + 1
            if i == 5:
                numero_grupo = numero_grupo + 1
                numero_estudiante = numero_estudiante - 4
            elif i == 10:
                numero_grupo = numero_grupo + 1
                numero_estudiante = numero_estudiante - 4

