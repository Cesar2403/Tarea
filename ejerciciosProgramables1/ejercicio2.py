"""La escuela de Estadística requiere desarrollar un programa que le permita realizar
algunos cálculos estadísticos importantes para la toma de decisiones.
- Se debe capturar la cantidad de pasajeros de cada uno de los 4 servicios que se
realizan al día para los 5 días de la semana.
- Ya que el autobús tiene un capacidad máxima de 60 pasajeros, se debe verificar que
no se ingrese un valor mayor a 60.
- El programa debe mostrar el promedio de pasajeros de cada uno de los días.
- El programa debe mostrar el promedio general de todos los días y todos los
servicios.
- El programa debe mostrar cuál de los 4 servicios durante el día es el mejor (en el
que se transportan más personas).
- El programa debe mostrar el momento en que menos pasajeros se transportaron
(servicio y día).
- La captura de los datos y cada uno de los procesos que muestran información deben
estar ubicados en su propio sub proceso.
- Debe utilizar un arreglo de 2 dimensiones.
- Debe utilizar nombres representativos para los elementos (variables, arreglos, sub
procesos, etc.)."""

DIAS = 5
SERVICIOS = 4
MAX_PASAJEROS = 60

def obtener_datos():
    pasajeros_dia = [0] * DIAS
    pasajeros_servicio = [0] * SERVICIOS
    cantidad = 0
    for dia in range(DIAS):
        for servicio in range(SERVICIOS):
            while True:
                try:
                    cantidad = int(input("Pasajeros del servicio " + str(servicio + 1) + " del día " + str(dia + 1) + ": "))
                    
                    if cantidad >= MAX_PASAJEROS:
                        print("Error. La cantidad de pasajeros no puede ser mas de 60")
                    else:
                        pasajeros_dia[dia] += cantidad
                        pasajeros_servicio[servicio] += cantidad
                        break
                except ValueError:
                    print("Introduce un valor menor a 60, porfavor")
    return pasajeros_dia, pasajeros_servicio

def promedio_dia(pasajeros_dia):
    for i in range(DIAS):
        promedio = pasajeros_dia[i] / SERVICIOS
        print("Promedio del día " + str(i + 1) + ": " + str(round(promedio, 2)))

def promedio_general(pasajeros_dia):
    total = sum(pasajeros_dia)
    promedio = total / (DIAS * SERVICIOS)
    print("Promedio general: " + str(round(promedio, 2)))

def mejor_servicio(pasajeros_servicio):
    mayor = -1
    servicio_mayor = 0
    for i in range(SERVICIOS):
        if pasajeros_servicio[i] > mayor:
            mayor = pasajeros_servicio[i]
            servicio_mayor = i + 1
    print("Mejor servicio servicio " + str(servicio_mayor) + " con " + str(mayor) + " pasajeros")


def peor_servicio(pasajeros_servicio):
    menor = MAX_PASAJEROS + 1
    servicio_menor = 0
    for i in range(SERVICIOS):
        if pasajeros_servicio[i] < menor:
            menor = pasajeros_servicio[i]
            servicio_menor = i + 1
    print("Peor servicio, servicio " + str(servicio_menor) + " con " + str(menor) + " pasajeros")


def main():
    try:
        pasajeros_dia, pasajeros_servicio = obtener_datos()
        promedio_dia(pasajeros_dia)
        promedio_general(pasajeros_dia)
        mejor_servicio(pasajeros_servicio)
        peor_servicio(pasajeros_servicio)
    except:
        print("Introduce un valor valido, porfavor")

main()
