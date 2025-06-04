import tkinter as tk
from View.Productos_view import *

def ventana_usuario(datos):
    ventana_User = tk.Tk()
    ventana_User.title("Ventana Usuario")
    ventana_User.geometry("1800x1000")
    cargar_producto(ventana_User)
    ventana_User.mainloop()
