"""Escribir un programa que pida al
usuario dos números enteros y
muestre por pantalla la <n> entre
<m> da un cociente <c> y un resto
<r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y
<r> son el cociente y el resto de la
división entera respectivamente."""

num1 = int(input("Introduzca un numero"))
num2 = int(input("Introduzca un numero"))
cociente = num1 % num2
resto = num1 // num2

print(num1, num2, cociente, resto)