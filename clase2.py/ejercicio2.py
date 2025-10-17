# crear un programa en python que permitagestionar una lista de nombres de estudiantes el progrma debe tener:
#1. iniciar con una lista vacia
#2. pedir al usuario que ingrese 5 nombres y agregarlos a la lista usando append()
#3. mostrar la lista completa
#4.ordenar la lista alfabeticamente usando sort()
#5.mostrar cuando los elementos tiene la lista usando len ()
#6. Permitir al usuario eliminar un nombre que elija de la lista usando remove().
#7. Mostrar la lista actualizada.
#8. Agregar un nombre en una posición específica usando insert().
#9. Mostrar el índice de un nombre específico usando index().
#10. Borrar el último nombre de la lista usando pop().
#11. Mostrar la lista final.


lista=[] #1 lista vacia
for i in range(5):
    nombre=input("Ingrese el nombre del estudiante: ")
    lista.append(nombre) #2 agregar nombres a la lista
print("La lista completa de estudiantes es: ", lista) #3mostrar la lista completa
lista.sort() #ordenar la lista alfabeticamente
print("La lista ordenada alfabeticamente es: ", lista) #4mostrar la lista ordenada
print("La cantidad de estudiantes en la lista es: ", len(lista)) #5mostrar la cantidad de elementos en la lista
nombre_eliminar=input("Ingrese el nombre que desea eliminar de la lista: ")
if nombre_eliminar in lista:
    lista.remove(nombre_eliminar) # 6 eliminar un nombre de la lista
    print("El nombre ha sido eliminado.")
print("La lista actualizada es: ", lista) #7 mostrar la lista actualizada
nombre_insertar=input("Ingrese el nombre que desea insertar en la lista: ")
posicion=int(input("Ingrese la posición (0 a {} ) donde desea insertar el nombre: ".format(len(lista))))
if 0 <= posicion <= len(lista):
    lista.insert(posicion, nombre_insertar) #8 insertar un nombre en una posición específica
    print("El nombre ha sido insertado.")
print("La lista actualizada es: ", lista) #mostrar la lista actualizada
nombre_buscar=input("Ingrese el nombre que desea buscar en la lista: ")
if nombre_buscar in lista:
    indice=lista.index(nombre_buscar) #9 mostrar el índice de un nombre específico
    print("El nombre {} se encuentra en la posición: {}".format(nombre_buscar, indice)) 
    nombre_borrar=lista.pop() #10 borrar el último nombre de la lista
    print("El último nombre {} ha sido eliminado de la lista.".format(nombre_borrar))
print("La lista final de estudiantes es: ", lista) #11 mostrar la lista final   

    
