"""
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
Para hacer una espera en Python podemos usar el método sleep del módulo time.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
import time

print("\nA continuación, el programa mostrará un cronometro.")

start = input("\nPresione ENTER para iniciar el cronómetro: ")

if start == "":
    while True:        
        for hours in range(24):
            for minutes in range(60):
                for seconds in range(60):
                    print("\033c", end="") # Cleans terminal (escape sequence) and avoids to add a new line
                    print(f"Cronómetro: {hours:02d}:{minutes:02d}:{seconds:02d}") # If hours < 10 it writes 0
                    time.sleep(1)  # Wait 1 second