import requests
import time

def main():
    all_results = get_all_results()
    get_wanted_by_office(all_results)

def get_all_results():
    url_base = "https://api.fbi.gov/wanted/v1/list"
    page = 1
    all_results = []

    while True:
        url = f"{url_base}?page={page}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Check if there are results
            if data.get('items'):
                all_results.extend(data['items'])
                page += 1
            else:
                break
        elif response.status_code == 429:
            # Rate limit exceeded, wait for a while and try again
            print(f"Rate limit exceeded. Waiting for 10 seconds...")
            time.sleep(10)
        else:
            print(f"Error en la solicitud: {response.status_code}")
            break
    return all_results

def get_wanted_by_office(results):
    field_offices_dic = {}

    for item in results:
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
                field_offices_dic['none'] += 1
            else:
                field_offices_dic['none'] = 1

    print("\nListado de fugitivos por oficina:")
    print('-'*30)

    for field_office, count in sorted(field_offices_dic.items()):
        print(f"{field_office.upper()}: {count}")

if __name__ == '__main__':
    main()
