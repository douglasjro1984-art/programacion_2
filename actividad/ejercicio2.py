#Escribe un programa en Python que permita que un estacionamiento cobre a sus
#clientes según el siguiente esquema:
#• Primeras 2 horas: $1000 por hora.
#• De la 3.a a la 5.a hora: $800 por hora.
#• A partir de la 6.a hora: $500 por hora.
#Se pide desarrollar un programa que:
#1. Solicite al usuario la cantidad de vehículos a procesar.
#2. Para cada vehículo, ingresar:
#o Patente
#o Cantidad de horas que estuvo estacionado
#3. Calcular el monto a pagar por cada vehículo usando una función.
#4. Mostrar un resumen con:
#o Patente
#o Horas
#o Monto a pagar
# Ejercicio 2: Sistema de cobro de estacionamiento

print("-----SISTEMA DE COBRO DE ESTACIONAMIENTO-----")
# Función para calcular el monto a pagar según las horas estacionadas
continuar = "s"  # Variable de control para el bucle
while continuar == "s":
    def cobrar_estacionamiento(horas):
        if horas <= 2:
           tarifa_por_hora = 1000  
           total = horas * tarifa_por_hora
           return total
        elif 3 <= horas <= 5:
           tarifa_por_hora = 800 
           total = horas * tarifa_por_hora
           return total
        elif horas >= 6:
           tarifa_por_hora = 500
           total = horas * tarifa_por_hora
           return total
        else:
           return 0

    cantidad_vehiculos = input("¿Cuántos vehículos se van a registrar? ")
    vehiculos = [] 

    for i in range(int(cantidad_vehiculos)):
        print(f"\nRegistrando vehículo {i + 1} de {cantidad_vehiculos}")
        numero_de_patente = input("Ingrese el número de patente del vehículo: ")
        horas_estacionado = input("Ingrese la cantidad de horas que estuvo estacionado: ")
        vehiculos.append({"patente": numero_de_patente, "horas": horas_estacionado})

        # Mostrar el resumen por cada vehículo (dentro del bucle)
        print("-----EVALUAR COBRANZA-----")
        print(f"Patente: {numero_de_patente}")
        print(f"Horas estacionado: {horas_estacionado}")
        print(f"Monto a pagar: ${cobrar_estacionamiento(int(horas_estacionado))}")
        
    continuar = input("\n¿Desea registrar más vehículos? (s/n): ")