"""
V1
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. 
- Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. 
- Si se introduce una opción incorrecta se muestra un mensaje de error. 
- El menú se volverá a mostrar, a menos que no se de a la opción terminar.

V2
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). 
- Las variables se inicializan a cero. Si no se introduce nada, hace las operaciones a 0.

Author: Virginia Ordoño Bernier
Date: november 2023
"""
import time

def main():
    
    num1 = num2 = 0

    print("\nEl siguiente programa te pedirá introducir en primer lugar dos valores. Luego podrás hacer diferentes operaciones con ellos.")
    print("Si no introduces ningún valor, por defecto los valores serán 0.")
    time.sleep(2)
    
    while True:
        selected_option = None

        show_menu()

        while selected_option not in [1,2,3,4,5,6]:
            try:
                selected_option = int(input("\nIntroduce un número entre 1 y 6 para seleccionar una opción: "))
            except ValueError:
                print("\033c", end="")
                print("\nDebes introducir un número. Inténtalo de nuevo")
                time.sleep(1)

        if selected_option == 1:
            
            try:
                num1 = float(input("\nIntroduce el primer número: "))
                num2 = float(input("\nIntroduce el segundo número: "))
                show_menu()
            except ValueError:
                print("\033c", end="")
                print("\nDebes introducir un número. Inténtalo de nuevo")
                time.sleep(1)
        
        elif int(selected_option) in range(2, 7):
            get_operation(int(selected_option), num1, num2)
        
        else:
            print("\033c", end="")
            print("\nOpción incorrecta. Inténtalo de nuevo.")
            time.sleep(1)

def show_menu():
    print("\nOpciones:")
    print("--------------")
    print("\n1. Introducir números")
    print("\n2. Sumar")
    print("\n3. Restar")
    print("\n4. Multiplicar")
    print("\n5. Dividir")
    print("\n6. Terminar")

def get_operation(selected_option, num1, num2):
    if selected_option == 2:
        print(f"\nSuma: {num1} + {num2} = {add(num1, num2)}")
        time.sleep(2)
    elif selected_option == 3:
        print(f"\nResta: {num1} - {num2} = {subtract(num1, num2)}")
        time.sleep(2)
    elif selected_option == 4:
        print(f"\nMultiplicación: {num1} * {num2} = {multiply(num1, num2)}")
        time.sleep(2)
    elif selected_option == 5:
        if num2 == 0:
            print("\033c", end="")
            print("\nError: No se puede dividir por cero.")
        else:
            print(f"\nDivisión: {num1} / {num2} = {divide(num1, num2)}")
        time.sleep(2)
    elif selected_option == 6:
        print("\033c", end="")
        print("\nEl programa ha finalizado.")
        exit(0)
    else:
        print("\033c", end="")
        print("\Opción incorrecta. Inténtalo de nuevo.")
        time.sleep(1)

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result if b != 0 else "Error: No se puede dividir por cero."

if __name__ == "__main__":
    main()