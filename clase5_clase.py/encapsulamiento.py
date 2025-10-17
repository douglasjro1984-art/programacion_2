# Encapsulamiento oculta los atributos internos.  
# El encapsulamiento es el concepto
# que permite restringir el acceso a ciertos
#datos y métodos dentro de una clase. En Python,
# los atributos y métodos se #pueden hacer "privados"
# usando guiones bajos, aunque es una convención más
# que una restricción estricta..
# Abstracion  define la interfaz que hace el objeto sin mostrar detalles
# del funcionamiento.
# La abstracción se refiere al proceso de ocultar los detalles
# internos de  implementación y mostrar
# solo la funcionalidad esencial

# Ejercicio  Crear un objeto CuentaBancaria donde podamos depositar,
# retirar  y ver saldo,
# pero no modificarlo directamente
# libreria ABC para crear clases abstractas
# abc = Abstract Base Class
from abc import ABC ,abstractmethod
import os

os.system ("cls")

# Definamos las abstrata para cuenta en sus metodos  
# clase padre
class Cuenta (ABC):
    @abstractmethod # DECORADOR
    def depositar (self, monto):
        pass
   
    @abstractmethod
    def retirar (self, monto):
        pass
       
# Encasulamiento
# clase hijo
class Cuentabancaria (Cuenta):
    def __init__(self, titular, saldo = 0 ):
        self.titular = titular
        self.__saldo = saldo # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print ( f" Deposito exitoso. Saldo Actual : {self.__saldo}")
        else:
            print ("El monto a depositar tiene que ser positivo ")
           
    def retirar (self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print (f"Retiro exitoso. Saldo Actual :{self.__saldo}")
        else:
            print ("Fondo Insuficiente o monto inválido")
   
    def versaldo (self):
        print (f" Saldo disponible: {self.__saldo}")
       
   
    # Programa principal
    # son los valores que agregamos a la clase para crear el objeto
titular = input ("Ingrese el nombre titular de la cuenta:    ")

saldo = int (input ("Ingrese el saldo actual de su cuenta"))
   
    # crear objeto de clase
cuenta1 = Cuentabancaria (titular, saldo)
cuenta1.versaldo ()
monto = int (input (" Ingrese el monto a depositar : "))
cuenta1.depositar (monto)
monto = int (input (" Ingrese el monto a retirar  : "))
cuenta1.retirar (monto)  
cuenta1.versaldo ()

cuenta1.__saldo = 5000000  # no se puede modificar directamente

cuenta1.versaldo ()
