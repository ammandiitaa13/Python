import tkinter as tk

# Diccionario de tasas de conversión respecto a USD
tasas = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.81,
    "JPY": 134.0,
    "AUD": 1.46,
    "CAD": 1.33
}

# Función para realizar la conversión
def convertir():
    monto = float(entrada_monto.get())
    moneda_origen = variable_origen.get()
    moneda_destino = variable_destino.get()
    tasa_origen = tasas[moneda_origen]
    tasa_destino = tasas[moneda_destino]
    monto_convertido = monto * (tasa_destino / tasa_origen)
    etiqueta_resultado.config(text=f"Resultado: {monto_convertido:.2f} {moneda_destino}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Monedas")
ventana.geometry("400x300")
ventana.configure(bg="#E6E6FA")

# Etiqueta y campo de entrada para el monto
etiqueta_monto = tk.Label(ventana, text="Monto a convertir:", bg="#E6E6FA", fg="black")
etiqueta_monto.pack(pady=10)
entrada_monto = tk.Entry(ventana, bg="white", fg="black", bd=2, relief="solid")
entrada_monto.pack(pady=5)

# Menús desplegables para seleccionar las monedas de origen y destino
monedas = list(tasas.keys())
variable_origen = tk.StringVar(ventana)
variable_origen.set(monedas[0])  # Valor por defecto
menu_origen = tk.OptionMenu(ventana, variable_origen, *monedas)
menu_origen.config(bg="white", fg="black", bd=2, relief="solid")
menu_origen.pack(pady=5)

variable_destino = tk.StringVar(ventana)
variable_destino.set(monedas[1])  # Valor por defecto
menu_destino = tk.OptionMenu(ventana, variable_destino, *monedas)
menu_destino.config(bg="white", fg="black", bd=2, relief="solid")
menu_destino.pack(pady=5)

# Botón para realizar la conversión
estilo_boton = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir, **estilo_boton)
boton_convertir.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", bg="#E6E6FA", fg="black")
etiqueta_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()