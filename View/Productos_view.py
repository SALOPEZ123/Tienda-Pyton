import tkinter as tk

def cargar_producto(ventana):
    Producto_panel = tk.Frame(
        ventana,
        bg="green",
        padx=0,pady=0,
        width=1000,
        height=400)
    Producto_panel.pack()
    print("panel productos cargados")