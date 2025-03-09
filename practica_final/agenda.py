import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import re

def crear_tabla():
    """
    Crea la base de datos y la tabla contactos si no existe.
    """
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT, telefono TEXT, correo TEXT)''')
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

def agregar_contacto(nombre, telefono, correo):
    """
    Agrega un nuevo contacto a la base de datos.
    """
    if not telefono.isdigit():
        messagebox.showerror("Error", "El teléfono debe contener solo números.")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        messagebox.showerror("Error", "El correo debe ser válido y contener un '@' y un dominio.")
        return
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO contactos (nombre, telefono, correo) VALUES (?, ?, ?)",
                       (nombre, telefono, correo))
        conexion.commit()
        messagebox.showinfo("Información", "Contacto agregado con éxito.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al agregar el contacto: {e}")
    finally:
        conexion.close()
    interfaz_listar_contactos()

def listar_contactos():
    """
    Muestra la lista de contactos almacenados en la base de datos.
    """
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos")
        contactos = cursor.fetchall()
        return contactos
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al listar los contactos: {e}")
        return []
    finally:
        conexion.close()

def buscar_contacto(nombre):
    """
    Busca un contacto por su nombre.
    """
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        contacto = cursor.fetchall()
        return contacto
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al buscar el contacto: {e}")
        return []
    finally:
        conexion.close()

def eliminar_contacto(nombre):
    """
    Elimina un contacto por su nombre.
    """
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM contactos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        conexion.commit()
        messagebox.showinfo("Información", "Contacto eliminado con éxito.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar el contacto: {e}")
    finally:
        conexion.close()
    interfaz_listar_contactos()

def actualizar_contacto(nombre, nuevo_telefono, nuevo_correo):
    """
    Actualiza el teléfono y correo de un contacto existente.
    """
    if not nuevo_telefono.isdigit():
        messagebox.showerror("Error", "El teléfono debe contener solo números.")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", nuevo_correo):
        messagebox.showerror("Error", "El correo debe ser válido y contener un '@' y un dominio.")
        return
    try:
        conexion = sqlite3.connect("agenda.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE contactos SET telefono = ?, correo = ? WHERE nombre LIKE ?",
                       (nuevo_telefono, nuevo_correo, '%' + nombre + '%'))
        conexion.commit()
        messagebox.showinfo("Información", "Contacto actualizado con éxito.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar el contacto: {e}")
    finally:
        conexion.close()
    interfaz_listar_contactos()

def exportar_contactos_csv():
    """
    Exporta los contactos a un archivo CSV.
    """
    try:
        contactos = listar_contactos()
        with open("contactos.csv", "w", newline='', encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["ID", "Nombre", "Teléfono", "Correo"])
            escritor.writerows(contactos)
        messagebox.showinfo("Información", "Contactos exportados a contactos.csv")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar los contactos: {e}")

def interfaz_agregar_contacto():
    nombre = simpledialog.askstring("Agregar Contacto", "Nombre:")
    telefono = simpledialog.askstring("Agregar Contacto", "Teléfono:")
    correo = simpledialog.askstring("Agregar Contacto", "Correo:")
    if nombre and telefono and correo:
        agregar_contacto(nombre, telefono, correo)

def interfaz_actualizar_contacto():
    nombre = lista.get(tk.ACTIVE).split(" - ")[0]
    nuevo_telefono = simpledialog.askstring("Actualizar Contacto", "Nuevo Teléfono:")
    nuevo_correo = simpledialog.askstring("Actualizar Contacto", "Nuevo Correo:")
    if nombre and nuevo_telefono and nuevo_correo:
        actualizar_contacto(nombre, nuevo_telefono, nuevo_correo)

def interfaz_eliminar_contacto():
    nombre = lista.get(tk.ACTIVE).split(" - ")[0]
    if nombre:
        eliminar_contacto(nombre)

def interfaz_listar_contactos():
    contactos = listar_contactos()
    lista.delete(0, tk.END)
    if contactos:
        for contacto in contactos:
            lista.insert(tk.END, f"{contacto[1]} - {contacto[2]} - {contacto[3]}")
    else:
        lista.insert(tk.END, "No hay contactos guardados.")

def interfaz_buscar_contacto():
    nombre = entrada_busqueda.get()
    if nombre:
        contactos = buscar_contacto(nombre)
        lista.delete(0, tk.END)
        if contactos:
            for contacto in contactos:
                lista.insert(tk.END, f"{contacto[1]} - {contacto[2]} - {contacto[3]}")
        else:
            lista.insert(tk.END, "No se encontraron contactos.")
    else:
        interfaz_listar_contactos()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("500x500")
ventana.configure(bg="#E6E6FA")

# Estilo de los botones
estilo_boton = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
estilo_boton_buscar = {"font": ("Arial", 12), "bg": "#2196F3", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
estilo_boton_agregar = {"font": ("Arial", 12), "bg": "#FF9800", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
estilo_boton_actualizar = {"font": ("Arial", 12), "bg": "#8BC34A", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
estilo_boton_eliminar = {"font": ("Arial", 12), "bg": "#F44336", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}
estilo_boton_exportar = {"font": ("Arial", 12), "bg": "#9C27B0", "fg": "white", "padx": 10, "pady": 5, "bd": 2, "relief": "raised"}

# Barra de búsqueda
frame_busqueda = tk.Frame(ventana, bg="#E6E6FA")
frame_busqueda.pack(pady=10)
entrada_busqueda = tk.Entry(frame_busqueda, bg="white", fg="black", bd=2, relief="solid", font=("Arial", 12))
entrada_busqueda.pack(side=tk.LEFT, padx=5)
boton_buscar = tk.Button(frame_busqueda, text="🔍", command=interfaz_buscar_contacto, **estilo_boton_buscar)
boton_buscar.pack(side=tk.LEFT)
boton_agregar = tk.Button(frame_busqueda, text="+", command=interfaz_agregar_contacto, **estilo_boton_agregar)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar los contactos
lista = tk.Listbox(ventana, bg="white", fg="black", bd=2, relief="solid", font=("Arial", 12))
lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Botones de actualizar, eliminar y exportar contacto
frame_botones = tk.Frame(ventana, bg="#E6E6FA")
frame_botones.pack(pady=10)
boton_actualizar = tk.Button(frame_botones, text="Actualizar Contacto", command=interfaz_actualizar_contacto, **estilo_boton_actualizar)
boton_actualizar.pack(side=tk.LEFT, padx=5)
boton_eliminar = tk.Button(frame_botones, text="Eliminar Contacto", command=interfaz_eliminar_contacto, **estilo_boton_eliminar)
boton_eliminar.pack(side=tk.LEFT, padx=5)
boton_exportar = tk.Button(frame_botones, text="Exportar a CSV", command=exportar_contactos_csv, **estilo_boton_exportar)
boton_exportar.pack(side=tk.LEFT, padx=5)

# Deshabilitar botones de actualizar y eliminar si no hay selección
def actualizar_estado_botones(event):
    seleccion = lista.curselection()
    if seleccion:
        boton_actualizar.config(state=tk.NORMAL)
        boton_eliminar.config(state=tk.NORMAL)
    else:
        boton_actualizar.config(state=tk.DISABLED)
        boton_eliminar.config(state=tk.DISABLED)

lista.bind("<<ListboxSelect>>", actualizar_estado_botones)
boton_actualizar.config(state=tk.DISABLED)
boton_eliminar.config(state=tk.DISABLED)

# Ejecutar la aplicación
ventana.mainloop()

# Crear la tabla al iniciar la aplicación
crear_tabla()
interfaz_listar_contactos()