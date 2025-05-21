import tkinter as tk
from Services.mi_sql import conectar

def cargar_producto(ventana):
    Producto_panel = tk.Frame(
        ventana,
        bg="white",
        padx=0, pady=0,
        width=600,
        height=400
    )
    
    # Obtener productos
    resultados = conectar("SELECT nombre FROM productos;")

    # Crear etiquetas en un grid (3 columnas)
    columnas = 3
    for index, fila in enumerate(resultados):
        nombre_producto = fila[0]
        row = index // columnas
        col = index % columnas

        etiqueta = tk.Label(Producto_panel, text=nombre_producto, bg="white", padx=5, pady=5)
        etiqueta.grid(row=row, column=col, padx=10, pady=10)

    Producto_panel.pack()
    print("panel productos cargados")
