"""Escribir un programa que almacene las
asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla. Utilice
recursividad."""


def main():
    asignaturas = []

    for x in range(5):
        asignatura = input("Introduzca el nombre de la asignatura: ")
        asignaturas.append(asignatura)

    for i in range(len(asignaturas)):
        print("Llevas de materia: " + asignaturas[i])

main()