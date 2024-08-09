import tkinter as tk

def crear_gradiente(canvas, color1, color2):
    # Obtener el tamaño del canvas
    ancho = canvas.winfo_width()
    alto = canvas.winfo_height()

    # Crear el gradiente vertical
    for i in range(alto):
        # Calcular el color para cada línea
        r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // alto
        g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // alto
        b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // alto
        color = f'#{r:02x}{g:02x}{b:02x}'

        # Dibujar una línea horizontal
        canvas.create_line(0, i, ancho, i, fill=color)

def on_resize(event):
    # Redibujar el gradiente al redimensionar la ventana
    crear_gradiente(event.widget, "#ff0000", "#0000ff")

root = tk.Tk()
root.geometry("400x400")

# Crear un canvas que ocupe toda la ventana
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Dibujar el gradiente en el canvas
crear_gradiente(canvas, "#ff0000", "#0000ff")

# Redibujar el gradiente al redimensionar la ventana
canvas.bind("<Configure>", on_resize)

root.mainloop()
