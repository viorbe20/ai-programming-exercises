"""
V1. Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. 
- Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. 
- Si se introduce una opción incorrecta se muestra un mensaje de error. 
- El menú se volverá a mostrar, a menos que no se de a la opción terminar.

V2
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). 
- Las variables se inicializan a cero. Si no se introduce nada, hace las operaciones a 0.

V3
Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente 
no se puedan ejecutar el resto de las opciones. a y b no se inicializan a cero.

Author: Virginia Ordoño Bernier
Date: november 2023
"""
def main():

    print("\nEl siguiente programa te pedirá introducir en primer lugar dos valores. Luego podrás hacer diferentes operaciones con ellos.")

    option_1_selected = False

    while True:
        show_menu()
        
        selected_option = get_selected_option()

        if selected_option == 1:
            num1, num2 = get_numbers()
            option_1_selected = True

        # Mandatory chose option 1 first 
        while selected_option != 1 and option_1_selected == False:
            print("\nPrimero debes introducir los valores. Pulsa 1.")
            selected_option = get_selected_option()
        
        if not option_1_selected and (selected_option != 1 and selected_option != 6):
            print("\nNo se pueden realizar operaciones sin introducir los valores de A y B.")
            continue


        match (selected_option):
            case 2:
                print(f"\n2. Suma: {num1} + {num2} = {add(num1, num2)}")
            case 3:
                print(f"\n3. Resta: {num1} - {num2} = {substract(num1, num2)}")
            case 4:
                print(f"\n4. Multiplicación: {num1} * {num2} = {multiply(num1, num2)}")
            case 5:
                if num2 == 0:
                    print("\nEl divisor no puede ser 0")
                else:
                    print(f"\n5. División: {num1} / {num2} = {divide(num1, num2)}")
            case 6:
                print("\nEl programa ha finalizado.")
                exit(0)

def get_numbers(): 
    
    while True:
        try:
            num1 = float(input("\nIntroduce el primer número: "))
            num2 = float(input("\nIntroduce el segundo número: "))
            break
        except ValueError:
            print(f"\nDebes introducir un número. Inténtalo de nuevo")
    
    return num1, num2

def show_menu():
    print("\nMenú de Operaciones")
    print("----------------------")
    print("1. Introducir los números")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Terminar")
    print("----------------------")

def get_selected_option():
    
    while True:
        try:
            selected_option = int(input("\nIntroduce la opción: "))

            if selected_option in range(1, 7):
                break
            else:
                print("\nEl número debe estar comprendido entre 1 y 6. Inténtalo de nuevo.")
        except ValueError:
            print(f"\nDebes introducir un número. Inténtalo de nuevo")
    
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