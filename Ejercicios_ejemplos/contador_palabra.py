"""
Ejercicio: Análisis de Texto

Descripción:
Escribe un programa en Python que permita ingresar un texto y devuelva la siguiente información:
1. La cantidad de veces que aparecen vocales en el texto.
2. La cantidad de veces que aparecen consonantes en el texto.
3. Las palabras más repetidas en el texto y su cantidad de apariciones.
4. La cantidad total de caracteres en el texto.

El programa debe:
1. Solicitar al usuario que ingrese un texto.
2. Analizar el texto para obtener la información solicitada.
3. Mostrar los resultados del análisis.
"""

def contar_vocales(texto):
    # Función para contar las vocales en el texto
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    return sum(1 for char in texto if char in vocales)

def contar_consonantes(texto):
    # Función para contar las consonantes en el texto
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in texto if char in consonantes)

def palabras_mas_repetidas(texto):
    # Función para encontrar las palabras más repetidas en el texto
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    max_frecuencia = max(frecuencia.values(), default=0)
    
    if max_frecuencia > 1:
        palabras_repetidas = {palabra: freq for palabra, freq in frecuencia.items() if freq == max_frecuencia}
    else:
        palabras_repetidas = {}
    
    return palabras_repetidas

def main():
    # Función principal que controla el flujo del programa
    texto = input("Ingresa un texto: ")

    # Cantidad total de caracteres en el texto
    total_caracteres = len(texto)

    # Cantidad de vocales en el texto
    num_vocales = contar_vocales(texto)

    # Cantidad de consonantes en el textohola 
    num_consonantes = contar_consonantes(texto)

    # Palabras más repetidas en el texto
    palabras_repetidas = palabras_mas_repetidas(texto)

    # Mostrar los resultados del análisis
    print(f"Cantidad total de caracteres: {total_caracteres}")
    print(f"Cantidad de vocales: {num_vocales}")
    print(f"Cantidad de consonantes: {num_consonantes}")
    if palabras_repetidas:
        print("Las palabras más repetidas y sus apariciones son:")
        for palabra, frecuencia in palabras_repetidas.items():
            print(f"'{palabra}': {frecuencia} veces")
    else:
        print("Todas las palabras aparecen una sola vez")

if __name__ == "__main__":
    main()
