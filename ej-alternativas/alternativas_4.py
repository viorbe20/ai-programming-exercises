"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla 
el mensaje «Es signo de puntuación» solo si el carácter leído es un signo de puntuación, 
«Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada), 
«Es un dígito» si es un dígito, 
«Es otro carácter» si no es ninguno de los anteriores y 
«No es un carácter» si el usuario ha introducido más de un carácter. 
Pista: quizás te pueda venir bien usar el método find de la clase str.
string.punctuation es un módulo con los signos de puntuación
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación el programa te pedirá que introduzcas un carácter de teclado para determinar el tipo de carácter.\n")

# Ask character and strip blank spaces
char = input("\nIntroduce un carácter: ").strip()

if len(char) != 1: # Check character's length
    print("\nNo es un carácter.")
    exit()
else:
    if ",.;:'¡!¿?-_()[]{/}\*&#%$+=><".find(char) != -1:
        print("\nEs un signo de puntuación")
    elif char.isalpha():
        print("\nEs una letra")
    elif char.isdigit():
        print("\nEs un dígito")
    else:
        print("\nEs otro carácter") 