"""
V1. Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. 
- Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. 
- Si se introduce una opción incorrecta se muestra un mensaje de error. 
- El menú se volverá a mostrar, a menos que no se dé a la opción terminar.

Author: Virginia Ordoño Bernier
Date: november 2023
"""
def main():

    print("\nEste programa te pedirá dos valores numéricos. Luego te mostrará un menú para que selecciones las operaciones que deseas realizar.")

    try:
        num1 = float(input("\nIntroduce el primer número: "))
        num2 = float(input("\nIntroduce el segundo número: "))

    except ValueError:
        print("\nDebes introducir un dato numérico")
        exit(1)

    selected_option = ''

    # Show menu
    while selected_option != 5:
        selected_option  = get_selected_option()
        get_operations(selected_option, num1, num2)
    
    print("\nEl programa ha finalizado.")
    exit(0)

def get_operations(selected_option, num1, num2):
    
    match(selected_option):
        case 1:
            print(f"\nSuma: {num1} + {num2} = {add(num1, num2)}")
        case 2:
            print(f"\nResta: {num1} - {num2} = {substract(num1, num2)}")
        case 3:
            print(f"\nMultiplicación: {num1} * {num2} = {multiply(num1, num2)}")
        case 4:
            if num2 == 0:
                print("El denominador no puede ser 0")
            else:
                print(f"\División: {num1} / {num2} = {divide(num1, num2)}")

def get_selected_option():
    
    print("\nElige una de las siguientes opciones:")
    print("\n1. Sumar")
    print("\n2. Restar")
    print("\n3. Multiplicar")
    print("\n4. Dividir")
    print("\n5. Terminar")

    # Validation input as integer 
    try:
        selected_option = int(input("\nIntroduce la opción: "))
    except ValueError:
        print(f"\nDebes introducir un número. El programa ha finalizado.\n")
        exit(1)

    # Validation input as in range
    if selected_option not in range(1, 6):
        print("\nLa opción debe estar en el rango de 1 a 5. El programa ha finalizado.\n")
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