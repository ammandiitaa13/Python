import tkinter as tk
import random
import string

# Función para generar una contraseña aleatoria
def generar_contrasena():
    longitud = int(entrada_longitud.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = "".join(random.choices(caracteres, k=longitud))
    while (not any(c.islower() for c in contrasena) or
           not any(c.isupper() for c in contrasena) or
           not any(c.isdigit() for c in contrasena) or
           not any(c in string.punctuation for c in contrasena)):
        contrasena = "".join(random.choices(caracteres, k=longitud))
    etiqueta_contrasena.config(text=f"Contraseña: {contrasena}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("300x200")
ventana.configure(bg="#E6E6FA")

# Etiqueta y campo de entrada para la longitud de la contraseña
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:", bg="#E6E6FA", fg="black")
etiqueta_longitud.pack(pady=10)
entrada_longitud = tk.Entry(ventana, bg="white", fg="black", bd=2, relief="solid")
entrada_longitud.pack(pady=5)

# Botón para generar la contraseña
estilo_boton = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
boton_generar = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena, **estilo_boton)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
etiqueta_contrasena = tk.Label(ventana, text="Contraseña: ", bg="#E6E6FA", fg="black")
etiqueta_contrasena.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()