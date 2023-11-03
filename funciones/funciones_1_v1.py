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

def main():

    print("\nEl siguiente programa te pedirá dos valores y hará diferentes operaciones con ellos.")

    num1 = num2 = None
    
    while True:

        if (num1 == None) or (num2 == None):

            try:
                num1 = float(input("\nIntroduce el primer número: "))
                num2 = float(input("\nIntroduce el segundo número: "))

                show_menu(num1, num2)

            except ValueError:
                print("\033c", end="")
                print("\nDebes introducir un número. Inténtalo de nuevo")
                time.sleep(1)
        else: 
            show_menu(num1, num2)

def show_menu(num1, num2):
    
    print("\nElige una de las siguientes opciones:")
    print("\n1. Sumar")
    print("\n2. Restar")
    print("\n3. Multiplicar")
    print("\n4. Dividir")
    print("\n5. Terminar")
    
    selected_option = int(input("\nIntroduce la opción: "))
    
    if selected_option == 1:
        print(f"\nSuma: {num1} + {num2} = {add(num1,num2)}")
        time.sleep(2)
    elif selected_option == 2:
        print(f"\nResta: {num1} - {num2} = {substract(num1,num2)}")
        time.sleep(2)
    elif selected_option == 3:
        print(f"\nMultiplicación: {num1} * {num2} = {multiply(num1,num2)}")
        time.sleep(2)
    elif selected_option == 4:
        print(f"\nDivisión: {num1} / {num2} = {divide(num1,num2)}")
        time.sleep(2)
    elif selected_option == 5:
        print("\033c", end="")
        print("\nEl programa ha finalizado.")
        exit(0)
    else:
        print("\033c", end="")
        print("\nOpción incorrecta. Inténtalo de nuevo.")
        time.sleep(1)
        
    
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

if __name__ == "__main__":
    main()