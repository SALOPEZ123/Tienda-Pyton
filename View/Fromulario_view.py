import tkinter as tk
from tkinter import ttk
from Services.mi_sql import conectar

def crear_panel_lateral(parent,actualizar_productos):
    panel_izquierdo = ttk.LabelFrame(
        parent,
        text="Panel Lateral",
        padding=(15, 10)
    )
    panel_izquierdo.pack(side="left", fill="y", padx=10, pady=10)

    ttk.Label(panel_izquierdo, text="Registrar Producto").pack(anchor="w")
    def producto_new():
        txt_Producto = ttk.Label(panel_izquierdo, text="Ingrese Producto")
        txt_Producto.pack()
    def precio_new():
        txt_precio = ttk.Label(panel_izquierdo, text="Ingrese Precio")
        txt_precio.pack()
    def cantidad_new():
        txt_cantidad = ttk.Label(panel_izquierdo, text="Ingrese cantidad")
        txt_cantidad.pack()
    def categoria_new():
        txt_categoria = ttk.Label(panel_izquierdo, text="Ingrese categoria")
        txt_categoria.pack()
    
    producto_new()
    entry_nombre = tk.Entry(panel_izquierdo)
    entry_nombre.pack(pady=5)

    precio_new()
    entry_precio = tk.Entry(panel_izquierdo)
    entry_precio.pack(pady=5)

    cantidad_new()
    entry_cantidad = tk.Entry(panel_izquierdo)
    entry_cantidad.pack(pady=5)

    categoria_new()
    entry_categoria = tk.Entry(panel_izquierdo)
    entry_categoria.pack(pady=5)

    def btm_agregar_productos():
        nombre = entry_nombre.get().strip()
        precio = entry_precio.get().strip()
        cantidad = entry_cantidad.get().strip()
        categoria = entry_categoria.get().strip()
        try:
            consulta = "INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s, %s, %s, %s)"
            conectar(consulta, (nombre, float(precio), int(cantidad), int(categoria)))
            actualizar_productos()
        except Exception as e:
            print("no se pudo XD")
            
    btm_insertar = tk.Button(panel_izquierdo, text="Insertar",command=btm_agregar_productos)
    btm_insertar.pack(pady=10)

    return panel_izquierdo