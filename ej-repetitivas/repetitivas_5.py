"""
Una persona adquirió un producto para pagar en 20 meses. 
El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

MONTHLY_INCREASE = 2
total_amount = 0

print("\nA continuación, el programa determinará cuánto debe pagar una persona por un producto mensualmente y el total de lo que pagará después de los 20 meses.")

for i in range(1, 21):
    total_amount += 10 * MONTHLY_INCREASE ** (i - 1)
    
    # Monthly price 
    formatted_monthly_price = '{:,}'.format(10 * MONTHLY_INCREASE ** (i - 1)).replace(',', '.')
    print("--------------------")
    print(f"Mes {i} | {formatted_monthly_price} €.")

print("----------------")

# Total format
formatted_total = '{:,}'.format(total_amount).replace(',', '.')

print(f"\nEl total a pagar después de los 20 meses es de {formatted_total} €.\n")