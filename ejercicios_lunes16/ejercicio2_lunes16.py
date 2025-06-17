import math

def menu():
    print("1.Seno")
    print("2.Coseno")
    print("3.Tangente")
    print("4.Exponencial")
    print("5.Raíz")
    print("6.Logaritmo")
    opcion = int(input("Elige del 1 al 6:  "))
    num = int(input("Que número quieres calcular?"))
    return opcion, num

def main():
    opcion, num = menu()
    print("Numero" + " " + "Resultado")
    for i in range(1, num + 1):
        if opcion == 1:
            print(str(i) + " " + str(math.sin(i)))
        elif opcion == 2:
            print(str(i) + " " + str(math.cos(i)))
        elif opcion == 3:
            print(str(i) + " " + str(math.tan(i)))
        elif opcion == 4:
            print(str(i) + " " + str(math.exp(i)))
        elif opcion == 5:
            print(str(i) + " " + str(math.sqrt(i)))
        elif opcion == 6:
            print(str(i) + " " + str(math.log(i)))
        else:
            print("Solo del 1 al 6")
            break

main()