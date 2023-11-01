"""
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, 
los siguientes tres, 80 céntimos por minuto, 
los siguientes dos minutos, 70 céntimos por minuto, 
y a partir del décimo minuto, 50 céntimos por minuto. 
Además, se carga un impuesto de 3% cuando es domingo, 
y si es otro día, en turno de mañana, 15%, 
y en turno de tarde, 10%. 
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa determinará el pago que debes hacer a la compañía telefónica.")

try:
    total_minutes = int(input("\nIntroduce la cantidad de tiempo en minutos: "))
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit(1)

# Check if the day is a sunday
day = input("\nIntroduce 1 si el día de la llamada fue domingo. Si el día de la llamada fue otro día introduce cualquier otro carácter: ")

# If not Sunday, check shift 
if day != 1:
    sunday_tax_percent = 1
    shift = input("\nIntroduce 1 si el turno fue mañana u otro carácter si el turno fue tarde: ")
    if shift == 1:
        price_minute = 15
    else:
        price_minute = 10
else:
    sunday_tax_percent = 0.03

price_minute = 0

# Regular Price
if total_minutes <= 5:
    price_minute = 1
elif total_minutes >= 6 or total_minutes <= 8: 
    price_minute = 0.8
elif total_minutes == 6 or total_minutes == 10: 
    price_minute = 0.7
else:
    price_minute = 0.5

# Total Price

total_price = price_minute * total_minutes

# Tax

tax = total_price * sunday_tax_percent

# Total Price with Tax

total_price_with_tax = total_price + tax

# Print Results

print("\nPrecio por minuto es: " + str(price_minute))
print("Precio del impuesto: " + str(tax))
print("-------------------------------")
print(f"Precio total: {str(total_price)} euros\n")






