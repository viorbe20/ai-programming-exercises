"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres. 
Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes. 
Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por pantalla, 
solo se debe usar print desde el programa principal.
Author: Virginia Ordoño Bernier
Date: november 2023
"""

NUMBER = 470213

def convert_to_pipe(num):
    pipe = "|"
    pipe_conversion = ""
    
    # Create a list of digits from the number
    digits = [int(n) for n in str(num)]

    # Iterate through the list of digits and construct the representation
    for digit in digits:
        pipe_conversion += pipe * digit + " - "

    # Remove last " - " and return the result
    return pipe_conversion[:-3]


# Main program
if __name__ == "__main__":
    print(convert_to_pipe(NUMBER))