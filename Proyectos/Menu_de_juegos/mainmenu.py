import tkinter as tk
import subprocess
import os
import sys
from PIL import Image, ImageTk

# Ruta de la carpeta de juegos
JUEGOS_DIR = os.path.join(os.path.dirname(__file__), 'Juegos')

# Ruta del ícono personalizado
ICON_PATH = os.path.join(os.path.dirname(__file__), 'src', 'iconmenu.ico')

# Diccionario de juegos y sus imágenes asociadas
juegos = {
    "Ahorcado By Wilson": ("ahorcado_tkv2.py", "skull.png"),
    "Mesa de Apuestas By José": ("MesaDeApuesta.pyw", "bet.png"),
    "Blackjack 21 By Cristian": ("blackjack_21_apuestas.py", "bj.png"),
    "Piedra Papel Tijeras By Mariana (en espera)": ("piedra_papel_tijeras.py", "rps.png"),  # Futuro juego
    "Juego Desconocido (en espera)": ("juego_desconocido.py", "unknown.png")  # Futuro juego
}

# Función para ejecutar un juego
def ejecutar_juego(juego_archivo):
    juego_path = os.path.join(JUEGOS_DIR, juego_archivo)
    if os.path.exists(juego_path):
        # Ejecutar el juego en el mismo entorno virtual me da error sino
        subprocess.run([sys.executable, juego_path])
    else:
        print(f"El juego {juego_archivo} no se encontró.")

# Función para centrar la ventana
def centrar_ventana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)

    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

# Crear la ventana principal
root = tk.Tk()
root.title("Menú de Juegos")

# Establecer tamaño de la ventana y centrarla
ventana_ancho = 680
ventana_alto = 540
centrar_ventana(root, ventana_ancho, ventana_alto)

# Deshabilitar la posibilidad de redimensionar la ventana
root.resizable(False, False)

# Establecer el ícono de la ventana
root.iconbitmap(ICON_PATH)

# Diccionario para almacenar las imágenes de los botones
button_images = {}

# Crear botones para cada juego
for nombre, (archivo, img) in juegos.items():
    # Cargar la imagen asociada a este juego
    img_path = os.path.join(os.path.dirname(__file__), 'src', img)
    button_image = Image.open(img_path)
    button_image = button_image.resize((50, 50), Image.Resampling.LANCZOS)  # Ajustar el tamaño de la imagen
    button_photo = ImageTk.PhotoImage(button_image)

    # Guardar la imagen para evitar que se recoja por el recolector de basura
    button_images[nombre] = button_photo

    # Crear el botón con la imagen y texto asociado
    btn = tk.Button(root, text=nombre, image=button_photo, compound="left",
                    command=lambda archivo=archivo: ejecutar_juego(archivo),
                    width=380, height=60, font=("Helvetica", 10, "bold"))
    btn.pack(pady=10, padx=20)

# Iniciar el loop de la ventana principal
root.mainloop()
