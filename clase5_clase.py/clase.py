import os
#Realizar  el código en Python aplicando POO:
#Desarrollar un programa con el ejemplo de la clase base
#Animal y clases hijas: Herbívoro, Carnívoro, Omnívoro. (usar el
#concepto de Herencia).

class Animal:
    def __init__ (self, nombre,edad,especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_atributos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"especie: {self.especie}")


class Herbivoro(Animal):
    def __init__(self, nombre, edad, especie, planta_favorita):
        super().__init__(nombre, edad, especie)
        self.planta_favorita = planta_favorita

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"planta favorita: {self.planta_favorita}")


class Carnivoro(Animal):
    def __init__(self, nombre, edad, especie, presa_favorita):
        super().__init__(nombre, edad, especie)
        self.presa_favorita = presa_favorita

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"presa favorita: {self.presa_favorita}")


class Omnivoro(Animal):
    def __init__(self, nombre, edad, especie, planta_favorita, presa_favorita):
        super().__init__(nombre, edad, especie)
        self.planta_favorita = planta_favorita
        self.presa_favorita = presa_favorita

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"planta favorita: {self.planta_favorita}")
        print(f"presa favorita: {self.presa_favorita}")

#instancia de objetos
herbivoro = Herbivoro("Bambi", 2, "Ciervo", "Hierba")
carnivoro = Carnivoro("Simba", 3, "León", "Antílopes")
omnivoro = Omnivoro("Pumba", 4, "Jabalí", "Frutas", "Insectos")
#mostrar atributos
print("Herbívoro:")
herbivoro.mostrar_atributos()
print("\nCarnívoro:")
carnivoro.mostrar_atributos()
print("\nOmnívoro:")
omnivoro.mostrar_atributos()


import os
#Realizar  el código en Python aplicando POO:
#Desarrollar un programa con el ejemplo de la clase base
#Animal y clases hijas: Herbívoro, Carnívoro, Omnívoro. (usar el
#concepto de Herencia).

class animal:
    def __init__ (self, nombre, especie, edad ):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
   

class carniboro(animal):
    def __init__ (self, nombre, especie, edad):
        print(f"nombre: {self.nombre}")
        print(f"especie: {self.especie}")
        print(f"edad: {self.edad}")

class herbiboro(animal):
    def __init__ (self, nombre, especie, edad):
        print(f"nombre: {self.nombre}")
        print(f"especie: {self.especie}")
        print(f"edad: {self.edad}")

class obniboro(animal):
    def __init__ (self, nombre, especie, edad):
        print(f"nombre: {self.nombre}")
        print(f"especie: {self.especie}")
        print(f"edad: {self.edad}")

conejo = obniboro("conejo", "obniboro", "5")
oso = carniboro("oso", "carniboro", "10")
vaca = obniboro("vaca", "herbiboro", "7")