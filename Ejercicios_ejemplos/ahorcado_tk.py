import tkinter as tk
from tkinter import messagebox
import random
import os

# Ruta del ícono (definida globalmente para que esté disponible después de compilar)
ICON_PATH = os.path.join(os.path.dirname(__file__), "src", "iconh.ico")

# Diccionarios de palabras por temáticas
palabras_por_tematica = {
    "Frutas": ["manzana", "banana", "naranja", "pera", "uva", "mango", "limon", "kiwi", "sandia", "melon", 
               "fresa", "cereza", "ciruela", "durazno", "granada", "higo", "papaya", "piña", "frambuesa", 
               "grosella", "arándano", "mandarina", "pomelo", "guayaba", "lichi"],
    "Utensilios de cocina": ["cuchillo", "tenedor", "cuchara", "sarten", "olla", "colador", "batidora", 
                             "licuadora", "tostadora", "cafetera", "tetera", "rallador", "cacerola", "espumadera", 
                             "abrelatas", "pinzas", "mortero", "rodillo", "espátula", "cucharon", "cuchillo", 
                             "pelador", "tabla", "vaso", "plato"],
    "Paises": ["argentina", "brasil", "canada", "dinamarca", "egipto", "francia", "alemania", "hungria", 
               "india", "japon", "kenia", "libano", "mexico", "nepal", "oman", "portugal", "qatar", 
               "rusia", "suecia", "turquia", "uruguay", "vietnam", "yemen", "zambia", "zimbabwe"],
    "Palabras reservadas en Python": ["False", "None", "True", "and", "as", "assert", "async", "await", 
                                      "break", "class", "continue", "def", "del", "elif", "else", "except", 
                                      "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", 
                                      "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
}

class Ahorcado:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")

        # Establecer tamaño de la ventana y hacer que no sea redimensionable
        self.root.geometry("400x450")  # Tamaño de la ventana: 400x400 píxeles
        self.centrar_ventana(400, 450)# Centrar la ventana en la pantalla
        self.root.resizable(False, False)  # Deshabilitar la redimensión de la ventana

        # Establecer el ícono de la ventana
        self.root.iconbitmap(ICON_PATH)

        
        

        # Variables del juego
        self.tematica = tk.StringVar(value="Frutas")
        self.intentos_restantes = 5
        self.palabra_secreta = ""
        self.letras_adivinadas = set()
        self.progreso = []

        # Configuración de la interfaz
        self.setup_ui()

    def centrar_ventana(self, width, height):
        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer la geometría de la ventana para que aparezca centrada
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        # Menú de selección de temática
        tk.Label(self.root, text="Seleccione una temática:").pack(pady=10)
        for tematica in palabras_por_tematica.keys():
            tk.Radiobutton(self.root, text=tematica, variable=self.tematica, value=tematica).pack()

        # Botones de control
        tk.Button(self.root, text="Comenzar a jugar", command=self.iniciar_juego).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

        # Mostrar intentos restantes
        self.label_intentos = tk.Label(self.root, text=f"Intentos restantes: {self.intentos_restantes}")
        self.label_intentos.pack(pady=10)

        # Mostrar progreso
        self.label_progreso = tk.Label(self.root, text="Progreso: " + " ".join(self.progreso))
        self.label_progreso.pack(pady=10)

        # Entrada para adivinar letras
        self.entrada_letra = tk.Entry(self.root)
        self.entrada_letra.pack(pady=10)
        tk.Button(self.root, text="Adivinar letra", command=self.adivinar_letra).pack(pady=10)

    def iniciar_juego(self):
        self.intentos_restantes = 5
        self.letras_adivinadas = set()
        self.palabra_secreta = obtener_palabra_secreta(self.tematica.get()).lower()
        self.progreso = ["_"] * len(self.palabra_secreta)
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")
        self.label_progreso.config(text="Progreso: " + " ".join(self.progreso))

    def adivinar_letra(self):
        letra = self.entrada_letra.get().lower()
        self.entrada_letra.delete(0, tk.END)

        if letra in self.letras_adivinadas:
            self.centrar_popup("Letra repetida", "Ya has adivinado esa letra. Intenta con otra.")
            return

        self.letras_adivinadas.add(letra)

        if letra in self.palabra_secreta:
            for i, char in enumerate(self.palabra_secreta):
                if char == letra:
                    self.progreso[i] = letra
            if "_" not in self.progreso:
                self.centrar_popup("Ganaste", f"¡Felicidades! Has adivinado la palabra: {self.palabra_secreta}")
                self.iniciar_juego()
        else:
            self.intentos_restantes -= 1
            if self.intentos_restantes == 0:
                self.centrar_popup("Perdiste", f"¡Perdiste! La palabra secreta era: {self.palabra_secreta}")
                self.iniciar_juego()
        self.actualizar_pantalla()

    def centrar_popup(self, titulo, mensaje):
        # Crear un pop-up centrado
        popup = tk.Toplevel(self.root)
        popup.title(titulo)
        popup.geometry("300x100")

        # Centrar el pop-up en la ventana principal
        popup_x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 150
        popup_y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 50
        popup.geometry(f"+{popup_x}+{popup_y}")

        tk.Label(popup, text=mensaje, wraplength=250).pack(pady=10)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

def obtener_palabra_secreta(tematica):
    return random.choice(palabras_por_tematica[tematica])

if __name__ == "__main__":
    root = tk.Tk()
    juego = Ahorcado(root)
    root.mainloop()
