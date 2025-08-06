import tkinter as tk
from paneles.header_view import *
from paneles.Productos_view import *
from paneles.login_view import *



ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")

fr1 = cargar_login(ventana)

ventana.mainloop()