"""
Mostrar en pantalla los N primeroS número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("\nA continuación, el programa te mostrará la cantidad de números primos que le indiques.")

amount_prime_numbers = ""

while  amount_prime_numbers == "":
    try:
        amount_prime_numbers = int (input("\nIndica cuantos números primos quieres mostrar: "))
    except ValueError:
        print("\nValor incorrecto. Debes introducir un número entero.")

print("\nA continuación, te mostrará los", amount_prime_numbers, "primeros números primos:\n")


if (amount_prime_numbers <= 0):
    print("No se puede mostrar ningún número primo.")
else:
    pass