#datos entrada- capturasCO2 : una coleccion con capturas de concentracion de CO2cada cinco min ejem 420 430 425 y 450
# Tiempos_capturas: una coleccion dque sirve de bitacora para anotar en que momoento se hixzo cada captura de co2 cada campo i esta ocleccion indica la hora a la q se hizo captura i de la coleccion capturas co2 
#ejem 14:00, 14:05

cantidad_co2 = [430 , 420 , 410 , 415 , 450]
hora_co2 = ["14:05" , "14:10" , "14:15" , "14:20" , "14:25"]

def cantidad_capturas(cantidad_co2):
    return len(cantidad_co2)

def promedio_capturas(cantidad_co2):    
    promedio = sum(cantidad_co2) / len(cantidad_co2)
    return promedio

def mayor_concentracion(cantidad_co2):
    mayor = max(cantidad_co2)
    return mayor

def menor_concentracion(cantidad_co2):
    menor = min(cantidad_co2)
    return menor

def hora_mayor(mayor):
    for i in range (len(cantidad_co2)):
        if mayor == cantidad_co2[i]:
            posicion_hora_mayor = hora_co2[i]
    return posicion_hora_mayor
    
def hora_menor(menor):
    for i in range (len(cantidad_co2)):
        if menor == cantidad_co2[i]:
            posicion_hora_menor = hora_co2[i]
    return posicion_hora_menor

def mostrar_hora_diferencia(cantidad_co2, hora_co2):
    for i in range (len(cantidad_co2)):
        j = i + 1
        if i + 1 == len(cantidad_co2):
            j = 0
        if cantidad_co2[i] < (cantidad_co2[j] - 15):
            print (hora_co2[i] + " " + " " +  hora_co2[i+1])

mayor = mayor_concentracion(cantidad_co2)
menor = menor_concentracion(cantidad_co2)

def main():
    print (cantidad_capturas(cantidad_co2))
    print(promedio_capturas(cantidad_co2))
    print(mayor_concentracion(cantidad_co2))
    print(menor_concentracion(cantidad_co2))
    print(hora_mayor(mayor))
    print(hora_menor(menor))
    print(mostrar_hora_diferencia(cantidad_co2, hora_co2))
    
main()
