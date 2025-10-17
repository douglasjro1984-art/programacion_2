#5) Dado el precio de un producto indicar, por pantalla, los impuestos que debe pagar.
# IVA 21%, ingresos brutos 2.5% e impuesto municipal 1.5%

print("-----CÁLCULO DE IMPUESTOS-----")
# Ingreso de datos
continuar ="s"# Variable de control para el bucle    
# Bucle para permitir múltiples cálculos
while continuar == "s":
    precio_producto = float(input("Ingrese el precio del producto: $"))
    if precio_producto < 0:
        print("El precio no puede ser negativo. Intente nuevamente.")
        precio_producto = float(input("Ingrese el precio del producto: $")) 
        continue
    # Cálculo de impuestos
    iva = precio_producto * 0.21
    ingresos_brutos = precio_producto * 0.025
    impuesto_municipal = precio_producto * 0.015
    total_impuestos = iva + ingresos_brutos + impuesto_municipal
    
    # Muestra los resultados
    print(f"IVA (21%): ${iva:.2f}")
    print(f"Ingresos Brutos (2.5%): ${ingresos_brutos:.2f}")
    print(f"Impuesto Municipal (1.5%): ${impuesto_municipal:.2f}")
    print(f"Total de impuestos a pagar: ${total_impuestos:.2f}")    
    print(f"Precio total del producto con impuestos: ${precio_producto + total_impuestos:.2f}")
    continuar = input("¿Desea calcular los impuestos para otro producto? (s/n): ")

# Finalización del programa
print("-----GRACIAS POR SU COMPRA-----")