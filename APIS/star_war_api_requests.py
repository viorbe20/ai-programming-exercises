import requests

'''
Retrieves all the information about all characters 
'''
def get_all_characters():
    base_url = "https://swapi.dev/api/people/"
    all_characters = []
    page = 1
    
    while True:
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        data = response.json()

        try:
            characters_on_page = data.get('results')
            all_characters.extend(characters_on_page)
            page += 1
        except Exception as e:
            print(f"Error al extraer informmación de la página {page}: {e}")
            break

    return all_characters

'''
Takes a character index as input and retrieves information 
about the character associated with that index
'''
def get_character_by_index(index):
    base_url = "https://swapi.dev/api/people/"
    
    try:
        response = requests.get(base_url)
        data = response.json()
        total_characters = data.get('count')

        if 1 <= index <= total_characters:
            page = (index - 1) // 10 + 1
            character_index_on_page = (index - 1) % 10
            url = f"{base_url}?page={page}"
            response = requests.get(url)
            data = response.json()
            character = data.get('results')[character_index_on_page]
            return character
        else:
            print(f"Índice {index} fuera de rango.")
    except Exception as e:
        print(f"Error al consultar el personaje con índice {index}: {e}")
    
    return None

'''
Takes a character index as input and retrieves information 
about the films associated with that character 
'''
def get_films_by_character_index(character_index):
    base_url = f"https://swapi.dev/api/people/{character_index}/"

    try:
        response = requests.get(base_url)
        character_data = response.json()
        film_urls = character_data.get('films', [])

        films = []
        for film_url in film_urls:
            film_response = requests.get(film_url)
            film_data = film_response.json()
            films.append(film_data)

        return films

    except Exception as e:
        print(f"Error con el índice del personaje {character_index}: {e}")
    
    return None

'''
Takes a character index as input and retrieves information 
about the starships associated with that character 
'''
def get_starships_by_character_index(character_index):
    
    base_url = f"https://swapi.dev/api/people/{character_index}/"

    try:
        response = requests.get(base_url)
        character_data = response.json()
        starship_urls = character_data.get('starships', [])

        starships = []
        for starship_url in starship_urls:
            starship_response = requests.get(starship_url)
            starship_data = starship_response.json()
            starships.append(starship_data)

        return starships

    except Exception as e:
        print(f"Error con el índice del personaje {character_index}: {e}")
    
    return None

