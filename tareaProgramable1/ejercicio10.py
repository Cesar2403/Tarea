"""Escribir un programa que pregunte al usuario los
números ganadores de la lotería primitiva, los
almacene en una lista y los muestre por pantalla
ordenados de menor a mayor. Utilice
recursividad."""

def main():
    lista_ganadores = []
    for x in range(5):
        num_ganador = int(input("Introduzca el numero ganador de la loteria: "))
        lista_ganadores.append(num_ganador)
        lista_ganadores_ordenada = sorted(lista_ganadores)
    return lista_ganadores_ordenada
print(main())
