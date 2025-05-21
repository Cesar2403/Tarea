"""Arbol de navidad: Imprime un árbol de navidad
formado con * haciendo uso del while y de la
multiplicación de un entero por una cadena, cuyo
resultado en Python es replicar la cadena.
"""

x = 1
while x < 7:
    arbol = "*" * x
    print(arbol.center(9))
    x = x + 1