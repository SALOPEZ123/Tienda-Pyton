import tkinter as tk
from Services.mi_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(ventana,
    bg="blue",
    padx=0,
    pady=0,
    width=1000,
    height=600,
    )

    titulo = tk.Label(login_panel, text="login")
    titulo.pack()
    txt_correo = tk.Label(login_panel, text="Correo")
    txt_correo.pack()

    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

    txt_Contraseña = tk.Label(login_panel, text="Contraseña")
    txt_Contraseña.pack()

    entrada_contraseña = tk.Entry(login_panel)
    entrada_contraseña.pack()

    def btm_continuar():    
        Et_Corro = entrada_correo.get()
        Et_Contr = entrada_contraseña.get()

        print(conectar("SHOW TABLES"))


    boton = tk.Button(login_panel, text="Continuar",command=btm_continuar)
    boton.pack()


    login_panel.pack()
    print("panel login cargado")
