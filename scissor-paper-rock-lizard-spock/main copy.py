'''
Partiendo del código disponible en fichero adjunto,
añade la funcionalidad necesaria para ofrecer la variante lagarto, Spock del juego piedra, papel o tijeras.
Usa las diferentes situaciones de juego, junto con su resultado, del archivo victories.xml que se adjunta.
Sustituye el diccionario Victories por alguna referencia que permita acceder al contenido de victories.xml.

@author - Virginia Ordoño Bernier
@date - January 2024
'''
import xml.etree.ElementTree as ET
import random
from enum import IntEnum
from statistics import mode

class GameAction(IntEnum):
    # possible actions 
    Rock = 0
    Paper = 1
    Scissors = 2
    # add elements 
    Lizard = 3
    Spock = 4

class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

def get_victories(xml_file):
# Get info about victories from a xml file and return a dictionary with the result depending on the selection
    tree = ET.parse(xml_file) # parse method returns an object ElementTree that represents the xml tree
    root = tree.getroot() # reference to the superior element in order to work with all its elements
    victories_dict = {}
    results_dict = {}

    for victory_elem in root.findall('victory'):
        # print(victory_elem.text)
        # 'choice' and 'against' are both attributes of each element <victory> from the xml
        choice = GameAction[victory_elem.get('choice')] 
        against = GameAction[victory_elem.get('against')]
        victories_dict[choice] = against
        
        translation = victory_elem.text.strip()
        results_dict[choice] = translation

    return victories_dict, results_dict

Victories, Results = get_victories("C:/Users/vober/Documents/curso-especializacion-bd-ia/PIA/pia-github/scissor-paper-rock-lizard-spock/resources/victories.xml")

# The computer will attempt to predict the user's choice based on the last recent actions  
NUMBER_RECENT_ACTIONS = 5


def assess_game(user_action, computer_action):
    game_result = None
    
    if user_action == computer_action:
        print(f"Usuario y máquina han elegido {user_action.name}. ¡Empate!")
        game_result = GameResult.Tie

    elif user_action in Results:
        translation = Results[user_action]
        print(f"{translation}. ¡Has perdido!" if Victories[user_action] == computer_action else f"{translation}. ¡Has ganado!")
        game_result = GameResult.Victory if Victories[user_action] == computer_action else GameResult.Defeat

    return game_result
def get_computer_action(user_actions_history, game_history):
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Alternative AI functionality
    # Choice that would beat the user's most frequent recent choice
    else:
        most_frequent_recent_computer_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        computer_action = get_winner_action(most_frequent_recent_computer_action)

    print(f"La máquina ha elegido {computer_action.name}.")
    
    return computer_action
            
def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nEscoge una opción ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def get_random_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action

def get_winner_action(game_action):
    return Victories[game_action]

def play_another_round():
        another_round = input("\n¿Deseas seguir jugando? (s/n): ")
        return another_round.lower() == 's'

def main():
    game_history = []
    user_actions_history = []
    
    while True:
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError as e:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Selección incorrecta. Elige un número dentro de este rango {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history)
        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)

        if not play_another_round():
            break
        
if __name__ == "__main__":
    main()
