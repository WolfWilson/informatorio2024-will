
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time


cartas = ['-As-', '-Dos-', '-Tres-', '-Cuatro-', '-Cinco-', '-Seis-',
          '-Siete-', '-Ocho-', '-Nueve-', '-Diez-', '-Jota-', '-Reina-', '-Rey-']


""" Principio funciones"""

"""funciones apuesta y saldo"""


def sumar_5():
    global suma_apuesta, saldo
    suma_apuesta += 5
    saldo -= 5
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_10():
    global suma_apuesta, saldo
    suma_apuesta += 10
    saldo -= 10
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_20():
    global suma_apuesta, saldo
    suma_apuesta += 20
    saldo -= 20
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_50():
    global suma_apuesta, saldo
    suma_apuesta += 50
    saldo -= 50
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_100():
    global suma_apuesta, saldo
    suma_apuesta += 100
    saldo -= 100
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def mostrar_saldo():
    global saldo
    etq_saldo_1.delete(0, tk.END)
    etq_saldo_1.insert(0, saldo)


def mostrar_suma_apuesta():
    global suma_apuesta
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)


def fondos_negativos():  # compara si el saldo es negatico o la apuesta es mayor el saldo del banco
    global saldo
    if saldo <= 0:
        resp_saldo = messagebox.askquestion(
            "Cajero", "Te quedaste sin fondos, ¿Deseas Sumar 1000 mas a tu saldo?")
        if resp_saldo == "yes":
            messagebox.showinfo(
                "Suma saldo", "Se te acreditaron $1000 mas para seguir jugando")
            saldo += 1000
        else:
            messagebox.showinfo(
                "Lo Siento", "Se a quedado sin saldo, puede terminar la mano")


""""Funcion tutorial"""


def ver_tuto():
    respuesta = messagebox.askquestion(
        "Como Jugar", "¿Desea leer un mini tutorial del juego?")
    if respuesta == "yes":
        messagebox.showinfo("Como Jugar",
                            "Se debe sumar 21 puntos. El Crupier está obligado a pedir carta siempre que su puntuación sume 16 o menos. En el caso del crupier, los ases valen 11 mientras no se pase de 21, y 1 en caso contrario. Las cartas numéricas suman su valor, las figuras suman 10 y el 'as' vale 11 o 1, depende la situación.")
    else:
        pass


""" funcion para iniciar"""


def desea_comenzar():
    comenzar = messagebox.askquestion(
        "Bienvenido/a Black Jack 21 INFO24", "¿Desea Comenzar a Jugar?")
    if comenzar == "yes":
        messagebox.showinfo(
            "Comencemos", " Que disfrutes el Juego, apuesta minima para iniciar $5")
        time.sleep(0.5)
        iniciar_mano()
    else:
        messagebox.showinfo("Adios", "Vuelve Pronto")
        time.sleep(1)
        exit(2)


def desea_nueva_mano():
    time.sleep(0.5)
    comenzar = messagebox.askquestion(
        "Black Jack 21", "¿Desea Comenzar Nueva Mano?")
    if comenzar == "yes":
        messagebox.showinfo(
            "Continuamos", " Apuesta minima de la mano $5")
        time.sleep(0.5)
        iniciar_mano()
    else:
        messagebox.showinfo("Adios", "Vuelve Pronto")
        time.sleep(1)
        exit(2)


def iniciar_mano():
    """uncion q inicia la mano y reparte dos cartas cada uno"""
    global mano_crupier, mano_player, saldo, suma_apuesta
    suma_apuesta = 0
    mano_player = [obtener_nueva_carta(), obtener_nueva_carta()]
    mano_crupier = [obtener_nueva_carta(), obtener_nueva_carta()]
    sumar_5()
    mostrar_saldo()
    mostrar_suma_apuesta()
    etq_cartas_player_1.delete(0, tk.END)
    etq_cartas_player_1.insert(0, mano_player)
    etq_cartas_crupier_1.delete(0, tk.END)
    etq_cartas_crupier_1.insert(0, mano_crupier[0] + " 'Carta Oculta' ")
    etq_pts_player_1.delete(0, tk.END)
    etq_pts_player_1.insert(0, valor_mano(mano_player))
    etq_pts_crupier_1.delete(0, tk.END)
    if valor_mano(mano_player) == 21:
        messagebox.showinfo(
            "Ganaste", '¡¡¡Black Jack!!!¡Felicidades Ganaste la mano, Sumaste 21!')
        saldo += (suma_apuesta*2)
        time.sleep(0.5)
        mostrar_suma_apuesta()
        mostrar_saldo()
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == 21 and valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Empate!!!", ' Ambos obtuvieron 21 puntos')
        saldo += suma_apuesta
        mostrar_saldo()
        desea_nueva_mano()


def continuar_jugando():
    global saldo, suma_apuesta
    mostrar_suma_apuesta()
    mano_player.append(obtener_nueva_carta())
    etq_cartas_player_1.delete(0, tk.END)
    etq_cartas_player_1.insert(0, mano_player)
    etq_cartas_crupier_1.delete(0, tk.END)
    etq_cartas_crupier_1.insert(0, mano_crupier[0] + " '+Carta Oculta' ")
    etq_pts_player_1.delete(0, tk.END)
    etq_pts_player_1.insert(0, valor_mano(mano_player))
    if valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡¡Ganaste!!!", '¡¡¡Black Jack!!! ¡Felicidades Ganaste la mano, Sumaste 21!')
        juega_crupier()
        etq_cartas_crupier_1.delete(0, tk.END)
        etq_cartas_crupier_1.insert(0, mano_crupier)
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_player) > 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Perdiste!!!", 'Lo siento, te has paso de 21 puntos')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()


def detner_pasar():
    global saldo, suma_apuesta
    juega_crupier()
    etq_cartas_player_1.delete(0, tk.END)
    etq_cartas_player_1.insert(0, mano_player)
    etq_cartas_crupier_1.delete(0, tk.END)
    etq_cartas_crupier_1.insert(0, mano_crupier)
    etq_pts_player_1.delete(0, tk.END)
    etq_pts_player_1.insert(0, valor_mano(mano_player))
    etq_pts_crupier_1.delete(0, tk.END)
    etq_pts_crupier_1.insert(0, valor_mano(mano_crupier))
    if valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Ganaste!!!", '¡¡¡Black Jack!!! ¡Felicidades ganaste la mano, Sumaste 21 puntos!')
        etq_cartas_crupier_1.delete(0, tk.END)
        etq_cartas_crupier_1.insert(0, mano_crupier)
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == 21 and valor_mano(mano_player) < 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "Lo siento", '¡Perdiste el crupier las tiene mejores, Sumo 21!')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) > 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡Felicidades!", "¡¡¡Ganaste!!! .El crupier se paso de rosca y sumo mas de 21")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) < valor_mano(mano_player):
        time.sleep(0.5)
        messagebox.showinfo("¡Felicidades! ",
                            "¡¡¡Ganaste!!! tenes mejor puntaje que el crupier")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == valor_mano(mano_player):
        messagebox.showinfo(
            "¡Empate!", " Sumaron los mismos puntos y se te retorna tu apuesta")
        saldo += suma_apuesta
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_player) == 21:
        messagebox.showinfo(
            "¡Black Jack!", "¡Felicidades Ganaste la mano, Sumaste 21!")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) > valor_mano(mano_player) and valor_mano(mano_crupier) < 21:
        messagebox.showinfo(
            "¡Lo Siento!", '¡Perdiste el crupier las tiene mejores!')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()


def obtener_nueva_carta():
    maxi = len(cartas)
    indice = random.randint(0, maxi)-1
    return cartas[indice]


def valor_mano(mano):
    """Calcula el valor de mano, elige el valor del AS de acuerdo situación"""
    valor_mano = 0
    hay_as = False
    for carta in mano:
        valor_carta = cartas.index(carta)+1
        if valor_carta > 10:
            valor_carta = 10
        if carta == '-As-':  # busca si la mano tiene un 'as' en ella
            hay_as = True
        valor_mano += valor_carta
    if hay_as and valor_mano <= 11:  # comprobamos si el valor de la mano es menor a 10 y si hay un 'as' presente el valor del 'as' pasa a ser 11
        valor_mano += 10
    return valor_mano


def juega_crupier():
    while valor_mano(mano_crupier) < 17:
        nueva_carta = obtener_nueva_carta()
        mano_crupier.append(nueva_carta)
    return mano_crupier


"""Fin funciones
"""

ventana = tk.Tk()  # Crea una instancia de la clase Tk, que representa la ventana principal
# Establece el título de la ventana principal
ventana.title("BLACK JACK 21 Informatorio2024")
# Establece el tamaño de la ventana principal a 350x400 píxeles
ventana.geometry("500x600")
# establece tamaño fijo de ventana
ventana.resizable(False, False)


"""Frame 1"""
frame_1 = Frame(ventana)
frame_1.config(background="Green", bd=1,
               relief="solid", cursor="target",)
frame_1.pack(expand=True, fill="both")


"""Frame 1_1"""
frame_1_1 = Frame(frame_1, width="250", height="300")
frame_1_1.config(background="green", bd=1, relief="solid")
frame_1_1.grid(row=0, column=0)

etq_1 = tk.Label(frame_1_1, text="PLAYER")
etq_1.config(bg="grey75", fg="black", font="arial 10")
etq_1.place(relx=.3, rely=.05, bordermode=OUTSIDE,
            height=30, width=100)

# para mostrar el puntaje del Player
etq_pts_player = tk.Label(frame_1_1, text="Puntos Cartas")
etq_pts_player.config(bg="grey75", fg="black", border=2,
                      font="arial 10", justify="right")
etq_pts_player.place(x=10, y=250, width=90, height=30)

etq_pts_player_1 = tk.Entry(frame_1_1)  # para mostrar el puntaje del Player
etq_pts_player_1.config(bg="white", fg="black", border=2,
                        font="arial 25", justify="right")
etq_pts_player_1.place(x=105, y=250, width=60, height=30)

etq_cartas_player = tk.Label(frame_1_1, text="Cartas jugador")
etq_cartas_player.config(bg="grey75", fg="black", border=2,
                         font="arial 10", justify="center")
etq_cartas_player.place(relx=0.03, rely=0.35, width=100, height=30)

etq_cartas_player_1 = tk.Entry(frame_1_1)
etq_cartas_player_1.config(bg="white", fg="black", border=2,
                           font="arial 10", justify="center")
etq_cartas_player_1.place(
    relx=0.03, rely=0.5, width=230, height=30)

"""Frame 1_2"""
frame_1_2 = Frame(frame_1, width="250", height="300")
frame_1_2.config(background="Green", bd=1, relief="solid")
frame_1_2.grid(row=0, column=1)


etq_2 = tk.Label(frame_1_2, text="CRUPIER")
etq_2.config(bg="grey75", fg="black", font="arial 10")
etq_2.place(relx=.3, rely=.05, bordermode=INSIDE,
            height=30, width=100)

# para mostrar el puntaje del crupier
etq_pts_crupier = tk.Label(frame_1_2, text="Puntos Cartas")
etq_pts_crupier.config(bg="grey75", fg="black", border=2,
                       font="arial 10", justify="right")
etq_pts_crupier.place(x=10, y=250, width=90, height=30)


etq_pts_crupier_1 = tk.Entry(frame_1_2)  # para mostrar el puntaje del crupier
etq_pts_crupier_1.config(bg="white", fg="black", border=2,
                         font="arial 25", justify="right")
etq_pts_crupier_1.place(x=105, y=250, width=60, height=30)


etq_cartas_crupier = tk.Label(frame_1_2, text="Cartas Crupier")
etq_cartas_crupier.config(bg="grey75", fg="black", border=2,
                          font="arial 10", justify="center")
etq_cartas_crupier.place(relx=0.03, rely=0.35, width=100, height=30)

etq_cartas_crupier_1 = tk.Entry(frame_1_2)
etq_cartas_crupier_1.config(bg="white", fg="black", border=2,
                            font="arial 10", justify="center")
etq_cartas_crupier_1.place(
    relx=0.03, rely=0.5, width=230, height=30)

"""Frame 2"""

frame_2 = Frame(ventana)
frame_2.config(background="green", bd=1, relief="solid",
               width="500", height="250")
frame_2.pack(expand=True, fill="both")

# se muestra el monto apuesta de la apuesta
etq_apuesta = tk.Label(frame_2, text="Valor Apuesta")
etq_apuesta.config(bg="grey75", fg="black", border=2,
                   font="arial 10", justify="right")
etq_apuesta.place(x=10, y=50, width=90, height=30)

# se muestra el monto apuesta de la apuesta
etq_apuesta_1 = tk.Entry(frame_2)
etq_apuesta_1.config(bg="white", fg="black", border=2,
                     font="arial 15", justify="right")
etq_apuesta_1.place(x=105, y=50, width=80, height=30)

# se muestra el saldo de la cuenta en pesos
etq_saldo = tk.Label(frame_2, text="Saldo")
etq_saldo.config(bg="grey75", fg="black", border=2,
                 font="arial 10", justify="right")
etq_saldo.place(x=10, y=90, width=90, height=30)


etq_saldo_1 = tk.Entry(frame_2)  # se muestra el saldo de la cuenta en pesos
etq_saldo_1.config(bg="white", fg="black", border=2,
                   font="arial 15", justify="right")
etq_saldo_1.place(x=105, y=90, width=80, height=30)

btn_apuesta_5 = tk.Button(frame_2, text="Apuesta $5",
                          command=sumar_5)
btn_apuesta_5.config(bg="grey75", fg="black", font="arial12")
btn_apuesta_5.place(y=10, x=380, width=110, height=35)

btn_apuesta_10 = tk.Button(frame_2, text="Apuesta $10", command=sumar_10)
btn_apuesta_10.config(bg="grey75", fg="black", font="arial12")
btn_apuesta_10.place(
    y=55, x=380, width=110, height=35)

btn_apuesta_20 = tk.Button(frame_2, text="Apuesta $20",
                           command=sumar_20)
btn_apuesta_20.config(
    bg="grey75", fg="black", font="arial12")
btn_apuesta_20.place(
    y=100, x=380, width=110, height=35)

btn_apuesta_50 = tk.Button(frame_2, text="Apuesta $50", command=sumar_50)
btn_apuesta_50.config(bg="grey75", fg="black", font="arial12")
btn_apuesta_50.place(y=145, x=380, width=110, height=35)

btn_apuesta_100 = tk.Button(frame_2, text="Apuesta $100", command=sumar_100)
btn_apuesta_100.config(bg="grey75", fg="black", font="arial12")
btn_apuesta_100.place(y=190, x=380, width=110, height=35)

btn_pedir = tk.Button(frame_2, text="Pedir",
                      command=continuar_jugando)
btn_pedir.config(bg="grey75", fg="black", font="arial12")
btn_pedir.place(y=40, x=250, width=90, height=55)

btn_pasar = tk.Button(frame_2, text="Pasar",
                      command=detner_pasar)
btn_pasar.config(bg="grey75", fg="black", font="arial12")
btn_pasar.place(y=130, x=250, width=90, height=55)

"""Frame 3"""

frame_3 = Frame(ventana)
frame_3.config(background="grey75", bd=1,
               relief="solid", width="500", height="50")
frame_3.pack(expand=True, fill="both")

btn_tuto = tk.Button(frame_3, text="Tutorial", command=ver_tuto, )
btn_tuto.config(bg="green4", fg="white", font="arial 12",)
btn_tuto.place(y=10, x=220, width=70, height=30)

suma_apuesta = 0
saldo = 1000
mano_player = []
mano_crupier = []
mostrar_saldo()
mostrar_suma_apuesta()
desea_comenzar()  # se inicia la manmo del crupier y del juagdor


ventana.mainloop()
