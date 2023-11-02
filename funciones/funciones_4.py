"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres. 
Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.
Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.
Los números en Morse los puedes encontrar aquí: https://morsecw.com/alfabeto.html#numeros
Author: Virginia Ordoño Bernier
Date: november 2023
"""
NUMBER = 213

def morse_conversion(num):

    morse_numbers = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    
    # Create a list of digits from the number
    digits_list = [int(n) for n in str(num)]
    morse_result = "" 

    for digit in digits_list:
        morse_result += morse_numbers[str(digit)] + " "  # Concatenate the Morse representation of the digit

    return morse_result 

# Main program
if __name__ == "__main__":
    print(morse_conversion(NUMBER))