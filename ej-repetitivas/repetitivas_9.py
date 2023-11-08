"""
Introducir una cadena de caracteres e indicar si es un palíndromo. 
Una palabra palíndroma es aquella que se lee igual adelante que atrás. No se pueden usar slices..
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("\nA continuación, el programa te indicará si la palabra introducida es un palíndromo.")

user_string = input("\nIntroduce  la cadena: ")

# Iterates through half of the string and compares each character with the corresponding character in the other half of the string.

for i in range(len(user_string) // 2):
    
    if user_string[i] != user_string[-i - 1]:
        print("\nLa cadena no es un palíndromo.")
        break
else:
    print("\nLa cadena es un palíndromo.")

# V2. cadena[::-1]es la cadena al reves