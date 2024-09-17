import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import time
import os

# Definir la ruta de la carpeta 'src'
ruta_media = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src')

cartas = ['as_corazon', 'dos_corazon', 'tres_corazon', 'cuatro_corazon', 'cinco_corazon', 'seis_corazon',
          'siete_corazon', 'ocho_corazon', 'nueve_corazon', 'diez_corazon', 'jota_corazon', 'reina_corazon', 'rey_corazon',
          'as_picas', 'dos_picas', 'tres_picas', 'cuatro_picas', 'cinco_picas', 'seis_picas',
          'siete_picas', 'ocho_picas', 'nueve_picas', 'diez_picas', 'jota_picas', 'reina_picas', 'rey_picas',
          'as_diamante', 'dos_diamante', 'tres_diamante', 'cuatro_diamante', 'cinco_diamante', 'seis_diamante',
          'siete_diamante', 'ocho_diamante', 'nueve_diamante', 'diez_diamante', 'jota_diamante', 'reina_diamante', 'rey_diamante',
          'as_trebol', 'dos_trebol', 'tres_trebol', 'cuatro_trebol', 'cinco_trebol', 'seis_trebol',
          'siete_trebol', 'ocho_trebol', 'nueve_trebol', 'diez_trebol', 'jota_trebol', 'reina_trebol', 'rey_trebol']

# Variables globales
maso_juego = cartas.copy()
saldo = 1000
suma_apuesta = 0
mano_player = []
mano_crupier = []

# Redimensionar las imágenes de cartas
def size_cards(carta):
    global carta_img
    carta_path = os.path.join(ruta_media, 'img', 'cartas', f'{carta}.png')  # Construir la ruta a la imagen
    carta_img = Image.open(carta_path)
    card_size_card = carta_img.resize((100, 140))
    carta_img = ImageTk.PhotoImage(card_size_card)
    return carta_img

# Funciones para manejar las apuestas
def sumar_10():
    global suma_apuesta, saldo
    if saldo >= 10:
        suma_apuesta += 10
        saldo -= 10
        mostrar_saldo()
    else:
        messagebox.showinfo("Fondos insuficientes", "No tienes suficiente saldo.")

def sumar_20():
    global suma_apuesta, saldo
    if saldo >= 20:
        suma_apuesta += 20
        saldo -= 20
        mostrar_saldo()
    else:
        messagebox.showinfo("Fondos insuficientes", "No tienes suficiente saldo.")

def sumar_50():
    global suma_apuesta, saldo
    if saldo >= 50:
        suma_apuesta += 50
        saldo -= 50
        mostrar_saldo()
    else:
        messagebox.showinfo("Fondos insuficientes", "No tienes suficiente saldo.")

def sumar_100():
    global suma_apuesta, saldo
    if saldo >= 100:
        suma_apuesta += 100
        saldo -= 100
        mostrar_saldo()
    else:
        messagebox.showinfo("Fondos insuficientes", "No tienes suficiente saldo.")

# Función para mostrar el saldo actualizado
def mostrar_saldo():
    print(f"Saldo: {saldo} - Apuesta: {suma_apuesta}")

# Función que muestra las cartas del jugador e inserta las imágenes de cada carta en cada label
def mostrar_carta_player(mano):
    global player_img1, player_img2, player_img3, player_img4, player_img5
    player_spot = 0
    for carta in mano:
        player_spot += 1
        if player_spot == 1:
            player_img1 = size_cards(carta)
            player_label_1.config(image=player_img1)
        elif player_spot == 2:
            player_img2 = size_cards(carta)
            player_lebel_2.config(image=player_img2)
        elif player_spot == 3:
            player_img3 = size_cards(carta)
            player_label_3.config(image=player_img3)
        elif player_spot == 4:
            player_img4 = size_cards(carta)
            player_label_4.config(image=player_img4)
        elif player_spot == 5:
            player_img5 = size_cards(carta)
            player_label_5.config(image=player_img5)

# Función que muestra las cartas del crupier e inserta las imágenes de cada carta en cada label
def mostrar_carta_crupier(mano):
    global crupier_img1, crupier_img2, crupier_img3, crupier_img4, crupier_img5
    crupier_spot = 0
    for carta in mano:
        crupier_spot += 1
        if crupier_spot == 1:
            crupier_img1 = size_cards(carta)
            crupier_label_1.config(image=crupier_img1)
        elif crupier_spot == 2:
            crupier_img2 = size_cards(carta)
            crupier_label_2.config(image=crupier_img2)
        elif crupier_spot == 3:
            crupier_img3 = size_cards(carta)
            crupier_label_3.config(image=crupier_img3)
        elif crupier_spot == 4:
            crupier_img4 = size_cards(carta)
            crupier_label_4.config(image=crupier_img4)
        elif crupier_spot == 5:
            crupier_img5 = size_cards(carta)
            crupier_label_5.config(image=crupier_img5)

# Función que muestra en el crupier solo una carta visible y la otra oculta
def mostrar_crupier_oculta(mano):
    global crupier_img1, crupier_img2
    crupier_spot = 0
    for carta in mano:
        crupier_spot += 1
        if crupier_spot == 1:
            crupier_img1 = size_cards(carta)
            crupier_label_1.config(image=crupier_img1)
        elif crupier_spot == 2:
            crupier_img2 = size_cards('carta_oculta')  # muestra carta oculta
            crupier_label_2.config(image=crupier_img2)

# Función para limpiar las cartas del juego anterior
def limpiar_cartas():
    player_label_1.config(image='')
    player_lebel_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    crupier_label_1.config(image='')
    crupier_label_2.config(image='')
    crupier_label_3.config(image='')
    crupier_label_4.config(image='')
    crupier_label_5.config(image='')

# Iniciar la ventana
ventana = tk.Tk()
ventana.title("BLACK JACK-Informatorio-Parra Cristian")
ventana.iconbitmap(os.path.join(ruta_media, 'img', 'icon.ico'))  # Cargar el ícono desde la carpeta 'src'
ventana.geometry("900x550")  # Definir el tamaño de la ventana
ventana.config(bg="green")  # Cambiar el fondo de la ventana a verde

"""Frame 1"""
frame_1 = Frame(ventana)
frame_1.config(background="Green", bd=1, relief="solid", cursor="target")
frame_1.pack(fill="both", padx=10, pady=10)

# Crear labels para las cartas del jugador
player_label_1 = Label(frame_1, text='', bg='green')
player_label_1.grid(row=0, column=0, pady=10, padx=5)

player_lebel_2 = Label(frame_1, text='', bg='green')
player_lebel_2.grid(row=0, column=1, pady=10, padx=5)

player_label_3 = Label(frame_1, text='', bg='green')
player_label_3.grid(row=0, column=2, pady=10, padx=5)

player_label_4 = Label(frame_1, text='', bg='green')
player_label_4.grid(row=0, column=3, pady=10, padx=5)

player_label_5 = Label(frame_1, text='', bg='green')
player_label_5.grid(row=0, column=4, pady=10, padx=5)

# Crear labels para las cartas del crupier
crupier_label_1 = Label(frame_1, text='', bg='green')
crupier_label_1.grid(row=1, column=0, pady=10, padx=5)

crupier_label_2 = Label(frame_1, text='', bg='green')
crupier_label_2.grid(row=1, column=1, pady=10, padx=5)

crupier_label_3 = Label(frame_1, text='', bg='green')
crupier_label_3.grid(row=1, column=2, pady=10, padx=5)

crupier_label_4 = Label(frame_1, text='', bg='green')
crupier_label_4.grid(row=1, column=3, pady=10, padx=5)

crupier_label_5 = Label(frame_1, text='', bg='green')
crupier_label_5.grid(row=1, column=4, pady=10, padx=5)

"""Frame 2 para los botones"""
frame_2 = Frame(ventana)
frame_2.config(background="green", bd=1, relief="solid")
frame_2.pack(fill="x", padx=10, pady=10)

# Botones de Apuesta
btn_apuesta_10 = tk.Button(frame_2, text="Apuesta +$10", command=sumar_10)
btn_apuesta_10.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_10.pack(side="left", padx=5)

btn_apuesta_20 = tk.Button(frame_2, text="Apuesta +$20", command=sumar_20)
btn_apuesta_20.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_20.pack(side="left", padx=5)

btn_apuesta_50 = tk.Button(frame_2, text="Apuesta +$50", command=sumar_50)
btn_apuesta_50.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_50.pack(side="left", padx=5)

btn_apuesta_100 = tk.Button(frame_2, text="Apuesta +$100", command=sumar_100)
btn_apuesta_100.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_100.pack(side="left", padx=5)

# Botón de pedir carta
btn_pedir = tk.Button(frame_2, text="Pedir Carta", command=lambda: print("Pedir Carta"))
btn_pedir.config(bg="grey75", fg="black", font="arial 12")
btn_pedir.pack(side="left", padx=5)

# Botón de pasar
btn_pasar = tk.Button(frame_2, text="Pasar", command=lambda: print("Pasar"))
btn_pasar.config(bg="grey75", fg="black", font="arial 12")
btn_pasar.pack(side="left", padx=5)

# Inicializar el juego mostrando una carta oculta al inicio
carta_oculta = 'carta_oculta'
crupier_img1 = size_cards(carta_oculta)
crupier_label_1.config(image=crupier_img1)
player_img1 = size_cards(carta_oculta)
player_label_1.config(image=player_img1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
