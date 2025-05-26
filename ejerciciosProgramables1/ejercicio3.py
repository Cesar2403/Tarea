"""l equipo de fútbol nacional Las Tuercas F.C. cuenta con 25 jugadores en su planilla, cada uno de
ellos recibe un salario mensual diferente y el equipo paga los salarios
en efectivo. Por lo que le ha solicitado desarrollar un programa que reciba el salario de cada uno
de los futbolistas, posterior, debe informar cuál es el monto de dinero que se debe retirar del
banco y la denominación de billetes y monedas necesaria para poder realizar el pago exacto en
efectivo. Considere las denominaciones de billetes y monedas disponibles en nuestro país.
Para ejemplificar los cálculos a realizar se presenta la siguiente información. El jugador “Luis”
gana ₡1,845,725 lo que implica que para hacer su pago se requiere el siguiente desglose.
Denominación Cantidad Monto
Una vez calculado el desglose de un jugador, debe acumular la cantidad de cada denominación
por todos los jugadores. Eso significa que debe indicar la sumatoria de todos los billetes de 50
mil, todos los de 20 mil, etc."""

def salario_recibir():
    for i in range (0, 16):
        lista_salarios = []
        lista_jugadores = []
        nombre_jugador = str(input("Introduzca su nombre"))
        cantidad_salario = int(input("Introduzca su salario"))
        lista_jugadores.append(nombre_jugador)
        lista_salarios.append(cantidad_salario)
    return lista_jugadores, lista_salarios

def calculador_denominaciones(lista_salarios, lista_jugador):
    x = 0
    for i in range (0, 16):
        salario_por_pagar = lista_salarios[x]

        billetes_veinte = salario_por_pagar // 20
        residuo_billetes_veinte = salario_por_pagar % 20
        if residuo_billetes_veinte != 0:
            billetes_diez = residuo_billetes_veinte // 10
            residuo_billetes_diez = residuo_billetes_veinte % 10
            if residuo_billetes_diez != 0:
                billetes_cinco = residuo_billetes_diez // 5
                residuo_billetes_cinco = residuo_billetes_diez % 5
                if residuo_billetes_cinco != 0:
                    billetes_dos = residuo_billetes_cinco // 2
                    residuo_billetes_dos = residuo_billetes_cinco % 2
                    if residuo_billetes_dos != 0:
                        billetes_uno = billetes_dos // 1
                        residuo_billetes_uno = residuo_billetes_dos % 1
        lista
        print ("El jugador:" + lista_jugador + " tiene un salario de " + lista_salarios + "")