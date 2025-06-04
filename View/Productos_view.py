import tkinter as tk
from tkinter import ttk
from Services.mi_sql import conectar

def cargar_producto(ventana):
    # Marco contenedor con borde y título
    contenedor = ttk.LabelFrame(
        ventana,
        text="Catálogo de Productos",
        padding=(20, 10)
    )
    contenedor.pack(padx=20, pady=20, fill="both", expand=True)

    # Intentar obtener productos
    try:
        resultados = conectar("SELECT nombre FROM productos;")
    except Exception as e:
        ttk.Label(contenedor, text=f"Error al cargar productos: {e}", foreground="red").pack()
        return

    if not resultados:
        ttk.Label(contenedor, text="No hay productos disponibles.").pack(pady=10)
        return

    # Grid de productos
    columnas = 3
    for index, fila in enumerate(resultados):
        nombre_producto = fila[0]
        row = index // columnas
        col = index % columnas

        # Cada producto en su propio frame
        producto_frame = ttk.Frame(contenedor, relief="ridge", padding=10)
        producto_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

        etiqueta = ttk.Label(producto_frame, text=nombre_producto, anchor="center", font=("Arial", 10, "bold"))
        etiqueta.pack()

    # Expansión proporcional de columnas
    for col in range(columnas):
        contenedor.columnconfigure(col, weight=1)

    print("Panel de productos cargado.")
