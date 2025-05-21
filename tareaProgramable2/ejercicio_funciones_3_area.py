"""Escribir una función que
calcule el área de un círculo y
otra que calcule el volumen de
un cilindro usando la primera
función.
"""

import math

def formula_area_circulo (radio):
    return (radio * radio) * math.pi

def formula_volumen_cilindro (area_circulo, altura_cilindro):
    return area_circulo * altura_cilindro

radio = float(input("Ingrese el valor del radio del circulo: "))
area_circulo = formula_area_circulo(radio)

print ("El area del circulo es de: ", round(area_circulo, 2))

altura_cilindro = float(input("Ingrese el valor de la altura del cilindro: "))
volumen_cilindro = formula_volumen_cilindro(area_circulo, altura_cilindro)

print ("El volumen del cilindro es de: ",round(volumen_cilindro, 2))