"""Imagina que acabas de abrir una nueva cuenta
de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se
cobran hasta finales de año, se te añaden al
balance final de tu cuenta de ahorros. Escribir
un programa que comience leyendo la cantidad
de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa
debe calcular y mostrar por pantalla la cantidad
de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales."""

dinero_introducido = float(input("Introduzca el dinero a su cuenta"))
primer_ano = dinero_introducido + dinero_introducido * 0.04
segundo_ano = primer_ano + primer_ano * 0.04
tercer_ano = segundo_ano + segundo_ano * 0.04

print(float(round(primer_ano, 2)), float(round(segundo_ano, 2)), float(round(tercer_ano, 2)), round(dinero_introducido, 2))