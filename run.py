import time
import sys
import os
import random
import art
import gametext


def type_effect(text, speed=0.0001):
    '''
    prints out text letter by letter, adjust speed argument
    to change speed, lower is faster
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


def display_title_screen():
    """
    Displays the Main Game Logo
    """
    TITLE = art.TITLE
    type_effect(TITLE, 0.0001)


def display_main_menu():
    """
    Displays the main menu
    """
    MAIN_MENU = art.MAIN_MENU
    type_effect(MAIN_MENU, 0.0001)


# Player Setup ############
class Player:
    """
    Player character class
    """
    def __init__(
        self, name, location, health, weapon, strength, shield, armour,
        lantern, manormap, eyeglass, silver_key
                ):
        self.name = name
        self.location = location
        self.health = health
        self.weapon = weapon
        self.shield = shield
        self.strength = strength
        self.armour = armour
        self.lantern = lantern
        self.manormap = manormap
        self.eyeglass = eyeglass
        self.silver_key = silver_key


myPlayer = Player(
    'Player', 'c3', 10, 'No Weapon', 2, 'No Shield', 2,
    False, False, False, False
    )


# Enemies Setup ###########
class Monster:
    """
    Monster class
    """
    def __init__(self, name, health, strength, armour):
        self.name = name
        self.health = health
        self.strength = strength
        self.armour = armour


ogre = Monster('Ogre', 10, 4, 2)
haunted_chest = Monster('Haunted Chest', 12, 5, 3)


class Weapon:
    """
    Weapon class
    """
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


rusty_dagger = Weapon('RUSTY DAGGER', 4)
silver_sword = Weapon('SILVER SWORD', 8)


class Shield:
    """
    Shield class
    """
    def __init__(self, name, armour):
        self.name = name
        self.armour = armour


wooden_shield = Shield('Wooden Shield', 4)
iron_shield = Shield('Iron Shield', 8)


def title_screen_options():
    """
    presents user with different selectable options at
    the title screen
    """
    option = input('> ')
    if option.lower().strip() == ('play'):
        player_setup()
        game_introduction()  # define this later
    elif option.lower().strip() == ('help'):
        help_screen()  # define this later
    elif option.lower().strip() == ('quit'):
        quit_game()  # define this later
    elif option.lower().strip() == ('test'):
        test_function()
    else:
        print('Please type play, help, or quit')
        title_screen_options()


def help_screen():
    """
    Displays the game instructions on ASCII art
    background
    """
    HELP = art.HELP
    print(HELP)
    input("\n\n                     -- Press ENTER to continue --")
    display_main_menu()
    title_screen_options()


def quit_game():
    print('Exiting Game...')
    sys.exit()


def player_setup():
    """
    Sets player starting attributes to default values
    """
    myPlayer.name = 'Player'
    myPlayer.location = 'c3'
    myPlayer.health = 10
    myPlayer.weapon = 'No Weapon'
    myPlayer.strength = 2
    myPlayer.shield = 'No Shield'
    myPlayer.armour = 2
    myPlayer.lantern = True
    myPlayer.manormap = False
    myPlayer.eyeglass = False
    myPlayer.silver_key = False


def inventory_screen():
    """
    Displays the player inventory, lists all weapons,
    equipment, and items the player has found & displays player health
    """
    print("Here are the items and equipment " 
          "that you have gathered on your journey so far:\n")
    if myPlayer.weapon == 'Rusty Dagger':
        print(
            f"\nWeapon: {myPlayer.weapon} -- +{rusty_dagger.strength - 2} damage"
            )
    elif myPlayer.weapon == 'Silver Sword':
        print(
            f"\nWeapon: {myPlayer.weapon} -- +{silver_sword.strength - 2} damage"
            )
    else:
        print(f"\nWeapon: {myPlayer.weapon}")

    if myPlayer.shield == 'Wooden Shield':
        print(
            f"\nShield: {myPlayer.shield} -- +{wooden_shield.armour - 2} armour"
            )
    elif myPlayer.shield == 'Iron Shield':
        print(
            f"\nShield: {myPlayer.shield} -- +{iron_shield.armour - 2} armour"
            )
    else:
        print(f"\nShield: {myPlayer.shield}")
    print("\nOther items:")
    if myPlayer.lantern:
        print("Lantern")
    else:
        print("None")
    if myPlayer.manormap:
        print("Map")
    if myPlayer.eyeglass:
        print("Eyeglass")
    if myPlayer.silver_key:
        print("Silver Key")
    
    print(f"\n\n Your health is currently at {myPlayer.health}")
    

def display_map():
    print(f"{map_dict[myPlayer.location]}")


# Test Function #######################
def test_function():
    print('The test function ran successfuly')
    print(f"the player is currently in room {myPlayer.location}")
    calculate_valid_directions()
    

# Map ########
#     _________________
#     |a1 |a2 |a3 |a4 |
#     |___|___|___|___|
#     |b1 |b2 |b3 |b4 |
#     |___|___|___|___|
#     |c1 |c2 |c3 |c4 |
#     |___|___|___|___|
#     |d1 |d2 |d3 |d4 |
#     |___|___|___|___|

room_map = {
    'a1': {
        'room_name': 'Study',
        'description': (f"{gametext.room_descriptions['a1']}"),
        'details': (f"{gametext.room_details['a1']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a2': {
        'room_name': 'Black Chasm',
        'description': (f"{gametext.room_descriptions['a2']}"),
        'details': (f"{gametext.room_details['a2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a3',
        'west': False
    },
    'a3': {
        'room_name': 'Library',
        'description': (f"{gametext.room_descriptions['a3']}"),
        'details': (f"{gametext.room_details['a3']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a4',
        'west': 'a2'
    },
    'a4': {
        'room_name': 'Dining room',
        'description': (f"{gametext.room_descriptions['a4']}"),
        'details': (f"{gametext.room_details['a4']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b4',
        'east': False,
        'west': 'a3'
    },
    'b1': {
        'room_name': 'Upstairs Corridor',
        'description': 'a bedroom',
        'details': 'you look around and see beds',
        'entered': False,
        'completed': False,
        'north': 'a1',
        'south': 'c1',
        'east': 'b2',
        'west': False
    },
    'b2': {
        'room_name': 'Arena',
        'description': 'a bathroom',
        'details': "you look around and see a toilet",
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'c2',
        'east': False,
        'west': 'b1'
    },
    'b3': {
        'room_name': 'Storage Room',
        'description': (f"{gametext.room_descriptions['b3']}"),
        'details': (f"{gametext.room_details['b3']}"),
        'entered': False,
        'looked': False,
        'lantern_looked': False,
        'completed': False,
        'north': False,
        'south': 'c3',
        'east': 'b4',
        'west': False
    },
    'b4': {
        'room_name': 'Grand Hall',
        'description': (f"{gametext.room_descriptions['b4']}"),
        'details': (f"{gametext.room_details['b4']}"),
        'entered': False,
        'completed': False,
        'north': 'a4',
        'south': 'c4',
        'east': False,
        'west': 'b3'
    },
    'c1': {
        'room_name': 'Final Door',
        'description': 'an Observatory',
        'details': 'you look around and see space',
        'entered': False,
        'completed': False,
        'north': 'b1',
        'south': 'd1',
        'east': False,
        'west': False
    },
    'c2': {
        'room_name': 'Bedroom',
        'description': 'a library',
        'details': "you look around and see books",
        'entered': False,
        'completed': False,
        'north': 'b2',
        'south': False,
        'east': False,
        'west': False
    },
    'c3': {
        'room_name': 'Prison Cell',
        'description': (f"{gametext.room_descriptions['c3']}"),
        'details': (f"{gametext.room_details['c3']}"),
        'entered': True,
        'completed': False,
        'north': 'b3',
        'south': False,
        'east': False,
        'west': False
    },
    'c4': {
        'room_name': 'Stone Corridor',
        'description': (f"{gametext.room_descriptions['c4']}"),
        'details': (f"{gametext.room_details['c4']}"),
        'entered': False,
        'completed': False,
        'north': 'b4',
        'south': 'd4',
        'east': False,
        'west': False
    },
    'd1': {
        'room_name': 'Final Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'c1',
        'south': False,
        'east': False,
        'west': False
    },
    'd2': {
        'room_name': 'Altar',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'd3',
        'west': False
    },
    'd3': {
        'room_name': 'Goblin Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'd4',
        'west': 'd2'
    },
    'd4': {
        'room_name': 'Riddle Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'c4',
        'south': False,
        'east': False,
        'west': 'd3'
    },
}

map_dict = {
    'a1': art.MAPA1,
    'a2': art.MAPA2,
    'a3': art.MAPA3,
    'a4': art.MAPA4,
    'b1': art.MAPB1,
    'b2': art.MAPB2,
    'b3': art.MAPB3,
    'b4': art.MAPB4,
    'c1': art.MAPC1,
    'c2': art.MAPC2,
    'c3': art.MAPC3,
    'c4': art.MAPC4,
    'd1': art.MAPD1,
    'd2': art.MAPD2,
    'd3': art.MAPD3,
    'd4': art.MAPD4,
}


def game_introduction():
    os.system("clear")
    type_effect("What is your name, victim ")
    type_effect('\b\b\b\b\b\b\b', 0.04)
    type_effect('brave adventurer? \n')
    name = input('> ')
    myPlayer.name = name
    os.system("clear")
    type_effect(f"Welcome, {myPlayer.name}, to Fell Manor\n")
    type_effect("Please, do make yourself at home \n")
    type_effect("But you may wish to steer clear of the other guests \n")
    type_effect("You might find them...")
    time.sleep(0.5)
    type_effect("\nless than hospitable \n", 0.06)
    type_effect("Heh heh heh heh \n", 0.15)
    game_instructions()


def update_player_location(destination):
    """
    Sets player location value to value of
    destination, passed as an argument.
    """
    os.system("clear")
    myPlayer.location = destination
    print_room_description()
    room_map[myPlayer.location]['entered'] = True


def print_room_description():
    if room_map[myPlayer.location]['entered']:
        print(
            f"You are back in the {room_map[myPlayer.location]['description']}"
            )
    else:
        type_effect(
            "You find yourself in"
            f" a {room_map[myPlayer.location]['description']}"
            )


def print_room_details():
    if room_map[myPlayer.location]['completed']:
        type_effect("You have found all there is to find in this room")

    elif myPlayer.location == 'b3':
        storage_room_details()

    elif myPlayer.location == 'a4':
        dining_room_prompt()

    elif myPlayer.location == 'c3':
        prison_cell_details()

    elif myPlayer.location == 'c4':
        type_effect(room_map[myPlayer.location]['details'])
        lantern_prompt()

    elif myPlayer.location == 'a2':
        black_chasm_details()

    elif myPlayer.location == 'a1':
        study_details()

    else:
        type_effect(room_map[myPlayer.location]['details'])


def storage_room_details():
    if room_map['b3']['looked'] is True:
        if myPlayer.lantern is False:
            type_effect(gametext.room_details_looked['b3'])
        else:
            type_effect(gametext.room_details_lantern['b3'])
            myPlayer.manormap = True
            room_map['b3']['completed'] = True

    else:
        if myPlayer.lantern is False:
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
                type_effect(room_map['b3']['details'])
                room_map['b3']['looked'] = True
        else:
            type_effect(gametext.room_details_combined['b3'])
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
            myPlayer.manormap = True
            room_map['b3']['completed'] = True
    

def prison_cell_details():
    if myPlayer.lantern is False:
        type_effect(room_map[myPlayer.location]['details'])
    else:
        if myPlayer.shield == 'No Shield':
            type_effect(gametext.room_details_lantern['c3'])
            myPlayer.shield = 'Wooden Shield'
            myPlayer.armour = 4
        else:
            type_effect(gametext.room_details_lesser_item['c3'])
       

def black_chasm_details():
    if myPlayer.lantern:
        type_effect(gametext.room_details_lantern['a2'])
        room_map['a2']['west'] = 'a1'
    else:
        type_effect("Do you want to step forward into the blackness? (yes/no)")
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            type_effect(gametext.room_details['a2'])
            player_death()
        else:
            main_prompt()


def study_details():
    type_effect(gametext.room_details['a1'])
    type_effect("Do you want to open the chest? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.enemy_text['haunted_chest'])
        combat(haunted_chest)
    else:
        type_effect("You step nervously back from the chest.")


def candlelit_corridor_details():
    type_effect(gametext.room_details['b1'])
    type_effect("Do you want to drink the liquid? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.item_text['health_potion'])
    else:
        type_effect(
            "You leave the vial where it is and slide the drawer shut"
            )


def update_player_health(num):
    myPlayer.health = myPlayer.health + num
    if myPlayer.health <= 0:
        player_death()


def update_enemy_health(enemy, num):
    enemy.health = enemy.health + num
    if enemy.health <= 0:
        enemy_death(enemy)


def player_death():
    type_effect("\n\nYou Died....")
    time.sleep(4)
    main()


def enemy_death(enemy):
    type_effect(f"You defeated the {enemy.name}!\n")
    if myPlayer.location == 'a4':
        type_effect(gametext.enemy_death['ogre'])
        update_player_health(10)
        room_map['a4']['completed'] = True
    elif myPlayer.location == 'a1':
        type_effect(gametext.enemy_death['haunted_chest'])
        myPlayer.shield = 'Iron Shield'
        myPlayer.armour = 8
        room_map['a1']['completed'] = True
        

def game_begin_message():
    type_effect(f"You awake in a {room_map[myPlayer.location]['description']}")


def calculate_valid_directions():
    directions_list = []
    for key, value in room_map[myPlayer.location].items():
        if key in ['north', 'south', 'east', 'west']:
            if value is not False:
                directions_list.append(key)
    type_effect(" you can travel: \n")
    for direction in directions_list:
        type_effect(direction + '\n')
    return directions_list


def main_prompt():
    print("\n")
    if myPlayer.manormap is False:
        type_effect(
            "\nYou can 'look' around the room for more information,"
            " type 'items' to view your items & health, \nor"
                 )
    else:
        type_effect(
            "\nYou can 'look' around the room for more information,"
            " type 'items' to view your items & health, type 'map' to view the"
            " map,\nor"
                 )
    directions_list = calculate_valid_directions()
    print("\n")
    type_effect("What would you like to do?\n", 0.004)
    answer = input("> ")
    if answer.lower().strip() in directions_list:
        update_player_location(room_map[myPlayer.location][f"{answer}"])
    elif answer.lower().strip() == 'look':
        os.system("clear")
        print_room_details()
    elif answer.lower().strip() == 'items':
        inventory_screen()
    elif answer.lower().strip() == 'map':
        if myPlayer.manormap:
            display_map()

    main_prompt()


def lantern_prompt():
    type_effect(" Do you want to try to grab the lantern? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        lantern_attempt()
    else:
        main_prompt()
        

def lantern_attempt():
    rng = random.randint(1, 3)
    if rng <= 2:
        type_effect(gametext.item_text['lantern_success'])
        myPlayer.lantern = True
    else:
        type_effect(gametext.item_text['lantern_failure'])
        update_player_health(1)
        type_effect(" Do you want to try again? (yes/no)")
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            lantern_attempt()
        else:
            main_prompt()


def dining_room_prompt():
    type_effect(f"{gametext.room_details['a4']}")
    type_effect("Do you take a bite of the bread? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(
            "You take a bite of the bread, it is astonishingly tasty,"
            " fluffy and warm, yet delightfully crunchy."
            "\n\n **Your health increases by 2 points**\n\n"
            )
        update_player_health(2)
        type_effect(gametext.enemy_text['ogre'])
        combat(ogre)


def game_instructions():
    os.system("clear")
# type_effect("You must escape from Fell Manor! \n", 0.003)
# type_effect("To move from room to room, type 'north', 'south',\n", 0.003)
# type_effect("'east' or 'west' when prompted.", 0.003)
# print('\n')
# time.sleep(0.07)
# type_effect("You can also type 'look' to examine", 0.003)
# type_effect(" the room you are in for more information \n", 0.003)
# print("\n")
# time.sleep(0.07)
# type_effect("Many challenges await you,\n", 0.003)
# type_effect("Good Luck!\n", 0.003)
# print("\n \n \n \n")
    input("-- press ENTER to begin --")
    os.system("clear")
    game_begin_message()
    main_prompt()


def combat(enemy):
    type_effect(f"\nThe {enemy.name} attacks!")
    enemy_attack_strength = random.randint(0, 4) + enemy.strength - myPlayer.armour
    if enemy_attack_strength < 0:
        enemy_attack_strength = 0
    type_effect(f"\nThe {enemy.name} hits you for {enemy_attack_strength} damage!")
    print(f"\nYour health was at {myPlayer.health}")
    print(
        f"\nafter that attack, it's now at {myPlayer.health - enemy_attack_strength}"
        )
    update_player_health(enemy_attack_strength * -1)

    input("\n\nPress ENTER to attack!")

    if myPlayer.weapon == 'No Weapon':
        type_effect(f"You attack the {enemy.name} with your bare fists!")
    else:
        type_effect(f"You attack the {enemy.name} with your {myPlayer.weapon}!")
    attack_strength = random.randint(0, 4) + myPlayer.strength - enemy.armour
    if attack_strength < 0:
        attack_strength = 0
    print(f"You hit the {enemy.name} for {attack_strength} damage!")
    print(f"The {enemy.name}'s health was at {enemy.health}")
    print(f"After that attack, it's now at {enemy.health - attack_strength}")
    update_enemy_health(enemy, attack_strength * -1)
    
    if enemy.health <= 0:
        return
    else:
        input("Press ENTER to continue!")
        combat(enemy)


def main():
    display_title_screen()
    time.sleep(0)
    display_main_menu()
    title_screen_options()


main()
