"""
Ejercicio: Menú de Operaciones Matemáticas

Descripción:
Escribe un programa en Python que muestre un menú con varias opciones de operaciones matemáticas básicas. El usuario podrá seleccionar la operación que desea realizar, ingresar los números necesarios, y el programa mostrará el resultado de la operación seleccionada. El menú debe incluir al menos las siguientes operaciones:

1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir

El programa debe:
1. Mostrar el menú de operaciones.
2. Permitir al usuario seleccionar una operación.
3. Pedir al usuario que ingrese los números necesarios para la operación seleccionada.
4. Realizar la operación y mostrar el resultado.
5. Repetir el menú hasta que el usuario seleccione la opción de salir.
"""

def mostrar_menu():
    print("Menú de Operaciones Matemáticas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Saliendo del programa...")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == '1':
                    print(f"Resultado de la suma: {suma(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado de la resta: {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado de la multiplicación: {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado de la división: {division(num1, num2)}")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingresa números válidos.")
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()
