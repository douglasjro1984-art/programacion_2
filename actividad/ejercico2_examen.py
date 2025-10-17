#Ejercicio de POO: Gestión de Libros y Biblioteca
#Douglas Romero 
#Celeste Cruz 


#Crear objetos Libros

class MaterialBiblioteca:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        self.disponible= True
        
    def mostrar_info(self):
        estado="disponible" if self.disponible else "Prestado"
        print(f"Libro: {self.titulo} - autor: {self.autor}- Estado: {estado}")
        return self.disponible
        

class libro(MaterialBiblioteca):
    def __init__(self,titulo,autor,adulto,):
        super().__init__(titulo,autor)
        self.adulto = adulto
      
         
class Revista (MaterialBiblioteca):
    def __init__(self,titulo,autor,adulto,):
        super().__init__(titulo,autor)
        self.adulto = adulto
         
        
class Biblioteca:
    def __init__(self, nombre):
        self.nombre=nombre
        self.catalogo=[]#Lista para guardar objetos libros
        
    def agregar_libro(self,libro):
        self.catalogo.append(libro)
        print(f"'{libro.titulo}' agregado a la {self.nombre}.")
        
    def prestar_libro(self, titulo_libro):
        for libro in self.catalogo:
            if libro.titulo==titulo_libro:
                if libro.disponible:
                    libro.disponible = False
                    print(f"Libro '{ titulo_libro}' prestado con exito.")
                    return
                else:
                    print(f"Libro'{titulo_libro}' ya esta prestado.")
                    
        print(f"Error: Libro '{titulo_libro}' no encontrado en el catalogo.")
                    
        
# Crear la biblioteca
mi_biblioteca = Biblioteca("Biblioteca UTN")
l1 = libro("Cien años de soledad", "Gabriel García Márquez","adulto")
mi_biblioteca.agregar_libro(l1)
l2 = libro("El señor de los anillos", "J.R.R. Tolkien","adulto")
mi_biblioteca.agregar_libro(l2)
l3 = libro("El Quijote", "Miguel de Cervantes","Adulto")
mi_biblioteca.agregar_libro(l3)

print("\n=== AGREGAR NUEVO LIBRO ===")
titulo_nuevo=input("Ingrese el titulo que desea agregar: ")
autor_nuevo=input("Ingrese el autor que desea agregar: ")

nuevo_libro=libro(titulo_nuevo,autor_nuevo)

print("\n=== SOLICITAR PRÉSTAMO ===")
titulo_prestamo = input("¿Qué libro desea solicitar en préstamo? (Ingrese el título exacto): ")
mi_biblioteca.prestar_libro(titulo_prestamo)

if titulo_prestamo == nuevo_libro.titulo:
    nuevo_libro.mostrar_info()
    
    
    