import os
import datatime 

os.system("cls")

class persona: 
    #constructor 
    def __init__(self, nombré,edad,DNI,sexo,peso,altura):
        self.nombré = nombré
        self.edad= edad
        self.DNI=DNI
        self.sexo=sexo
        self.peso=peso
        self.altura =altura
    def mostrar_datos(self):
        print(f"nombre: {self.nombre}")
        
        
    # principal
    # creamos un objeto de la clase persona
    # nombreobjeto= nombreclase (parámetros)
    
    
