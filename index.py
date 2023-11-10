import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import paramiko
from tkterm import Terminal
from test import *
from atk3 import attack3
from atk2 import attack2
from atk1 import attack1
from def1 import def_attack1
from def2 import def_attack2
from def3 import def_attack3
#from pycomm.ab_comm import LogixDriver



#SSH conexion
#Colocar aqui las credenciales, ip de la maquina a conectar y el comando
user = ""
password = ""
ip=""
comm="ls"





def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_main_window_resize(event):
    frame.update_idletasks()
    canvas.itemconfig(frame_id, width=canvas.winfo_width(), height=canvas.winfo_height())

main_screen = tk.Tk()
main_screen.title("AbsAttack")
#main_screen.geometry ("860x560")
#permite pantalla fullscreen
main_screen.attributes('-fullscreen', True)
main_screen.bind("<Configure>", on_main_window_resize)

# URL de la imagen
URL = "https://img2.helpnetsecurity.com/posts2021/assetcentre-attack.jpg"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im.thumbnail((400, 400))  
photo = ImageTk.PhotoImage(im)

main_screen.iconphoto(True, photo)

main_screen.config(background="black")

# Crear una ventana con scroll
canvas = Canvas(main_screen, borderwidth=0, background="black")
vsb = Scrollbar(main_screen, orient="vertical", command=canvas.yview)
hsb = Scrollbar(main_screen, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
canvas.pack(side="left", fill="both", expand=True)
vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")

frame = Frame(canvas, background="black")
frame_id = canvas.create_window((4, 4), window=frame, anchor="nw")



canvas.bind("<Configure>", on_frame_configure)

# Columna de botones a la izquierda
def def_attack1_wrapper():
    def_attack1(main_screen)

defattack1 = tk.Button(frame, text="Defender ataque 1", bg="black", fg="white", command= def_attack1_wrapper)
defattack1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

def def_attack2_wrapper():
    def_attack2(main_screen)

defattack2 = tk.Button(frame, text="Defender ataque 2", bg="black", fg="white", command= def_attack2_wrapper)
defattack2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

def def_attack3_wrapper():
    def_attack3(main_screen)
defattack3 = tk.Button(frame, text="Defender ataque 3", bg="black", fg="white", command= def_attack3_wrapper)
defattack3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

reset = tk.Button(frame, text="reiniciar", bg="black", fg="white")
reset.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Espacio de imagen
image_label = Label(frame, image=photo, bg="black")
image_label.grid(row=0, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")



# Columna de botones a la derecha

def attack1_wrapper():
    attack1(main_screen, ip, user, password, comm)

atk1 = tk.Button(frame, text="Prueba de ataque 1", bg="black", fg="white", command=attack1_wrapper)
atk1.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

def attack2_wrapper():
    attack2(main_screen)

atk2 = tk.Button(frame, text="prueba de ataque 2", bg="black", fg="white", command=attack2_wrapper)
atk2.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

def attack3_wrapper():
    attack3(main_screen, user, password, ip)

atk3 = tk.Button(frame, text="prueba de ataque 3", bg="black", fg="white", command=attack3_wrapper)
atk3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

def done():
    main_screen.destroy()

dne = tk.Button(frame, text="Salir", bg="black", fg="white", command=done)
dne.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")



# resize automatico
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

main_screen.mainloop()