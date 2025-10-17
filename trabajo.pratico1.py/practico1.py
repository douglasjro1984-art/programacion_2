from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre, dni, salario_base):
        self.__nombre = nombre
        self.__dni = dni
        self.__salario_base = salario_base

    def calcular_salario(self):
        pass

    def mostrar_info(self):
        salario = self.calcular_salario()
        print(f"Nombre: {self.__nombre}")
        print(f"DNI: {self.__dni}")
        print(f"Salario: {salario:.2f}")

# Clase EmpleadoAsalariado
class EmpleadoAsalariado(Empleado):
    def calcular_salario(self):
        bono = 0.10 * self._Empleado__salario_base
        return self._Empleado__salario_base + bono

# Clase EmpleadoPorHoras
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, dni, salario_base, horas_trabajadas, valor_por_hora):
        super().__init__(nombre, dni, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.valor_por_hora

# Función polimórfica
def imprimir_detalles(empleado):
    empleado.mostrar_info()

# Crear instancias y mostrar salarios
asalariado = EmpleadoAsalariado("Douglas Romero", "12345678A", 1500)
por_horas = EmpleadoPorHoras("Ana Martinez", "87654321B", 0, 160, 10)

# Mostrar detalles usando la función polimórfica
imprimir_detalles(asalariado)
imprimir_detalles(por_horas)