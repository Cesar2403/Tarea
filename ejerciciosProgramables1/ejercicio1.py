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
    notas = []
    for grupo in range(3): 
        grupo_notas = []
        print("\nIngresando notas para el grupo " + str(grupo + 1))
        for estudiante in range(5): 
            nota = float(input("Nota del estudiante " + str(estudiante + 1) + " del grupo " + str(grupo + 1) + "\n"))
            grupo_notas.append(nota)
        notas.append(grupo_notas)
    return notas


def promedio_general(notas):
    total = sum(5 for grupo in notas)
    cantidad = sum(5 for grupo in notas)
    promedio = total / cantidad
    print("\nEl promedio general de todos los estudiantes es: " + str(round(promedio, 2)))

def promedio_grupo(notas):
    print("\nPromedio por grupo:")
    for i, grupo in enumerate(notas):
        promedio = sum(grupo) / 5
        print("Grupo " + str(i + 1) + ": " + str(round(promedio, 2)))

def porcentaje_aprobados(notas):
    for i, grupo in enumerate(notas):
        aprobados = sum(1 for nota in grupo if nota >= 70)
        porcentaje = (aprobados / 5) * 100
        print("Grupo " + str(i + 1) + ": " + str(round(porcentaje, 2)) + "% aprobados")

def nota_max_min(notas):
    for i, grupo in enumerate(notas):
        nota_max = max(grupo)
        nota_min = min(grupo)
        print("Grupo " + str(i + 1) + ": Mayor es " + str(nota_max) + ", Menor es " + str(nota_min))
def main():
    while True:
        try:
            notas = obtener_notas()
            promedio_general(notas)
            promedio_grupo(notas)
            porcentaje_aprobados(notas)
            nota_max_min(notas)
        except ValueError:
            print("Introduce valores validos, porfavor")

main()
