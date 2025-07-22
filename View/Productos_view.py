import tkinter as tk
from tkinter import ttk
from Services.mi_sql import conectar

def crear_panel_productos(parent):
    contenedor = ttk.LabelFrame(
        parent,
        text="Catálogo de Productos",
        padding=(10, 10)
    )
    contenedor.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    try:
        resultados = conectar("SELECT nombre FROM productos;")  
    except Exception as e:
        ttk.Label(contenedor, text=f"Error al cargar productos: {e}", foreground="red").pack()
        return contenedor

    if not resultados:
        ttk.Label(contenedor, text="No hay productos disponibles.").pack(pady=10)
        return contenedor

    columnas = 3
    for index, fila in enumerate(resultados):
        nombre_producto = fila[0]
        row = index // columnas
        col = index % columnas

        producto_frame = ttk.Frame(contenedor, relief="ridge", padding=10)
        producto_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

        etiqueta = ttk.Label(producto_frame, text=nombre_producto, anchor="center", font=("Arial", 10, "bold"))
        etiqueta.pack()

    for col in range(columnas):
        contenedor.columnconfigure(col, weight=1)

    return contenedor

