from PIL import Image, ImageTk
import tkinter as tk
import pygame
import random
import os

# Inicialización de Pygame para manejo de audio
pygame.init()
pygame.mixer.init()

# Configuración de la ventana
window = tk.Tk()
window.geometry('1000x600')
window.title('Flappy Bird')

x = 150
y = 300
score = 0
speed = 10
game_over = False

# Definir ruta para los archivos multimedia dentro de "src"
ruta_media = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src')

# Cargar la imagen del pájaro y obtener sus dimensiones
img_bird_path = os.path.join(ruta_media, 'bird.png')
img_bird = Image.open(img_bird_path)
bird_width, bird_height = img_bird.size
img_bird = ImageTk.PhotoImage(img_bird)

# Cargar las imágenes de las tuberías y otros elementos
img_pipe_down_path = os.path.join(ruta_media, 'pipe.png')
img_pipe_down = Image.open(img_pipe_down_path)
img_pipe_up = img_pipe_down.rotate(180)
img_pipe_down = ImageTk.PhotoImage(img_pipe_down)
img_pipe_up = ImageTk.PhotoImage(img_pipe_up)

img_reset_path = os.path.join(ruta_media, 'restart.png')
img_reset = Image.open(img_reset_path)
img_reset = ImageTk.PhotoImage(img_reset)

# Crear el lienzo (canvas) y configurar el entorno
canvas = tk.Canvas(window, highlightthickness=0, bg='#00bfff')
canvas.place(relwidth=1, relheight=1)

text_score = canvas.create_text(50, 50, text='0', fill='white', font=('D3 Egoistism outline', 30))

bird = canvas.create_image(x, y, anchor='nw', image=img_bird)
pipe_top = canvas.create_image(1200, -550, anchor='nw', image=img_pipe_up)
pipe_down = canvas.create_image(1200, -550, anchor='nw', image=img_pipe_down)

# Cargar y reproducir sonidos
sound_jump_path = os.path.join(ruta_media, 'jump.mp3')
sound_die_path = os.path.join(ruta_media, 'die.mp3')

pygame.mixer.music.load(sound_jump_path)
pygame.mixer.music.play(loops=0)  # Reproduce el sonido una vez

# Movimiento del pájaro al presionar la barra espaciadora
def move_bird_key(event):
    global x, y
    if not game_over:
        y -= 30
        canvas.coords(bird, x, y)
        pygame.mixer.music.load(sound_jump_path)
        pygame.mixer.music.play(loops=0)  # Reproduce el sonido una vez

window.bind("<space>", move_bird_key)

# Función para mover el pájaro automáticamente (gravedad)
def move_bird():
    global x, y, game_over
    if not game_over:
        y += 7  # Incrementa la posición en Y (simulando gravedad)
        canvas.coords(bird, x, y)

        window_height = window.winfo_height()
        if y < 0 or y > window_height - bird_height:
            game_end()  # Finaliza el juego si el pájaro sale de los límites
        else:
            window.after(50, move_bird)

def move_pipe():
    global score, game_over, speed
    if not game_over:
        canvas.move(pipe_top, -speed, 0)
        canvas.move(pipe_down, -speed, 0)

        if canvas.coords(pipe_down)[0] < -100:
            h = window.winfo_height()
            num = random.choice([i for i in range(160, h, 160)])
            canvas.coords(pipe_down, window.winfo_width(), num+160)
            canvas.coords(pipe_top, window.winfo_width(), num-900)

        pipe_x = canvas.coords(pipe_down)[0]
        bird_x = canvas.coords(bird)[0]

        if pipe_x < bird_x and pipe_x + speed >= bird_x:
            score += 1
            speed += 1
            canvas.itemconfigure(text_score, text=str(score))

        window.after(50, move_pipe)

# Función para terminar el juego
def game_end():
    global game_over
    game_over = True
    lbl_game_over.place(relx=0.5, rely=0.4, anchor='center')
    bt_reset.place(relx=0.5, rely=0.5, anchor='center')
    pygame.mixer.music.load(sound_die_path)
    pygame.mixer.music.play(loops=0)

def check_collision():
    if not game_over:
        bird_coords = canvas.bbox(bird)
        pipe_down_coords = canvas.bbox(pipe_down)
        pipe_top_coords = canvas.bbox(pipe_top)

        bird_collision_box = (
            bird_coords[0] + 15,  
            bird_coords[1] + 15,  
            bird_coords[2] - 15,  
            bird_coords[3] - 15   
        )

        if bird_collision_box[0] < pipe_down_coords[2] and bird_collision_box[2] > pipe_down_coords[0]:
            if bird_collision_box[1] < pipe_top_coords[3] or bird_collision_box[3] > pipe_down_coords[1]:
                game_end()

        window.after(50, check_collision)

# Función para reiniciar el juego
def reset_game():
    global x, y, score, speed, game_over
    x = 150
    y = 300
    score = 0
    speed = 10
    game_over = False
    canvas.coords(bird, x, y)
    canvas.coords(pipe_top, 1200, -550)
    canvas.coords(pipe_down, 1200, 550)
    canvas.itemconfigure(text_score, text="0")
    lbl_game_over.place_forget()
    bt_reset.place_forget()
    move_bird()
    move_pipe()
    check_collision()

# Etiqueta de Game Over y botón de reinicio
lbl_game_over = tk.Label(window, text="Game Over!", font=('D3 Egoistism outline', 30), fg='white', bg='#00bfff')
bt_reset = tk.Button(window, border=0, image=img_reset, activebackground='#00bfff', bg='#00bfff', command=reset_game)

window.after(50, move_bird)
window.after(50, move_pipe)
window.after(50, check_collision)

window.mainloop()
