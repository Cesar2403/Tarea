"""Escribir un programa que pida al
    usuario su peso (en kg) y estatura
    (en metros), calcule el índice de
    masa corporal y lo almacene en una
    variable, y muestre por pantalla la
    frase Tu índice de masa corporal es
    <imc> donde <imc> es el índice de
    masa corporal calculado redondeado
    con dos decimales. """

peso = int(input("Introduzca su peso en kg"))
altura = float(input("Introduzca su altura en metros"))

def calcularImc(peso, altura):
    imc = peso / (altura*altura)
    return float(round(imc, 2))

print("Tu índice de masa corporal es ", calcularImc(peso, altura))