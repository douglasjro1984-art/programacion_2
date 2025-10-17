# ESTRRUCTURA DE DATOS la lista es una
# colección ordenada debobjeto de distintos 
# tipos equibalente en otro lenguajes arrays o vevtores 
# pueden contener cualquier tipo de dato:
# numeros ,cadenas booleanos y tambien listas

lista = [1,2,3,5,7,8]
print(lista)

# mostrar un elemento segun su indice
print(lista[2]) # primer elemento
print(lista[4]) # cuarto elemento
print(lista[1:3]) # [indice_inicial: indice_final] sin mos
 

# para saber el tamaño  de la lista
print ("para saber el tamaño  de la lista es ", len(lista))

#sublistas = slicing en lista
sublista = lista[1:3] # del indice 1 al 3
print(sublista)

# en listas podemos agregar,
# modificar y eliminar elementos
# agregar = appen(valor) agregar el elemnto al 
# final

lista.append(6)
lista.append(10)
print(lista)

# insertar elementos en una posicion
# insert(indiceconcreto)

lista.insert(4,15,)
lista.append(20)
print(lista)

# eliminar elemento e la lista remove (posición)

lista.remove(15)
print(lista)

#para saber si un elemento existe en la lista
# in devuelve verdadero(True) o falso (False)
print(8 in lista)
print(15 in lista)
print(30 in lista)

#recorrer una lista: bucle for o while
#el mas sencillo es for

for i in lista:
    print(f"Los elementos de la lista son: {i}" )

# recorrer la lista con while
asistencia_29 = ["Douglas", "Francisco","Santiago",
           "Emmanuel", "Fernando", "Alvaro",
           "Rodrigo","Federico","Roberto","Agustin",
           "Sofia", "Tamara","Celeste","Ana"]
i=0
while (i<len(asistencia_29)):
    print(f"El alumno: {asistencia_29[i]} estuvo presente en la \nclase de Programacion II el dia 29/08/2025 ")
    i += 1