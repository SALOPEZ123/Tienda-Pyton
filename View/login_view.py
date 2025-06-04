import tkinter as tk
from Services.mi_sql import conectar
from View.dashboard import ventana_usuario

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
        consultar_usuario = conectar(f"SELECT * FROM usuario WHERE correo = '{Et_Corro}' AND contraseña = '{Et_Contr}'")
        if len(consultar_usuario) != 0:
            print("usuario activo")
            ventana.destroy()
            print(consultar_usuario[0][3])
            ventana_usuario(consultar_usuario)
        else:
            print("datos incorrectos")

    boton = tk.Button(login_panel, text="Continuar",command=btm_continuar)
    boton.pack()

    login_panel.pack()
    print("panel login cargado")
