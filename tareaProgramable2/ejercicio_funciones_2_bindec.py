"""Escribir una función que
convierta un número decimal
en binario y otra que convierta
un número binario en decimal"""

def bin_to_dec(num):
    return int(num, 2)
def dec_to_bin(num):
    return bin(num)[2:]

num_decimal = int(input("Ingrese un numero decimal: "))
print (dec_to_bin(num_decimal))

num_binario = input("Ingrese un numero binario: ")
print(bin_to_dec(num_binario))