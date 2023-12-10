"""
Realizar un programa que compruebe si una cadena contiene una subcadena. 
Las dos cadenas se introducen por teclado. No se pueden usar los métodos de Python para este fin ni slices.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("\nA continuación, el programa te indicará si una cadena contiene una subcadena.")

string = input("\nIntroduce la cadena: ")
substring = input("Introduce la subcadena: ")


for i in range(len(string) - len(substring) + 1): # (len(string) - len(substring) + 1) == last index where it is possible to find substring
    
    match = True
    
    for j in range(len(substring)): # iterates through the substring 
        
        if string[i + j] != substring[j]:  # compares the characters of the substring with the characters of the string
            match = False
            break
    
    if match == True:
        print("La cadena contiene la subcadena.")
        break
    
else:
    print("La cadena no contiene la subcadena.")