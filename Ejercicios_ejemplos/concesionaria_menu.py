"""
Ejercicio: Registro de Automóviles en una Concesionaria

Descripción:
Escribe un programa en Python que permita a una concesionaria registrar automóviles, asignarles un valor y mostrar el listado de automóviles registrados. El programa debe usar diccionarios para almacenar la información de los automóviles y debe permitir al usuario realizar las siguientes acciones:

1. Registrar un nuevo automóvil.
2. Asignar un valor a un automóvil registrado.
3. Mostrar la lista de automóviles registrados.
4. Salir.

El programa debe:
1. Mostrar un menú con las opciones mencionadas.
2. Permitir al usuario seleccionar una opción.
3. Solicitar la información necesaria según la opción seleccionada.
4. Ejecutar la acción correspondiente y mostrar resultados.
5. Repetir el menú hasta que el usuario seleccione la opción de salir.
"""

def mostrar_menu():
    # Función que muestra el menú de opciones al usuario
    print("Menú de la Concesionaria")
    print("1. Registrar un nuevo automóvil")
    print("2. Asignar valor a un automóvil registrado")
    print("3. Mostrar lista de automóviles registrados")
    print("4. Salir")

def registrar_automovil(autos):
    # Función para registrar un nuevo automóvil
    # Solicita al usuario la marca, modelo y año del automóvil y lo agrega al diccionario 'autos'
    marca = input("Ingresa la marca del automóvil: ")
    modelo = input("Ingresa el modelo del automóvil: ")
    año = input("Ingresa el año del automóvil: ")
    autos[modelo] = {"marca": marca, "año": año, "valor": None}
    print(f"Automóvil {marca} {modelo} registrado exitosamente.")

def asignar_valor(autos):
    # Función para asignar un valor a un automóvil registrado
    # Solicita al usuario el modelo del automóvil y el valor a asignar, y actualiza el diccionario 'autos'
    modelo = input("Ingresa el modelo del automóvil al que quieres asignar un valor: ")
    if modelo in autos:
        try:
            valor = float(input("Ingresa el valor del automóvil: "))
            autos[modelo]["valor"] = valor
            print(f"Valor asignado al automóvil {modelo}: ${valor}")
        except ValueError:
            # Maneja la excepción si el usuario ingresa un valor no numérico
            print("Error: Entrada inválida. Por favor, ingresa un valor numérico.")
    else:
        # Mensaje de error si el modelo no está registrado
        print("Error: El modelo ingresado no está registrado.")

def mostrar_automoviles(autos):
    # Función para mostrar la lista de automóviles registrados
    # Recorre el diccionario 'autos' y muestra los detalles de cada automóvil
    if autos:
        print("Lista de Automóviles Registrados:")
        for modelo, detalles in autos.items():
            valor = detalles["valor"] if detalles["valor"] is not None else "No asignado"
            print(f"Marca: {detalles['marca']}, Modelo: {modelo}, Año: {detalles['año']}, Valor: {valor}")
    else:
        print("No hay automóviles registrados.")

def main():
    # Función principal que controla el flujo del programa
    autos = {}  # Diccionario para almacenar los automóviles registrados
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '4':
            # Salir del programa si el usuario selecciona la opción 4
            print("Saliendo del programa...")
            break

        if opcion == '1':
            registrar_automovil(autos)
        elif opcion == '2':
            asignar_valor(autos)
        elif opcion == '3':
            mostrar_automoviles(autos)
        else:
            # Mensaje de error si el usuario selecciona una opción no válida
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    main()
