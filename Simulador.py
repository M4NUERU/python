 #print("Movimiento Rectilineo Uniforme")
#d=float(input("Ingrese una DISTANCIA  "))
#t=float(input("Ingrese el TIEMPO  "))
#v=d/(t/60)


import tkinter as tk
from tkinter import simpledialog, messagebox

# Funciones específicas para cada opción
def opcion_1():
    print("Movimiento Rectilineo Uniforme")
    print("Calcular Velocidad")
    d = simpledialog.askfloat("Entrada", "Ingrese una DISTANCIA (en km): ")
    if d is None:
        return
    t = simpledialog.askfloat("Entrada", "Ingrese el TIEMPO (en minutos): ")
    if t is None:
        return
    if t == 0:
        messagebox.showerror("Error", "El tiempo no puede ser cero.")
        return
    v = d / (t / 60)
    print (v, "km/h")
def opcion_2():
    print("Movimiento Rectilineo Uniforme")
    print("Calcular Distancia")
    # Código específico para la opción 2
    v = simpledialog.askfloat("Entrada", "Ingrese una VELOCIDAD(en km/h): ")
    if v is None:
        return
    t = simpledialog.askfloat("Entrada", "Ingrese el TIEMPO (en minutos): ")
    if t is None:
        return
    if t == 0:
        messagebox.showerror("Error", "El tiempo no puede ser cero.")
        return
    d = v * (t / 60)
    print (d,"km")
    messagebox.showinfo("Opción 2", "Esta es la lógica de la opción 2.")

def opcion_3():
    print("Ejecutando la opción 3")
    # Código específico para la opción 3
    v = simpledialog.askfloat("Entrada", "Ingrese una VELOCIDAD(en km/h): ")
    if v is None:
        return
    d = simpledialog.askfloat("Entrada", "Ingrese la DISTANCIA (en km): ")
    if d is None:
        return
    if d == 0:
        messagebox.showerror("Error", "El tiempo no puede ser cero.")
        return
    t = d/v
    print (t,"h")
    messagebox.showinfo("Opción 3", "Esta es la lógica de la opción 3.")

# Diccionario simulando un switch
switch = {
    "Opción 1": opcion_1,
    "Opción 2": opcion_2,
    "Opción 3": opcion_3
}

# Función que se ejecuta cuando se presiona el botón
def mostrar_opcion_seleccionada():
    try:
        opcion = lista_opciones.get(lista_opciones.curselection())
    except tk.TclError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una opción de la lista.")
        return

    # Ejecutar la función correspondiente a la opción seleccionada
    funcion = switch.get(opcion, lambda: messagebox.showerror("Error", "Opción no válida"))
    funcion()

# Crear la ventana principal
root = tk.Tk()
root.title("Programa con Lista de Opciones")

# Crear una etiqueta
etiqueta = tk.Label(root, text="Selecciona una opción de la lista:")
etiqueta.pack(pady=10)

# Crear una lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Crear un widget Listbox
lista_opciones = tk.Listbox(root)
for opcion in opciones:
    lista_opciones.insert(tk.END, opcion)
lista_opciones.pack(pady=10)

# Crear un botón para mostrar la opción seleccionada
boton_mostrar = tk.Button(root, text="Mostrar Opción Seleccionada", command=mostrar_opcion_seleccionada)
boton_mostrar.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()

