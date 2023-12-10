"""
Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. 
Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa te pedirá que introduzcas una cantidad de dinero y calculará en desglose mñinimo en billetes")

# Ask for a year
try:
    amount = float(input("\nIntroduce una cantidad de dinero: "))
    decimal = amount - int(amount)
except ValueError: 
    print("\nEl valor introducido no es válido.")
    exit(1)

notes_500 = notes_200 = notes_100 = notes_50 = notes_20 = notes_10 = notes_5 = coins_2 = coins_1 = 0

# Compare to 500_notes
if amount >= 500:
    notes_500 = int(amount // 500) # Show quantity of 500_notes
    amount %= 500 # Saves the rest of the amount

if amount >= 200:
    notes_200 = int(amount // 200)
    amount %= 200 
    
if amount >= 100:
    notes_100 = int(amount // 100) 
    amount %= 100 
    
if amount >= 50:
    notes_50 = int(amount // 50)
    amount %= 50 
    
if amount >= 20:
    notes_20 = int(amount // 20) 
    amount %= 20 
    
if amount >= 10:
    notes_10 = int(amount // 10) 
    amount %= 10 
    
if amount >= 5:
    notes_5 = int(amount // 5) 
    amount %= 5 
    
if amount >= 2:
    coins_2 = int(amount // 2) 
    amount %= 2 
    
if amount >= 1:
    coins_1 = int(amount // 1) 
    amount %= 1 
    
# Show the result

print("\nEl desglose mínimo es: \n")

if notes_500 > 0:
    print(f"{notes_500} billetes de 500€")
    
if notes_200 > 0:
    print(f"{notes_200} billetes de 200€")
    
if notes_100 > 0:
    print(f"{notes_100} billetes de 100€")
    
if notes_50 > 0:
    print(f"{notes_50} billetes de 50€")
    
if notes_20 > 0:
    print(f"{notes_20} billetes de 20€")
    
if notes_10 > 0:
    print(f"{notes_10} billetes de 10€")
    
if notes_5 > 0:
    print(f"{notes_5} billetes de 5€")
    
if coins_2 > 0:
    print(f"{coins_2} monedas de 2€")
    
if coins_1 > 0:
    print(f"{coins_1} monedas de 1€")
    print(f"Y {decimal} centimos")

if decimal != 0.0:
    decimal = round(decimal, 2)
    print(f"Y {decimal} centimos")


    











































