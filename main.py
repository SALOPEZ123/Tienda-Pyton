import tkinter as tk
from View.header_view import *
from View.Productos_view import *
from View.login_view import *



ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")

fr1 = cargar_login(ventana)

ventana.mainloop()