"""
V1. Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
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

def main():

    num1 = 0
    num2 = 0

    print("\nEste programa te pedirá dos valores numéricos. Si no los introduces su valor será 0.") 
    print("Luego te mostrará un menú para que selecciones las operaciones que deseas realizar.")

    selected_option = ''

    while True:
    # Show menu
        selected_option  = get_selected_option()
        
        # Select exit programm
        if selected_option == 6:
            print("\nEl programa ha finalizado.")
            exit(0)
        
        # Select option 1
        if selected_option == 1:
            try:
                num1 = float(input("\nIntroduce el primer número: "))
                num2 = float(input("\nIntroduce el segundo número: "))

            except ValueError:
                print("\nDebes introducir un dato numérico. El programa ha finalizado")
                exit(1)
        
        get_operations(selected_option, num1, num2)

def get_operations(selected_option, num1, num2):
    
    match(selected_option):
        case 2:
            print(f"\nSuma: {num1} + {num2} = {add(num1, num2)}")
        case 3:
            print(f"\nResta: {num1} - {num2} = {substract(num1, num2)}")
        case 4:
            print(f"\nMultiplicación: {num1} * {num2} = {multiply(num1, num2)}")
        case 5:
            if num2 == 0:
                print("\nEl denominador no puede ser 0")
            else:
                print(f"\División: {num1} / {num2} = {divide(num1, num2)}")

def get_selected_option():
    
    print("\nElige una de las siguientes opciones:")
    print("\n1. Introducir las variables")
    print("\n2. Sumar")
    print("\n3. Restar")
    print("\n4. Multiplicar")
    print("\n5. Dividir")
    print("\n6. Terminar")

    # Validation input as integer 
    try:
        selected_option = int(input("\nIntroduce la opción: "))
    except ValueError:
        print(f"\nDebes introducir un número. El programa ha finalizado.\n")
        exit(1)

    # Validation input as in range
    if selected_option not in range(1, 7):
        print("\nLa opción debe estar en el rango de 1 a 6. El programa ha finalizado.\n")
        exit(1)
    
    return selected_option

def add (a, b):
    return a + b

def substract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

if __name__ == "__main__":
    main()