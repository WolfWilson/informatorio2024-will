"""
Juego del Ahorcado

Descripción:
Este programa implementa el juego del ahorcado. 
El usuario puede elegir entre varias temáticas de palabras, e intentar adivinar una palabra secreta en un número limitado de intentos. 
El programa incluye las siguientes funcionalidades:
1. Iniciar un nuevo juego.
2. Reintentar el juego después de perder.
3. Salir del programa.

El juego permite:
1. Seleccionar una temática.
2. Generar una palabra aleatoria de la temática seleccionada (tomada desde el diccionario correspondiente a la tematica)
3. Informar al usuario que tiene 5 intentos para adivinar la palabra.
4. Mostrar el progreso del usuario en la adivinanza (letras adivinadas y guiones bajos).
5. Finaliza el juego cuando se adivina la palabra o se agotan los intentos.
"""

import random

# Diccionarios de palabras por temáticas (unos 20 a 30 valores para elegir aleatoriamente)
palabras_por_tematica = {
    "Frutas": ["manzana", "banana", "naranja", "pera", "uva", "mango", "limon", "kiwi", "sandia", "melon", 
               "fresa", "cereza", "ciruela", "durazno", "granada", "higo", "papaya", "piña", "frambuesa", 
               "grosella", "arándano", "mandarina", "pomelo", "guayaba", "lichi"],

    "Utensilios de cocina": ["cuchillo", "tenedor", "cuchara", "sarten", "olla", "colador", "batidora", 
                             "licuadora", "tostadora", "cafetera", "tetera", "rallador", "cacerola", "espumadera", 
                             "abrelatas", "pinzas", "mortero", "rodillo", "espátula", "cucharon", "cuchillo", 
                             "pelador", "tabla", "vaso", "plato"],

    "Paises": ["argentina", "brasil", "canada", "dinamarca", "egipto", "francia", "republica checha", "hungria", 
               "india", "japon", "kenia", "libano", "mexico", "nepal", "alemania", "portugal", "qatar", 
               "rusia", "suecia", "turquia", "uruguay", "vietnam", "yemen", "zambia", "zimbabwe"],

    "Palabras reservadas en Python": ["False", "None", "True", "and", "as", "assert", "async", "await", 
                                      "break", "class", "continue", "def", "del", "elif", "else", "except", 
                                      "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", 
                                      "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
}

def mostrar_menu():
    # funcion para mostrar menú principal
    print("Menú del Juego del Ahorcado")
    print("1. Comenzar a jugar/reintentar")
    print("2. Salir")

def seleccionar_tematica(): #no es necesario el return, devuelve el valor de la variable opcion
    # función para que el  usuario seleccione una temática de palabras
    print("Seleccione una temática:")
    print("1. Frutas")
    print("2. Utensilios de cocina")
    print("3. Paises")
    print("4. Palabras reservadas en Python")

    while True:
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            return "Frutas"
        elif opcion == '2':
            return "Utensilios de cocina"
        elif opcion == '3':
            return "Paises"
        elif opcion == '4':
            return "Palabras reservadas en Python"
        else:
            print("Opción no válida. Intente de nuevo.")


def obtener_palabra_secreta(tematica):
    # devuelve con el return  una palabra secreta aleatoria de la temática seleccionada (random.choice(nombre del diccionario[variable que contiene el valor de la función de selección de tematica]))
    return random.choice(palabras_por_tematica[tematica])

def jugar():
    # Función principal del juego del ahorcado
    tematica = seleccionar_tematica()#Asigno a la variable tematica la elección del usuario a travez de la función seleccionar_tematica()
    palabra_secreta = obtener_palabra_secreta(tematica).lower() #recibe la elección random de la funcion obtener_palabra_secreta () lower lo pone todo en minúsculas
    intentos_restantes = 5
    letras_adivinadas = set()
    progreso = ["_"] * len(palabra_secreta)

    while intentos_restantes > 0:
        print(f"\nIntentos restantes: {intentos_restantes}")
        print("Progreso: " + " ".join(progreso))
        letra = input("Ingrese una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)#agrega la letra adivinada al conjunto para que se muestre por pantalla y se pueda comparar con otras que se ingresan

        if letra in palabra_secreta:
            for i, char in enumerate(palabra_secreta):
                if char == letra:
                    progreso[i] = letra
            if "_" not in progreso:
                print(f"\n¡Felicitaciones! ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧ Has adivinado la palabra: {palabra_secreta}")
                return
        else:
            intentos_restantes -= 1
            print("Letra incorrecta.")
    
    print(f"\nPerdiste! ¯\_(ツ)_/¯ . La palabra secreta era: {palabra_secreta}")

def main():    # Función principal del programa

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            jugar()
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
