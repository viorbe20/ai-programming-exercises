"""
Mostrar en pantalla los N primeroS número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("\nA continuación, el programa te mostrará la cantidad de númeors primos que le indiques.")

amount_prime_numbers = ""

while  amount_prime_numbers == "":
    try:
        amount_prime_numbers = int (input("\nIndica cuantos números primos quieres mostrar: "))
    except ValueError:
        print("\nValor incorrecto. Debes introducir un número entero.")

print("\nA continuación, te mostrará los", amount_prime_numbers, "primeros números primos:\n")

# Iterates and prints the prime numbers
for i in range (amount_prime_numbers):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        print(i, end = ", ")