'''
Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero en una moneda a otra moneda, 
para ello haremos uso de la API descrita aquí (https://www.exchangerate-api.com).

Al usuario/a le pediremos:

La moneda desde la que queremos la conversión.
La moneda a la que queremos convertir.
La cantidad de dinero que tenemos.
A tener en cuenta:

Si la consulta da un error hay que indicarlo.
Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, 
estas se pueden obtener mediante consulta en esta misma API (https://www.exchangerate-api.com/docs/supported-codes-endpoint).

@author Virginia Ordoño Bernier
@date January 2023 
'''
#import json
import time
import requests

API_KEY = '7c1bcd326d635859cbbd8548'
url_codes_list = f'https://v6.exchangerate-api.com/v6/{API_KEY}/codes'

payload = {}
headers = {}

def main():
    print('\nCONVERSIÓN DE DIVISAS')
    print('-'*25)
    print('\nA continuación el programa te pedirá los datos necesarios para la conversión de divisas.')
    print('A continuación se muestran los códigos de las diferentes divisas:')
    time.sleep(4)
    show_currencies_codes()
    
    source_currency = input('\nIntroduce la divisa origen: ').upper()
    target_currency = input('Introduce la divisa de destino: ').upper()
    
    try:
        amount = float(input('Introduce la cantidad: '))  # Use float to handle decimal numbers
    except ValueError:
        print("Error: La cantidad introducida no es válida.")
        return

    result = get_currency_conversion(source_currency, target_currency, amount)
    print(result)
    
def show_currencies_codes():
    response = requests.request("GET", url_codes_list, headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response content to a dictionary
        data = response.json()    
        supported_codes = data.get("supported_codes", [])

        for code, currency in supported_codes:
            print(f"Código: {code}, Moneda: {currency}")
    else:
        return (f"Error: {response.status_code}")

def get_currency_conversion(source_currency, target_currency, amount):
    try:
        url_currency_exchange = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source_currency}/{target_currency}/{amount}'
        response = requests.get(url_currency_exchange)
        response.raise_for_status()  
        data = response.json() # dictionary
        return (f"{amount} {source_currency} ==> {data.get('conversion_result')} {target_currency}")
    except requests.exceptions.RequestException:
        return (f"Ha habido un error en la petición. Inténtalo de nuevo.")
    
if __name__ == '__main__':
    main()