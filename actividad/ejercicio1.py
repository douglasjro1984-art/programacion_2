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
# 1 cantidad de alumnos
cantidad_alumnos = int(input("¿Cuántos alumnos se van a registrar? "))

# punto 3 calcular promedio
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
# 2 para cada alumno
# programa principal
i = 1

while i <= cantidad_alumnos:
    print(f"\nRegistro del alumno {i}:")
    nombre = input("Ingresa el Nombre del alumno: ")
    apellido = input("Ingresa el Apellido del alumno: ")  
    curso = input("Ingresa el Curso: ")
    materia = input("Ingresa la Materia: ")
    nota1 = float(input("Nota 1 (0-10): "))
    nota2 = float(input("Nota 2 (0-10): "))
    nota3 = float(input("Nota 3 (0-10): "))
    promedio = calcular_promedio(nota1, nota2, nota3)
    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Resaprobado"
   
    print("\n Datos del alumno:")
    print(f"Nombre y Apellido: {nombre} {apellido}")
    print(f"Curso y Materia: {curso} - {materia}")  
    print(f" El Promedio de {nota1} {nota2} {nota3} es  {promedio: .2f}")
    print(f"Estado: {estado}")
    i += 1

