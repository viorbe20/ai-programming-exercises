'''
El FBI tiene recorte de personal informático y solicitan nuestra ayuda, 
quieren saber cuantos fugitivos tienes registrados en cada una de sus oficinas, 
para ello han habilitado una API a la que puedes acceder desde aquí (https://www.fbi.gov/wanted/api).

El programa debe mostrar el nombre de cada oficina (ordenado) y la cantidad de fugitivos registrados. 
También debe mostrar la cantidad de fugitivos no registrados en ninguna oficina. 

Ten en cuenta que cada consulta muestra un número limitado de registros, 
vas a tener que hacer consultas iterativas enviando como parámetro la página de la consulta hasta que ya no queden páginas que consultar.
'''

import requests

def main():
    wanted_result = get_wanted_by_office()
    print(wanted_result)

def get_wanted_by_office():
    
    response = requests.get('https://api.fbi.gov/wanted/v1/list')
    
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        field_offices_dic = {}

        for item in items:

            field_offices = item.get('field_offices')

            # Check if 'field_offices' is not None before iterating
            if field_offices is not None:
                for field_office in field_offices:
                    if field_office in field_offices_dic:
                        field_offices_dic[field_office] += 1
                    else:
                        field_offices_dic[field_office] = 1
            else:
                if 'none' in field_offices_dic:
                    field_offices_dic['Ninguna'] += 1
                else:
                    field_offices_dic['Ninguna'] = 1

        print("\nListado de fugitivos por oficina:")
        print('-'*30)

        for field_office, count in sorted(field_offices_dic.items()):
            print(f"{field_office.upper()}: {count}")
    else:
        print(f"Error al hacer la petición: {response.status_code}")



    
if __name__ == '__main__':
    main()