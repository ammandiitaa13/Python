import tkinter as tk
import math

# Funciones de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    else:
        return a / b

def potencia(a, b):
    return math.pow(a, b)

def raiz(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    else:
        return math.sqrt(a)

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    else:
        return a % b

def porcentaje(a, b):
    return a * b / 100

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.configure(bg="#E6E6FA")  # Fondo en tono lavanda claro

# Estilo de los widgets
estilo_boton = {"font": ("Arial", 14), "bg": "#9370DB", "fg": "white", "padx": 20, "pady": 20, "bd": 0, "relief": "flat"}  # Botones en tono púrpura medio
estilo_entrada = {"font": ("Arial", 18), "bg": "#D8BFD8", "fg": "#000000", "bd": 2, "relief": "solid"}  # Entrada en tono thistle
estilo_etiqueta = {"font": ("Arial", 14), "bg": "#E6E6FA", "fg": "#000000"}  # Etiquetas en tono lavanda claro

# Etiquetas y campos de entrada
etiqueta_num1 = tk.Label(ventana, text="Número 1:", **estilo_etiqueta)
etiqueta_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada1 = tk.Entry(ventana, **estilo_entrada)
entrada1.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

etiqueta_num2 = tk.Label(ventana, text="Número 2:", **estilo_etiqueta)
etiqueta_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada2 = tk.Entry(ventana, **estilo_entrada)
entrada2.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", **estilo_etiqueta)
etiqueta_resultado.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Funciones para vincular la lógica con la interfaz
def calcular_suma():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = sumar(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_resta():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = restar(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_multiplicacion():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = multiplicar(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_division():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = dividir(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_modulo():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = modulo(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_potencia():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = potencia(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_raiz():
    try:
        num1 = float(entrada1.get())
        resultado = raiz(num1)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

def calcular_porcentaje():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = porcentaje(num1, num2)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

# Botones para las operaciones con diseño de cuadrícula
boton_suma = tk.Button(ventana, text="Sumar", command=calcular_suma, **estilo_boton)
boton_suma.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

boton_resta = tk.Button(ventana, text="Restar", command=calcular_resta, **estilo_boton)
boton_resta.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

boton_multiplicacion = tk.Button(ventana, text="Multiplicar", command=calcular_multiplicacion, **estilo_boton)
boton_multiplicacion.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

boton_division = tk.Button(ventana, text="Dividir", command=calcular_division, **estilo_boton)
boton_division.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

boton_modulo = tk.Button(ventana, text="Módulo", command=calcular_modulo, **estilo_boton)
boton_modulo.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

boton_potencia = tk.Button(ventana, text="Potencia", command=calcular_potencia, **estilo_boton)
boton_potencia.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

boton_raiz = tk.Button(ventana, text="Raíz", command=calcular_raiz, **estilo_boton)
boton_raiz.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

boton_porcentaje = tk.Button(ventana, text="Porcentaje", command=calcular_porcentaje, **estilo_boton)
boton_porcentaje.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

# Hacer que los botones se estiren correctamente
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_rowconfigure(4, weight=1)
ventana.grid_rowconfigure(5, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

# Ejecutar la aplicación
ventana.mainloop()
