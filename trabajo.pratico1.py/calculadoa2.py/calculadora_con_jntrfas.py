# calculadora simple por terminal
# suma, resta, multiplicacion y division
import tkinter as tk
from tkinter import messagebox

# Definimos la clase Calculadora fuera de la clase principal de la GUI
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

class CalculadoraGui:
    def __init__(self, master):
        self.master = master
        master.title("Ejercicio 2 - Calculadora")

        # Ahora creamos una instancia correcta de la clase Calculadora
        self.calculadora = Calculadora()
        
        # Widgest de entrada
        self.label_num1 = tk.Label(master, text="Número 1:")
        self.label_num1.grid(row=0, column=0)
        self.entry_num1 = tk.Entry(master)
        self.entry_num1.grid(row=0, column=1)
        self.label_num2 = tk.Label(master, text="Número 2:")
        self.label_num2.grid(row=1, column=0)
        self.entry_num2 = tk.Entry(master)
        self.entry_num2.grid(row=1, column=1)
        
        # Botones de operaciones
        self.button_suma = tk.Button(master, text="+", command=lambda: self.ejecutar_operacion("suma"))
        self.button_suma.grid(row=2, column=0, padx=2, pady=2)
        self.button_resta = tk.Button(master, text="-", command=lambda: self.ejecutar_operacion("resta"))
        self.button_resta.grid(row=2, column=1, padx=2, pady=2)
        self.button_multiplicacion = tk.Button(master, text="*", command=lambda: self.ejecutar_operacion("multiplicacion"))
        self.button_multiplicacion.grid(row=3, column=0, padx=2, pady=2)
        self.button_division = tk.Button(master, text="/", command=lambda: self.ejecutar_operacion("division"))
        self.button_division.grid(row=3, column=1, padx=2, pady=2)
       
        # Etiqueta de resultado
        self.label_resultado = tk.Label(master, text="Resultado:")
        self.label_resultado.grid(row=4, column=0, columnspan=2)
    
    def ejecutar_operacion(self, operacion):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            
            if operacion == "suma":
                resultado = self.calculadora.sumar(num1, num2)
            elif operacion == "resta":
                resultado = self.calculadora.restar(num1, num2)
            elif operacion == "multiplicacion":
                resultado = self.calculadora.multiplicar(num1, num2)
            elif operacion == "division":
                resultado = self.calculadora.dividir(num1, num2)
            else:
                raise ValueError("Operación no válida")
            
            self.label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError as e:
            messagebox.showerror("Error", "Entrada no válida. Por favor, ingrese números.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")   

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()  
    root.geometry("300x200")
    calculadora_gui = CalculadoraGui(root)
    root.mainloop()
