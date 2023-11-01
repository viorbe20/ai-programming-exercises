"""
V1. Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. 
- Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. 
- Si se introduce una opción incorrecta se muestra un mensaje de error. 
- El menú se volverá a mostrar, a menos que no se de a la opción terminar.
Author: Virginia Ordoño Bernier
Date: november 2023
"""

import time

num1 = num2 = ""

def add (a, b):
    result = a + b
    return result

def substract (a, b):
    result = a - b
    return result

def multiply (a, b):
    result = a * b
    return result

def divide (a, b):
    result = a / b
    return result

def show_menu():
    print ("\nOperaciones")
    print("-----------")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")
    print("5. Salir")

# Programm

print("\nEl siguiente programa te pedirá dos valores y hará diferentes operaciones con ellos.")


while True:
        
    if num1 == num2 == "":
    
        try:
            num1 = float(input("\nIntroduce el primer número: "))
            num2 = float(input("\nIntroduce el segundo número: "))
        
        except ValueError:
            print("\033c", end="")
            print("\nDebes introducir un número. Inténtalo de nuevo")
            time.sleep(2)

    show_menu()
    
    selected_option = ""
    
    # Check user´s selected option
    while selected_option not in [1,2,3,4,5]:
        
        try:
            selected_option = int(input("\nIntroduce un número del 1 al 4 para seleccionar la operación o 5 para salir: "))
        except ValueError:
            print("\nDebes introducir un número entre 1 y 5. Inténtalo de nuevo")

    # Selected option is correct
    match selected_option:
        case 1:
            print("\033c", end="")
            print(f"\nSuma: {num1} + {num2} = {add(num1,num2)}")
            time.sleep(2)
        case 2:
            print("\033c", end="")
            print(f"\nResta: {num1} - {num2} = {substract(num1,num2)}")
            time.sleep(2)
        case 3:
            print("\033c", end="")
            print(f"\nMultiplicación: {num1} * {num2} = {multiply(num1,num2)}")
            time.sleep(2)
        case 4:
            print("\033c", end="")
            print(f"\nDivisión: {num1} / {num2} = {divide(num1,num2)}")
            time.sleep(2)
        case 5:
            print("\033c", end="")
            print("\nEl programa ha finalizado.")
            exit(0)