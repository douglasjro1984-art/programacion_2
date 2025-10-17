#Tema Lista:
# Problema 1: Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] # lista de asignaturas
print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print(asignatura)
    
#Problema 2: Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista

#for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}") 
    
#Problema 3: Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

# orden inverso - metodo  reverse() nombrelista.reverse()
# ordenar la lista - metodo sort() nombrelista.sort()

lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
lista.reverse()
print(lista)

        

    