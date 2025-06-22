from ejercicio_animal import Animal

animales = []
x = ""
while x != "x":
    nome = input("\nIntroduzca el nombre del animal: ")
    especie = input("Introduzca la especie del animal: ")
    patas = int(input("Introduzca el número de patas: "))
    genero = input("Introduzca el género del animal: ")
    edad = int(input("Introduzca la edad del animal: "))

    animal = Animal(nome, especie, patas, genero, edad)
    animales.append(animal)

    animal.description()

    if input("\n¿Cambiar nombre? (s/n): ").lower() == "s":
        nuevo_nombre = input("Nuevo nombre: ")
        animal.cambiar_nombre(nuevo_nombre)
        animal.description()

    if input("¿Cambiar edad? (s/n): ").lower() == "s":
        nueva_edad = int(input("Nueva edad: "))
        animal.cambiar_edad(nueva_edad)
        animal.description()

    x = input("\nPresione 'x' para salir o enter para continuar: ")

for a in animales:
    a.description()