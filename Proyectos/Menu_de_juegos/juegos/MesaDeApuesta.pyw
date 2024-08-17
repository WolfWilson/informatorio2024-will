import random
from tkinter import *
from tkinter import messagebox, simpledialog

# VENTANA PRINCIPAL
root = Tk()
root.title("Mesa de Apuestas")
root.geometry("700x350")
root.resizable(False,False)

saldo = IntVar(value=1000)
numero_seleccionado = IntVar(value=-1)

# FUNCION PARA RESETEAR LOS VALORES INGRESADOS
def resetear_valores():
    ent_importe_apuesta.delete(0, END)
    numero_seleccionado.set(-1)

# FUNCION DESPEDIDA AL MOMENTO DE DEJAR EL JUEGO
def despedida():
    messagebox.showinfo(title="VUELVA PRONTO", message=" Gracias por elegirnos...")
    root.destroy()

# FUNCION PARA VERIFICAR RESULTADO DEL JUEGO
def verificacion():
    numero_aleatorio = random.randint (1, 12)
    if numero_aleatorio == numero_seleccionado.get():
        messagebox.showinfo(title="RESULTADO DE LA APUESTA", message=f" Felicidades el numero ganador es el {numero_aleatorio}.\n\n              Acaba de ganar $ {int(ent_importe_apuesta.get()) * 2}")
        saldo.set(saldo.get() + (int(ent_importe_apuesta.get()) * 2))
        resetear_valores()
    else:
        messagebox.showinfo(title="RESULTADO DE LA APUESTA", message=f" Lo siento, el numero ganador es el {numero_aleatorio}.\n\n            Acaba de perder $ {int(ent_importe_apuesta.get())}")
        saldo.set(saldo.get() - int(ent_importe_apuesta.get()))
        resetear_valores()

# FUNCION PARA RECARGAR SALDO
def recarga():
    recarga = simpledialog.askfloat("RECARGA","Ingrese el importa a que desea recargar.")
    if recarga:    
        saldo.set(saldo.get() + recarga)
        resetear_valores()
    else:
        despedida()

# FUNCION PARA DAR INICIO AL JUEGO
def play ():
    try:
        if int(saldo.get()) >= int(ent_importe_apuesta.get()):
            if int(numero_seleccionado.get()) > 0:
                verificacion()
            else:
                messagebox.showinfo(title="ERROR", message=" Debes seleccionar un numero")
        else:
            if int(saldo.get()) == 0:
                respuesta = messagebox.askokcancel(title="ERROR", message="  Su saldo es $ 0.\n¿Desea recargar?")
                if respuesta == True:
                    recarga()
                else:
                    despedida()
            else:
                messagebox.showinfo(title="ERROR", message=" Su saldo es insuficiente para la apuesta que desea realizar.")
                resetear_valores()
    except ValueError:
        messagebox.showinfo(title="ERROR", message=" El valor ingresado no es valido.")
        resetear_valores()



# FRAME SOLICITUD DE DATOS
frame1 = Frame (root, width="290", height="340", bd=5, relief="solid")
frame1.grid_propagate(False)
frame1.grid(row=0, column=0, padx=5, pady=5)

# FRAME2 TABLERO DE JUEGO
frame2 = Frame (root, width="390", height="340", bd=5, relief="solid")
frame2.grid_propagate(False)
frame2.grid(row=0, column=1, padx=5, pady=5)

# INFORMACION DE DE DATOS Y SOLICITUDES
lbl_bienvenida = Label (frame1, text="¡BIENVENIDO!")
lbl_instrucciones = Label (frame1, text="Ingresar el importe de la apuesta,\n seleccionar su apuesta\n y presione ENTER.")
lbl_solicitud_apuesta = Label(frame1, text="Importe de la apuesta:")
ent_importe_apuesta = Entry (frame1, )
lbl_info_saldo = Label(frame1, text=f"Su saldo actual es de $")
lbl_saldo_actual = Label(frame1, textvariable=saldo)
btm_enter = Button (frame1, text="ENTER", command=play)

lbl_bienvenida.place(x=100, y=5)
lbl_instrucciones.place(x=50, y=30)
lbl_solicitud_apuesta.place(x=75, y=100)
ent_importe_apuesta.place(x=75, y=120)
lbl_info_saldo.place(x=65, y=150)
lbl_saldo_actual.place(x=185, y=150)
btm_enter.place(x=115, y=210)


# TABLERO DE JUEGO
for i in range(16):
    button = Radiobutton(frame2, text=f"{i+1}", variable=numero_seleccionado, value=i+1)
    button.grid(row=1 + i//4, column=i%4, padx=29, pady=29)


root.mainloop()