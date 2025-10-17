#1) Elabora un algoritmo que permita averiguar si una persona puede tramitar su CUIL, 
# sabiendo su año de nacimiento. 
# El CUIL es el código único de identificación laboral que se otorga a todo trabajador
# al inicio de su actividad laboral en relación de dependencia (mayores de 17 años) que pertenezca 
# al Sistema Integrado de Jubilaciones y Pensiones y o toda persona que gestione alguna prestación 
# o servicio de Seguridad Social en la República Argentina.

print("-----TRAMITAR CUIL-----")
año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = 2025
edad = año_actual - año_de_nacimiento
inicio_actividad_laboral = 17
print(f"Su edad es: {edad} años")

if edad >= inicio_actividad_laboral:
    print("Usted puede tramitar su CUIL.")  
else:
    print("Usted no puede tramitar su CUIL, debe ser mayor de 17 años.")