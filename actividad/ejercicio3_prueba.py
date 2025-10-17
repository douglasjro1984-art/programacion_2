class Empleado:
    def __init__(self,nombre, id_empleado):
        self.nombre=nombre
        self.id_empleado=id_empleado
        
    def calcular_pago(self):
        print("Error: El metodo de pagp debe ser implementado por {self.nombre}.")
        return 0 
 
class EmpleadoTiempoCompleto:
    def __init__(self,nombre, id_empleado,salario_mensual):
            self.nombre=nombre
            self.id_empleado=id_empleado
            self.salario_mensual=salario_mensual
            
    def calcular_pago(self):
        return  self.salario_mensual
    
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, id_empleado, tarifa_por_hora,horas_trabajadas):
         super().__init__(nombre, id_empleado)
         self.tarifa_por_hora = tarifa_por_hora
         self.horas_trabjadas = horas_trabajadas
         
    def calcular_pago(self):
         return self.tarifa_por_hora * self.horas_trabjadas
         
    # Crear instancias de cada tipo de empleado
empleado_fijo = EmpleadoTiempoCompleto("Ana Pérez", 101, 350000) # Salario: $350,000
empleado_por_hora = EmpleadoPorHora("Luis Gómez", 202, 2500, 160) # Pago: 2500 * 160 = $400,000

# Crear una lista para aplicar el Polimorfismo
nomina = [empleado_fijo, empleado_por_hora]

# Recorrer la lista y calcular el pago de cada uno
print("--- Cálculo de Nómina ---")
for empleado in nomina:
    pago = empleado.calcular_pago()
    print(f"Empleado ID {empleado.id_empleado} ({empleado.nombre}): ${pago:,.2f}")    
          
            

        
     