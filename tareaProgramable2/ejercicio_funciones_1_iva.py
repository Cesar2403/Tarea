"""Escribir una función que
calcule el total de una factura
tras aplicarle el IVA. La función
debe recibir la cantidad sin IVA
y el porcentaje de IVA a
aplicar, y devolver el total de
la factura. Si se invoca la
función sin pasarle el
porcentaje de IVA, deberá
aplicar un 21%"""

def factura(factura_sin_iva, iva = 21):
    total_factura = factura_sin_iva + (factura_sin_iva * (iva / 100))
    return total_factura


monto = float(input("Ingrese el valor de la factura sin el IVA: "))
valor_iva = input("Ingrese el valor porcentual del IVA: ")

if valor_iva:
    print(factura(monto, float(valor_iva)))
else:
    print(factura(monto))

