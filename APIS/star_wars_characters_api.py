from star_war_api_requests import *

def main():
    print('\nINFORMACIÓN SOBRE LOS PERSONAJES DE STAR WAR')
    print('-'*45)
    print('A continuación se mostrará un listado con los personajes de la saga.')
    print('Busca aquel sobre el que quieras la información e introduce el número correspondiente a continuación.')
    
    characters = get_all_characters()

    for index, character in enumerate(characters, start=1):
        print(f"{index} - {character['name']}")
        
    character_index = int(input('\nIntroduce el número del personaje: '))

    character_info = get_character_by_index(character_index)
    character_films = get_films_by_character_index(character_index)
    character_starship = get_starships_by_character_index(character_index)
    
    print(f"\nPLANETAS DE {character_info['name'].upper()}")
    print('-'*45)
    for starship in character_starship:
        print(f"{starship['name']}")
    print(f"\nPELÍCULAS DE {character_info['name'].upper()}")
    print('-'*45)
    for film in character_films:
        print(f"{film['title']}, Episodio: {film['episode_id']}\n")

if __name__ == "__main__":
    main()

