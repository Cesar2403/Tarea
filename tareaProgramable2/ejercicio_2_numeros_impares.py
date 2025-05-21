"""Escribir un programa que pida al usuario un número
entero positivo y muestre por pantalla todos los
números impares desde 1 hasta ese número
separados por comas."""

numero = int(input("Ingresa un numero entero positivo \n"))

def numeros_impares():
    x = 0
    lista_numeros = []
    while x < numero + 1:
        if x % 2 == 1:
            lista_numeros.append(x)
        x = x + 1
    return lista_numeros

print(numeros_impares())