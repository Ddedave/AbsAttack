import paramiko
from tkinter import TOP, Toplevel, Label, Button

def attack1(main_screen, ip, user, password, comm):
    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 1")
    #messageWindow.geometry("860x560")
    #permite pantalla fullscreen
    messageWindow.attributes('-fullscreen', True)
    messageWindow.config(background="#65707F")
    tit = Label(messageWindow, text="Este es el ataque de nivel 1", font="Helvetica 20 bold", bg="#65707F", fg="white")
    tit.pack(pady=50)
    sub = Label(messageWindow, text="Listado de directorio", font="Helvetica 20", bg="#65707F", fg="white")
    sub.pack(side=TOP)

    #Descomentar para agregar boton si no pasa ssh
    #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda: on_closing()).pack()
    btn_back.grid(row=0, column=1,padx=10, pady=10, sticky="nsew")


    #Conexion ssh
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    #Se ejecuta comando
    _stdin, _stdout,_stderr = client.exec_command("ls")
    #print(_stdout.read().decode())
    string = str(_stdout.read().decode())
    #print(type(string))
    t = Label(messageWindow, text=string, bg="#65707F", fg="white", font="Helvetica 12")
    t.pack(side=TOP)
    client.close()


###### Conexion a PLC
    """  with LogixDriver('192.168.1.1') as plc:
        plc.open()
        if plc.read_tag('Tag1'):
            print('Lectura exitosa')
        plc.close() """

    ###### Botones
    #Regresar a menu principal
    btn_back= Button(messageWindow, text="Regresar", font=12, height=4, width=30,bg="black", fg="white", command=lambda: main_screen.tkraise()).pack()
    btn_back.grid(row=0,column=1,padx=10, pady=10, sticky="nsew")
    
    main_screen.withdraw()

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)

    