from tkinter import Toplevel, Label

def def_attack1(main_screen):
    messageWindow = Toplevel(main_screen)
    messageWindow.title("Defensa de ataque 1")
    messageWindow.geometry("860x560")
    Label(messageWindow, text="Esta es la defensa del ataque 1").pack()
    main_screen.withdraw()

    def on_closing():
        messageWindow.destroy()
        main_screen.deiconify()
    messageWindow.protocol("WM_DELETE_WINDOW", on_closing)