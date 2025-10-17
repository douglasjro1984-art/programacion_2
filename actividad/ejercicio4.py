# Elabora un algoritmo que solicite la edad de 2 hermanos y muestre un mensaje indicando la edad del mayor 
# y cuántos años de diferencia tiene con el menor

print("-----EDAD DE HERMANOS-----")
edad_hermano1 = int(input("Ingrese la edad del primer hermano: "))
edad_hermano2 = int(input("Ingrese la edad del segundo hermano: "))
if edad_hermano1 > edad_hermano2:
    mayor = edad_hermano1
    menor = edad_hermano2
    diferencia = mayor - menor
    print(f"El hermano mayor tiene {mayor} años y la diferencia de edad es de {diferencia} años.")
elif edad_hermano2 > edad_hermano1:
    mayor = edad_hermano2
    menor = edad_hermano1
    diferencia = mayor - menor
    print(f"El hermano mayor tiene {mayor} años y la diferencia de edad es de {diferencia} años.")
else:
    print("Ambos hermanos tienen la misma edad.")   