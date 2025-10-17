#3) Elabora un algoritmo que sirva para identificar el tipo de triángulo conociendo sus tres lados.

print("-----TIPO DE TRIÁNGULO-----")
# Ingreso de datos
continuar="s" # Variable de control para el bucle
# Bucle para permitir múltiples cálculos
while continuar == "s":
    lado1 = float(input("Ingrese la medida del primer lado: ")) 
    lado2 = float(input("Ingrese la medida del segundo lado: "))
    lado3 = float(input("Ingrese la medida del tercer lado: "))
#tipo de triángulo
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
    
    continuar = input("¿Desea analizar otro triángulo? (s/n): ")
    
    # Finalización del programa
    print("-----PROGRAMA TERMINADO-----")
    
    