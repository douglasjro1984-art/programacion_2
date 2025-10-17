#4) Elabora un algoritmo que permita ingresar un número entero ( 1 al 10) 
# y muestre su equivalente en Romano.

print("-----NÚMERO ENTERO A ROMANO-----")
# Números romanos del 1 al 10
numeros_romanos = {1: "I",2: "II",3: "III", 4: "IV",5: "V",6: "VI",7: "VII",8: "VIII",9: "IX",10: "X"}   
contiuar = "s"# Variable de control para el bucle
# Bucle para permitir múltiples conversiones
while contiuar =="s":
    numero = int(input("Ingrese un número entero del 1 al 10: "))
    if 1 <=10:
        print(f"El número {numero} en romano es: {numeros_romanos[numero]}")
    else:
        print("Número fuera de rango. Intente nuevamente.")
    contiuar = input("¿Quieres continuar? (s/n): ")
    
    # Finalización del programa
    print("-----PROGRAMA TERMINADO-----")
    
    