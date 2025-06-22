class Animal:
    def __init__(self, nombre, especie, numero_patas, genero, edad):
        self.nom = nombre
        self.espe = especie
        self.num_pat = numero_patas
        self.gen = genero
        self.eda = edad

    def description(self):
        print("El animal se llama %s, es de la especie %s, tiene %i patas, es %s y tiene %i años." % (self.nom, self.espe, self.num_pat, self.gen, self.eda))

    def cambiar_nombre(self, nuevo_nombre):
        self.nom = nuevo_nombre

    def cambiar_edad(self, nueva_edad):
        self.eda = nueva_edad