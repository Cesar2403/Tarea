"""Escribir un programa que almacene la cadena de
caracteres contraseña en una variable, pregunte al
usuario por la contraseña hasta que introduzca la
contraseña correcta. Finalmente indique el número
de intentos que realizó."""

password = "contrasena"
attemps = 0

question = str(input("Introduzca la contraseña\n"))

while question != password:
    print ("Contraseña incorrecta")
    question = str(input("Introduzca la contraseña\n"))
    attemps = attemps + 1

print ("Esa es la contraseña correcta \n Lo intentaste ", attemps ," veces")