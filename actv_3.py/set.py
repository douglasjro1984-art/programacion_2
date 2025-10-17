#Ejemplos aplicando Getters y Setters
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad       # atributo privado

    # Métodos GET
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Métodos SET
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:  # validación
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

# Uso de la clase
p1 = Persona("Ana", 11)

print("Nombre:", p1.get_nombre())
print("Edad:", p1.get_edad())

# Modificando los atributos usando los métodos SET
p1.set_nombre("María")
p1.set_edad(30)

print("Nuevo Nombre:", p1.get_nombre())
print("Nueva Edad:", p1.get_edad())
