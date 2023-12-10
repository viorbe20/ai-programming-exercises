"""
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
- La suma de los números que están dentro del intervalo (intervalo abierto).
- Cuantos números están fuera del intervalo.
- Informa si hemos introducido algún número igual a los límites del intervalo.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

interval_numbers = []
outside_interval_amount = 0
num1_equal_amount = 0
num2_equal_amount = 0

print("\nA continuación, el programa te dará diferentes datos sobre un intervalo de números. Sigue las instrucciones.")

while True:
    try:
        num1 = int(input("\nIntroduce el número que será el límite inferior del intervalo: "))
        num2 = int(input("\nIntroduce el número que será el límite superior del intervalo: "))
        break  
    except ValueError:
        print("\nIntroduce un número válido.")

# If num1 is bigger than num2, ask for number 2 again

while num1 > num2:
    num2 = int(input("\nIntroduce el número que será el límite superior del intervalo: "))


# Ask for numbers until we introduce the 0

while True:
    try:
        number = int(input("\nIntroduce 0 para salir del programa o cualquier otro número dentro o fuera del intervalo: "))
        
        if number == 0:
            break
        
        # Numbers equal to limits
        if number == num1:
            num1_equal_amount += 1
        elif number == num2:
            num2_equal_amount += 1

        # Numbers inside and outside interval
        if number >= num1 and number <= num2:
            interval_numbers.append(number)
        else:
            outside_interval_amount += 1
    except ValueError:
        print("\nIntroduce un número válido.")

print("\nResultados:")
print("----------------")
print("\nSuma de los números dentro del intervalo: ", sum(interval_numbers))
print("\nCantidad de números fuera del intervalo: ", outside_interval_amount) 
print ("\nCantidad de números igual al límite inferior: ", num1_equal_amount)
print ("\nCantidad de números igual al límite superior: ", num2_equal_amount)
print("\n")