# Escriba un algoritmo que realice
# operaciones aritméticas (suma, resta,
# multiplicación y división).

num1 = 10
num2 = 10

def operacionesAritmeticas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

print(operacionesAritmeticas(num1, num2))
