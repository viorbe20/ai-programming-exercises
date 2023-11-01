"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. 
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\n A continuación el programa te pedirá la edad de dos personas y determinará quién es más joven")

# Ask and check age of person 1
age1 = input("\nIntroduce la primera edad: ")

try:
    age1 = int(age1)
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit()
if age1 < 0 or age1 > 120:
    print("\nEl valor introducido no es válido.")
    exit()

# Ask and check age of person 2
age2 = input("\nIntroduce la segunda edad: ")
try:
    age2 = int(age2)
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit()
if age2 < 0 or age2 > 120:
    print("\nEl valor introducido no es válido.")
    exit()

# Result
if age1 == age2:
    print("\nTienen la misma edad.") 
elif age1 < age2:
    print("\nLa primera persona es más joven que la segunda.")
else:
    print("\nLa segunda persona es más joven que la primera.")