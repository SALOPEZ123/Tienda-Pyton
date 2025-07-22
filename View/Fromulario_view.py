from tkinter import ttk, messagebox
import tkinter as tk
from Services.mi_sql import conectar

def crear_panel_lateral(parent, actualizar_productos_callback):
    panel_izquierdo = ttk.LabelFrame(
        parent,
        text="Panel Lateral",
        padding=(15, 10)
    )
    panel_izquierdo.pack(side="left", fill="y", padx=10, pady=10)

    ttk.Label(panel_izquierdo, text="Registrar Producto").pack(anchor="w")

    # Nombre
    ttk.Label(panel_izquierdo, text="Ingrese Producto").pack()
    entry_nombre = tk.Entry(panel_izquierdo)
    entry_nombre.pack(pady=5)

    # Precio
    ttk.Label(panel_izquierdo, text="Ingrese Precio").pack()
    entry_precio = tk.Entry(panel_izquierdo)
    entry_precio.pack(pady=5)

    # Cantidad
    ttk.Label(panel_izquierdo, text="Ingrese cantidad").pack()
    entry_cantidad = tk.Entry(panel_izquierdo)
    entry_cantidad.pack(pady=5)

    # Categoría (Combobox)
    ttk.Label(panel_izquierdo, text="Seleccione categoría").pack()

    # 🔄 Obtener categorías desde la BD
    categorias = conectar("SELECT id, nombre FROM categorias")
    if not categorias:
        categorias = []

    # Crear diccionario {nombre: id}
    dict_categorias = {nombre: cid for cid, nombre in categorias}
    lista_nombres = list(dict_categorias.keys())

    combobox_categoria = ttk.Combobox(panel_izquierdo, values=lista_nombres, state="readonly")
    combobox_categoria.pack(pady=5)

    # Función para agregar producto
    def btm_agregar_productos():
        nombre = entry_nombre.get().strip()
        precio = entry_precio.get().strip()
        cantidad = entry_cantidad.get().strip()
        categoria_nombre = combobox_categoria.get().strip()

        if not (nombre and precio and cantidad and categoria_nombre):
            messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio)
            cantidad = int(cantidad)
            categoria_id = dict_categorias[categoria_nombre]
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser numéricos.")
            return
        except KeyError:
            messagebox.showerror("Error", "Categoría inválida.")
            return

        try:
            query = "INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s, %s, %s, %s)"
            conectar(query, (nombre, precio, cantidad, categoria_id))
            messagebox.showinfo("Éxito", "Producto insertado correctamente.")

            # Limpiar campos
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            combobox_categoria.set("")

            # Refrescar productos
            actualizar_productos_callback()

        except Exception as e:
            messagebox.showerror("Error al insertar", str(e))

    tk.Button(panel_izquierdo, text="Insertar", command=btm_agregar_productos).pack(pady=10)

    ttk.Label(panel_izquierdo, text="Filtro").pack

    entry_producto = tk.Entry(panel_izquierdo)
    entry_producto.pack()
    
    def btm_buscar_producto():
        producto = entry_producto.get().strip()
        consulta_buscar = conectar(f"SELECT * FROM productos WHERE nombre = '{producto}'")
        try:
            consulta_buscar = ttk.Frame(panel_izquierdo,relief="ridge", padding=10)

        except:
            print("Producto no encontrado")


    tk.Button(panel_izquierdo,text="Buscar",command=btm_buscar_producto).pack(pady=10)



    return panel_izquierdo