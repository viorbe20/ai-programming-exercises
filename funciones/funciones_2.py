"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. 
Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, 
si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo. 
Por ejemplo, la función is_palindromic() resulta trivial teniendo turn() 
y la función next_prime() también es muy fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversión del número a una cadena.

- is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
- next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- digits: devuelve el número de dígitos de un número entero.
- turn: le da la vuelta a un número.
- digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
- digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
- remove_behind: le quita a un número n dígitos por detrás (por la derecha).
- remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
- paste_behind: añade un dígito a un número por detrás.
- paste_ahead: añade un dígito a un número por delante.
- piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
- put_numbers_together: pega dos números para formar uno.

Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.
Author: Virginia Ordoño Bernier
Date: november 2023
"""
from colorama import init, Fore

init()

REVERSE_NUMBER = 123
PALINDROMIC_NUMBER_1 = 1231
PALINDROMIC_NUMBER_2 = 1221
PRIME_NUMBER_1 = 13
PRIME_NUMBER_2 = 20
NEXT_PRIME_NUMBER = 19
DIGITS_AMOUNT = 123456
DIGIT_N_SEQUENCE = 6789
DIGIT_N_POSITION_A = 0
DIGIT_N_POSITION_B = 2
DIGIT_N_POSITION_C = 20
DIGIT_POSITION_SEQUENCE = 66366636
DIGIT_POSITION_NUMBER_A = 3
DIGIT_POSITION_NUMBER_B = 9
REMOVE_AHEAD_SEQUENCE = 123456
REMOVE_AHEAD_DELETE = 2
REMOVE_BEHIND_SEQUENCE = 123456
REMOVE_BEHIND_DELETE = 2
PASTE_BEHIND_SEQUENCE = 4444
PASTE_BEHIND_DIGIT = 9
PASTE_AHEAD_SEQUENCE = 3333
PASTE_AHEAD_DIGIT = 5
PIECE_NUMBER_SEQUENCE = 24442
PIECE_NUMBER_FIRST_POSITION = 1 
PIECE_NUMBER_LAST_POSITION = 4
PASTE_NUMBERS_TOGETHER_1 = 333
PASTE_NUMBERS_TOGETHER_2= 666


# Append a digit to the end of a number.
def paste_behind(sequence, digit):
    return sequence * 10 + digit 

# Reverse the order of digits in a number.
def turn(number):
    reversed_number = 0
    remaining_number = abs(number)  # Absolute value to handle negative numbers

    while remaining_number > 0:
        last_digit = remaining_number % 10
        #reversed_number = reversed_number * 10 + last_digit
        reversed_number = paste_behind(reversed_number, last_digit)
        remaining_number = remaining_number // 10  # Remove the last digit
        
    # If the original number was negative, the reversed number will be negative too
    return -reversed_number if number < 0 else reversed_number 

# Prepend a digit to the beginning of a sequence of numbers.
def paste_ahead(sequence, digit):

    reversed_sequence = turn(sequence)

    pasted_sequence = paste_behind(reversed_sequence, digit)

    return turn(pasted_sequence)

# Check if a number is palindromic
def is_palindromic(number):
    if (number == turn(number)):
        return ("Es palíndromo")
    else:
        return ("No es palíndromo")

# Check if a number is prime.
def is_prime(number):
    
    if number <= 1:
        result = "No es primo"
    
    if number == 2:
        result = "Es primo"

    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                result = "No es primo"
                break
            else:
                result = "Es primo"
                
    return result 

# Find the next prime number, greater than the given number.
def next_prime(number):
    number += 1
    while is_prime(number) == "No es primo":
        number += 1
    return number

# Calculate the number of digits in an integer.
def digits(number):

    if number == 0:
        return 1

    number = abs(number)
    digits_amount = 0
    while number > 0:
        number = number // 10 # Deletes the last 
        digits_amount += 1
        
    return digits_amount

# Get the digit at position n, included in a number sequence 
def digit_n(sequence, position):

    reversed_sequence = turn(sequence)
    pointer = 0

    while pointer < position:
        reversed_sequence = reversed_sequence // 10
        pointer += 1
        
    if reversed_sequence > 0:
        return reversed_sequence % 10
    else:
        return None

# Find the position of the first occurrence of a digit in a number.
def digit_position(sequence, digit):
    
    reversed_sequence = turn(sequence)
    pointer = 0

    while reversed_sequence > 0:
        last_digit = reversed_sequence % 10
        if last_digit == digit:
            return pointer
        reversed_sequence = reversed_sequence // 10
        pointer += 1
        
    return -1

# Remove an amount of digits from the end of a sequence of number.
def remove_behind(sequence, amount):
    
    for _ in range(amount):
        sequence = sequence // 10
    
    return sequence

# Remove an amount of digits from the head of a sequence of number.
def remove_ahead(sequence, amount):
    
    reversed_sequence = turn(sequence)

    result = remove_behind(reversed_sequence, amount)
    
    return turn(result)

# With first and last positions, return a portion of a sequence of numbers.
def piece_of_number(sequence, first_position, last_position):
    
    reversed_sequence = turn(sequence)
    pointer = 0
    result = 0  
    last_position += 1

    while pointer < last_position:
        digit = reversed_sequence % 10  # Get last digit of reversed_sequence
        if pointer >= first_position:
            result = paste_ahead(result, digit)  # Add digit to result if we are inside the range
        reversed_sequence //= 10  # Delete last digit of reversed_sequence
        pointer += 1 # Go to next digit

    return turn(result)

# Paste two numbers to form one.
def put_numbers_together(number1, number2):
    
    reversed_number1 = turn(number1)
    reversed_number2 = turn(number2) 

    while reversed_number2 > 0:
        last_digit = reversed_number2 % 10  # Get last digit of reversed_number2
        reversed_number1 = paste_ahead(reversed_number1, last_digit)
        reversed_number2 //= 10  # delete last digit of reversed_number2

    return turn(reversed_number1)

# Testing

print(Fore.GREEN + "\nFunción: dar la vuelta a un número" + Fore.WHITE)
print(f"Número {REVERSE_NUMBER}. Resultado => ", turn(REVERSE_NUMBER))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: comprobar si un número es palíndromo" + Fore.WHITE)
print(f"Número {PALINDROMIC_NUMBER_1}. Resultado => ", is_palindromic(PALINDROMIC_NUMBER_1))
print(f"Número {PALINDROMIC_NUMBER_2}. Resultado => ", is_palindromic(PALINDROMIC_NUMBER_2))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: comprobar si un número es primo" + Fore.WHITE)
print(f"Número {PRIME_NUMBER_1}. Resultado => ", is_prime(PRIME_NUMBER_1))
print(f"Número {PRIME_NUMBER_2}. Resultado => ", is_prime(PRIME_NUMBER_2))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: encontrar el siguiente número primo" + Fore.WHITE)
print(f"Número {NEXT_PRIME_NUMBER}. Resultado => ", next_prime(NEXT_PRIME_NUMBER))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: calcular el número de dígitos de un número" + Fore.WHITE)
print(f"Número {DIGITS_AMOUNT}. Resultado => ", digits(DIGITS_AMOUNT))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: obtener un dígito dada la posición, en una secuencia de números " + Fore.WHITE)
print(f"Número entero: {DIGIT_N_SEQUENCE}. Posición: {DIGIT_N_POSITION_A}. Número obtenido  => ", digit_n(DIGIT_N_SEQUENCE, DIGIT_N_POSITION_A))
print(f"Número entero: {DIGIT_N_SEQUENCE}. Posición: {DIGIT_N_POSITION_B}. Número obtenido => ", digit_n(DIGIT_N_SEQUENCE, DIGIT_N_POSITION_B))
print(f"Número entero: {DIGIT_N_SEQUENCE}. Posición: {DIGIT_N_POSITION_C}. Número obtenido => ", digit_n(DIGIT_N_SEQUENCE, DIGIT_N_POSITION_C))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: obtener la posición de un dígito, en una secuencia de números" + Fore.WHITE)
print(f"Número entero: {DIGIT_POSITION_SEQUENCE}. Dígito: {DIGIT_POSITION_NUMBER_A}. Posición obtenida => ", digit_position(DIGIT_POSITION_SEQUENCE, DIGIT_POSITION_NUMBER_A))
print(f"Número entero: {DIGIT_POSITION_SEQUENCE}. Dígito: {DIGIT_POSITION_NUMBER_B}. Posición obtenida => ", digit_position(DIGIT_POSITION_SEQUENCE, DIGIT_POSITION_NUMBER_B))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: eliminar un número de dígitos por delante de una secuencia de números" + Fore.WHITE)
print(f"Número entero: {REMOVE_AHEAD_SEQUENCE}. Cantidad de dígitos a eliminar: {REMOVE_AHEAD_DELETE}. Resultado => ", remove_ahead(REMOVE_AHEAD_SEQUENCE, REMOVE_AHEAD_DELETE))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: eliminar un número de dígitos por detrás de una secuencia de números" + Fore.WHITE)
print(f"Número entero: {REMOVE_BEHIND_SEQUENCE}. Cantidad de dígitos a eliminar: {REMOVE_BEHIND_DELETE}. Resultado => ", remove_behind(REMOVE_BEHIND_SEQUENCE, REMOVE_BEHIND_DELETE))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: insertar un dígito por delante de una secuencia de números" + Fore.WHITE)
print(f"Número entero: {PASTE_AHEAD_SEQUENCE}. Dígito a insertar: {PASTE_AHEAD_DIGIT}. Resultado => ", paste_ahead(PASTE_AHEAD_SEQUENCE, PASTE_AHEAD_DIGIT))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: insertar un dígito por detrás de una secuencia de números" + Fore.WHITE)
print(f"Número entero: {PASTE_BEHIND_SEQUENCE}. Dígito a insertar: {PASTE_BEHIND_DIGIT}. Resultado => ", paste_behind(PASTE_BEHIND_SEQUENCE, PASTE_BEHIND_DIGIT))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: dada una secuencia de números, una posición inicial y una posición final, devuelve el intervalo correspondiente" + Fore.WHITE)
print(f"Secuencia: {PIECE_NUMBER_SEQUENCE}. Posición inicial: {PIECE_NUMBER_FIRST_POSITION}. Posición final: {PIECE_NUMBER_LAST_POSITION}. Resultado => ", piece_of_number(PIECE_NUMBER_SEQUENCE, PIECE_NUMBER_FIRST_POSITION, PIECE_NUMBER_LAST_POSITION))
print("\n--------------------------------------")

print(Fore.GREEN + "\nFunción: pegar dos números para formar uno" + Fore.WHITE)
print(f"Número entero: {PASTE_NUMBERS_TOGETHER_1}. Número entero: {PASTE_NUMBERS_TOGETHER_2}. Resultado => ", put_numbers_together(PASTE_NUMBERS_TOGETHER_1, PASTE_NUMBERS_TOGETHER_2))
print("\n--------------------------------------")