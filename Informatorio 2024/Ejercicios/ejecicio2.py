## Ejercicio 2: Suma de Números (For y Listas)
# Escribe un programa que solicite al usuario 5 números distintos y los almacene en una lista. 
# Luego, calcula y muestra la suma de todos los números en la lista.

numeros = []
print("ingresa 5 números distintos:")

for i in range(5):
    num = float(input(f"Ingresa el número {i + 1}: "))
    while num in numeros:
        print("El número ya ha sido ingresado. Ingresa un número distinto.")
        num = float(input(f"Ingresa el número {i + 1} nuevamente: "))
    numeros.append(num)

suma_total = sum(numeros)
print(f"La suma de los números  es: {suma_total}")

