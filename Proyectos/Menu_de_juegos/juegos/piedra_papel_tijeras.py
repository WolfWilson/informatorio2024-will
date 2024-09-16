import random
import tkinter as tk
from tkinter import font
import os

# Función para que la computadora elija un elemento al azar
def elegirElementoDeComputadora():
    return random.randint(0, 2)

# Función que maneja la lógica del juego
def jugarRonda(eleccionUsuario):
    eleccionComputadora = elegirElementoDeComputadora()

    # Mostrar imágenes de las elecciones
    labelUsuario.config(image=imagenes[eleccionUsuario])
    labelComputadora.config(image=imagenes[eleccionComputadora])

    # Comparar las elecciones y generar resultado
    resultado = ""
    if eleccionComputadora != eleccionUsuario:
        if eleccionComputadora == 0 and eleccionUsuario == 2:
            resultado = 'Perdiste! Piedra le gana a las tijeras'
        elif eleccionComputadora == 2 and eleccionUsuario == 1:
            resultado = 'Perdiste! Las tijeras le ganan al papel.'
        elif eleccionComputadora == 1 and eleccionUsuario == 0:
            resultado = 'Perdiste! El papel le gana a la piedra'
        elif eleccionComputadora == 2 and eleccionUsuario == 0:
            resultado = 'Ganaste! La piedra le gana a las tijeras'
        elif eleccionComputadora == 1 and eleccionUsuario == 2:
            resultado = 'Ganaste! Las tijeras le ganan al papel'
        elif eleccionComputadora == 0 and eleccionUsuario == 1:
            resultado = 'Ganaste! El papel le gana a la piedra'
    else:
        resultado = 'Empate!'

    eleccionComputadoraTexto = elementos[eleccionComputadora]
    labelResultado.config(text=f"Computadora eligió: {eleccionComputadoraTexto}. {resultado}")

# Crear ventana
window = tk.Tk()
window.title('Piedra, papel o tijeras')

# Configuración de la ventana (color celeste)
window.configure(bg='lightblue')

# Lista de elementos
elementos = ['piedra', 'papel', 'tijeras']

# Fuente en negrita para el texto
bold_font = font.Font(weight='bold')

# Obtener ruta absoluta para las imágenes en la carpeta src (subimos un nivel para encontrar la carpeta src)
ruta_imagenes = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src')

# Verificar la ruta generada para asegurarnos de que es correcta
print(f"Ruta de las imágenes: {ruta_imagenes}")

# Cargar imágenes (desde la carpeta src)
imagenes = [
    tk.PhotoImage(file=os.path.join(ruta_imagenes, "piedra.png")),   # piedra.png
    tk.PhotoImage(file=os.path.join(ruta_imagenes, "papel.png")),    # papel.png
    tk.PhotoImage(file=os.path.join(ruta_imagenes, "tijeras.png"))   # tijeras.png
]

# Crear botones para las elecciones del usuario con resaltado
botonPiedra = tk.Button(window, text='Piedra', width=10, bg='white', fg='black', font=bold_font,
                        activebackground='yellow', activeforeground='blue', command=lambda: jugarRonda(0))
botonPapel = tk.Button(window, text='Papel', width=10, bg='white', fg='black', font=bold_font,
                       activebackground='yellow', activeforeground='blue', command=lambda: jugarRonda(1))
botonTijeras = tk.Button(window, text='Tijeras', width=10, bg='white', fg='black', font=bold_font,
                         activebackground='yellow', activeforeground='blue', command=lambda: jugarRonda(2))

# Mostrar botones en la interfaz
botonPiedra.pack(side='left', padx=20, pady=20)
botonPapel.pack(side='left', padx=20, pady=20)
botonTijeras.pack(side='left', padx=20, pady=20)

# Crear etiquetas para mostrar imágenes de la elección del usuario y la computadora
labelUsuario = tk.Label(window, bg='lightblue')
labelUsuario.pack(side='left', padx=10)

labelComputadora = tk.Label(window, bg='lightblue')
labelComputadora.pack(side='right', padx=10)

# Crear una etiqueta para mostrar el resultado en negrita
labelResultado = tk.Label(window, text="Elige una opción para comenzar el juego", font=bold_font, bg='lightblue')
labelResultado.pack(side='bottom', pady=20)

# Ejecutar la ventana
window.mainloop()
