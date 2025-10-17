#III. Ejercicio Práctico de Implementación (3 puntos)
#Implementa una clase 
#Estudiante que cumpla con los siguientes requisitos, basándote en el ejemplo integrador:
# 1.	Debe tener un constructor (__init__) que reciba e inicialice el atributo nombre.
# 2.	Debe tener un atributo de lista llamado materias_aprobadas inicializado como lista vacía ([]).
# 3.	Debe tener un método llamado aprobar_materia(self, materia) que reciba el nombre de una materia y la agregue a la lista materias_aprobadas10.
# 4.	Crea una instancia llamada alumno con el nombre que desees.
#5.	Usa el método aprobar_materia para agregar dos materias: "Programación II" y "Matemática".



class Estudiante:
    def __init__(self,nombre):#Constructor y Atributo materias aprobadas
        self.nombre=nombre
        self.materias_aprobadas=[]#inicializamos como lista vacia
    
    #Metodo aprobar materia    
    def aprobar_materia(self,materia):
        self.materias_aprobadas.append(materia)
        
    #Creacion de instacia
    
alumno=Estudiante("Douglas Romero")
    
# Uso del metodo
    
alumno.aprobar_materia("Programacion II, Matematicas")

print(f"El alumno,{alumno.nombre},aprobo{alumno.materias_aprobadas}")
    
#(verificacion Opcional): print(alumno.materias_aprobadas)
        
        
        