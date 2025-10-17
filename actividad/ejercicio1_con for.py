#Escribe un programa en Python que permita registrar y evaluar las calificaciones de varios alumnos.
#1. El programa debe preguntar cuántos alumnos se van a registrar (for o while). 
# 2.Para cada alumno, debe solicitar su nombre, apellido, curso, materia y tres notas (valores entre 0 y 10).
#3. Calcular el promedio de cada alumno usando una función.
#4. Usar una estructura condicional (if) para determinar si el alumno aprueba o reprueba (nota mínima para aprobar: 6).
#5. Al final, mostrar un resumen con:
#o El nombre y apellido del alumno
#o Curso, materia y su promedio
#o Su estado: "Aprobado" o "Reprobado"
#6. Repetir este proceso usando un bucle hasta que se hayan ingresado todos los alumnos.


print("-----EVALUAR CALIFICACIONES-----")
cantidad_alumnos=input("¿Cuántos alumnos se van a registrar? ")#preguntar cuántos alumnos se van a registrar

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# registrar los datos de cada alumno 6  
for i in range(cantidad_alumnos):
    print(f"\nRegistrando alumno {i + 1},{cantidad_alumnos}") 
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = (input("Ingrese la apellido del alumno: "))
    curso = input("Ingrese el curso del alumno: ")
    materia = input("Ingrese la materia del alumno: ")
    # Solicitar las tres notas del alumno
    nota1 = float(input("Ingrese la primera nota (0-10): ")) 
    nota2 = float(input("Ingrese la segunda nota (0-10): "))
    nota3 = float(input("Ingrese la tercera nota (0-10): "))       
    promedio = calcular_promedio(nota1, nota2, nota3)
    
    # Determinar si el alumno aprueba o reprueba /Con una estructura condicional (if)
    if promedio >= 6:
        estado = "Aprobado"  
    else:
        estado = "Reprobado"   
    # Mostrar el resultado final
    print (f"El Alumno {nombre}, {apellido}")
    print (f"del Curso {curso}")
    print  (" de la materia {materia} es: {promedio:.2f}")



