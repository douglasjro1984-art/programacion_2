'''
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo
        self.edad = edad # Atributo
    def ladrar(self): # Método
        print(f"{self.nombre} está ladrando ¡Guau!")
# Crear objeto
mi_perro = Perro("Firulais", 3)
mi_perro.ladrar()
'''                


'''
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # CORRECCIÓN: Ahora solo necesita 'self'
    def ladrar(self): 
        # Usa self.nombre y self.edad para acceder a los datos internos del perro
        print(f"El perro {self.nombre}, de {self.edad} años, está ladrando.")
'''
# Ejemplo de varios objetos de una misma clase
'''
perro1=Perro("max",2)
perro2=Perro("Luna",5)

print(perro1.nombre, "tiene", perro1.edad, "años")
print(perro2.nombre, "tiene", perro2.edad, "años")
'''
'''
class CuentaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.saldo=saldo
        
    def despositar(self,monto):
        self.monto += monto
        
    def mostrar_saldo(self):
        print(f"Saldo del titular{self.titular}:${self.saldo}")
        
   
    c1=CuentaBancaria("Carla",1000)
    c1.depositar(500)
    c1.mostrar_saldo()
'''
class Animal:
    def __init__(self, nombre):
        self.nombre=nombre
        
class Perro(Animal):
    def sonido(self):
        print("Guau")
        
class Gato:
    def __init__(self, nombre):
        self.nombre=nombre
   
    def sonido(self):
        print("Miau")
        
animales=[Perro("Max"),Gato("Luna")]
for a in animales:
    a.sonido()
    
    
