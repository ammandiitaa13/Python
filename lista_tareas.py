import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = entrada_tarea.get().strip()  # Eliminar espacios en blanco innecesarios
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar una tarea.")

# Función para guardar las tareas en un archivo de texto
def guardar_tareas():
    tareas = lista_tareas.get(0, tk.END)
    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")
    messagebox.showinfo("Información", "Las tareas han sido guardadas en tareas.txt")

# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]  # Obtener el índice seleccionado
        lista_tareas.delete(indice)  # Eliminar de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Debe seleccionar una tarea para eliminar.")

# Función para cargar tareas desde el archivo al iniciar
def cargar_tareas():
    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                lista_tareas.insert(tk.END, linea.strip())  # Agregar sin espacios extra
    except FileNotFoundError:
        pass  # Si el archivo no existe, simplemente no se cargan tareas

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x600")
ventana.configure(bg="#E6E6FA")

# Etiqueta y campo de entrada para una nueva tarea
etiqueta_tarea = tk.Label(ventana, text="Nueva Tarea:", bg="#E6E6FA", fg="black")
etiqueta_tarea.pack(pady=10)
entrada_tarea = tk.Entry(ventana, bg="white", fg="black", bd=2, relief="solid")
entrada_tarea.pack(pady=5)

# Botón para agregar la tarea a la lista
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea, bg="#4CAF50", fg="white", padx=10, pady=5, bd=2, relief="raised")
boton_agregar.pack(pady=10)

# Listbox para mostrar las tareas actuales
lista_tareas = tk.Listbox(ventana, bg="white", fg="black", bd=2, relief="solid")
lista_tareas.pack(pady=10, fill=tk.BOTH, expand=True)

# Botón para eliminar tarea seleccionada
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea, bg="#FF5733", fg="white", padx=10, pady=5, bd=2, relief="raised")
boton_eliminar.pack(pady=5)

# Botón para guardar las tareas en un archivo de texto
boton_guardar = tk.Button(ventana, text="Guardar Tareas", command=guardar_tareas, bg="#4CAF50", fg="white", padx=10, pady=5, bd=2, relief="raised")
boton_guardar.pack(pady=10)

# Cargar tareas al iniciar
cargar_tareas()

# Ejecutar la aplicación
ventana.mainloop()
