from View.Productos_view import crear_panel_productos
from View.Fromulario_view import crear_panel_lateral
import tkinter as tk

def ventana_usuario(datos):
    ventana_User = tk.Tk()
    ventana_User.title("Ventana Usuario")
    ventana_User.geometry("1800x1000")
    frame_productos = tk.Frame(ventana_User)
    frame_productos.pack(side="left", fill="both", expand=True)

    panel_productos = crear_panel_productos(frame_productos)
    ventana_User.state('zoomed')
    def actualizar_productos():
        nonlocal panel_productos
        panel_productos.destroy()
        panel_productos = crear_panel_productos(frame_productos)

    crear_panel_lateral(ventana_User, actualizar_productos)

    ventana_User.mainloop()
