import time
import sys
import os
import random
import art


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


wooden_shield = Shield('WOODEN SHIELD', 2)
iron_shield = Shield('IRON SHIELD', 4)


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
    myPlayer.shield = 'No shield'
    myPlayer.armour = 2
    myPlayer.lantern = False
    myPlayer.manormap = False
    myPlayer.eyeglass = False
    myPlayer.silver_key = False


def inventory_screen():
    """
    Displays the player inventory, lists all weapons,
    equipment, and items the player has found.
    """
    print("Here are the items and equipment " 
          "that you have gathered on your journey so far:\n")
    if myPlayer.weapon == 'Rusty Dagger':
        print(f"\nWeapon: {myPlayer.weapon} -- +{rusty_dagger.strength - 2} damage")
    elif myPlayer.weapon == 'Silver Sword':
        print(f"\nWeapon: {myPlayer.weapon} -- +{silver_sword.strength - 2} damage")
    else:
        print(f"\nWeapon: {myPlayer.weapon}")
    print(f"\nShield: {myPlayer.shield}")
    print("\nOther items:")
    if myPlayer.lantern:
        print("Lantern")
    if myPlayer.manormap:
        print("Map")
    if myPlayer.eyeglass:
        print("Eyeglass")
    if myPlayer.silver_key:
        print("Silver Key")
    else:
        print("None")


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
        'description': 'a lab with chemicals',
        'details': 'you look around and see chemicals',
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a2': {
        'room_name': 'Corridor of Spikes',
        'description': 'a scary dungeon',
        'details': "it's a really scary dungeon",
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a3',
        'west': 'a1'
    },
    'a3': {
        'room_name': 'Library',
        'description': 'a dingy cellar',
        'details': "it's a really dingy cellar",
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a4',
        'west': 'a2'
    },
    'a4': {
        'room_name': 'Dining room',
        'description': (
            "Dining room. A fire burns in the huge hearth on the"
            " opposite wall, casting warm orange light on to the"
            " centerpiece of the room:\na gigantic oaken dining table.\n\n"
            " On this dining table sits a single plate, upon which"
            " rests the most, soft, warm, appetizing loaf of bread\n"
            " Your stomach grumbles..."),
        'details': (
            "Your eyes are transfixed on the loaf of bread.\n\n"
                    ),
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
        'description': (
            "storage room. Wooden crates are piled high"
            " all around you. \nThere is very little light,"
            " but you can just make out a spiral staircase"
            " to the east\n"),
        'details': (
            "You search around in the dark and find a RUSTY DAGGER!\n"
            "It looks like decades of rust have blunted its blade, "
            "but it's better than your fists.\n\n"
            "**You equip the RUSTY DAGGER**\n\n"
            "There is probably more hidden among the crates, but "
            "it's too dark to see anything"
            ),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'c3',
        'east': 'b4',
        'west': False
    },
    'b4': {
        'room_name': 'Grand Hall',
        'description': (
            "Grand hall. your eyes follow the intricate pattern on the"
            " red and gold carpet up to the staggeringly high walls,"
            " adorned from bottom to top with beautiful paintings"
            " and portraits.\n\n There are large ornate wooden doors"
            " to the north and to the south."),
        'details': (
            "You inspect the paintings. They are all beautifully done."
            " You notice that the characters in the portraits are never"
            " looking straight out, as you would expect, but instead"
            " looking up or down at other portraits...\n\n"
            " You follow the gaze of one portrait to the next, and again"
            " and again and again \nuntil finally coming to a portrait"
            " of a young girl.\n"
            " The girl is holding out her hands as if presenting something"
            " but her hands are empty. \n\n"
            " As you peer into the painting, you realise that there is a"
            " voice coming from it!\n"
            " You press your ear close to it and try to make out what"
            " it is saying...\n\n\n"
            "     'Return to me when you can see beyond what is shown'\n\n\n"),
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
        'description': ("Cold, stone room. It seems to be a cell of "
                        "some sort\nbut the large iron-barred door "
                        "to the north hangs open.\n"),
        'details': ("It's too dark to see anything."
                    " Perhaps if you had a light source..."),
        'entered': True,
        'completed': False,
        'north': 'b3',
        'south': False,
        'east': False,
        'west': False
    },
    'c4': {
        'room_name': 'Stone Corridor',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
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
        type_effect(
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
    else:
        type_effect(room_map[myPlayer.location]['details'])
    if myPlayer.location == 'b3':
        if myPlayer.weapon == 'No Weapon':
            myPlayer.weapon = 'Rusty Dagger'
            myPlayer.strength = 4
    if myPlayer.location == 'a4':
        dining_room_prompt()


def update_player_health(num):
    myPlayer.health = myPlayer.health - num


def update_enemy_health(enemy, num):
    enemy.health = enemy.health - num


def player_death():
    type_effect("\n\nYou Died....")
    time.sleep(4)
    main()


def enemy_death(enemy):
    type_effect(f"You defeated the {enemy.name}!")


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
    type_effect(
        "\nYou can 'look' around the room for more information,"
        " type 'items' to view your items, \nor"
        )
    directions_list = calculate_valid_directions()
    print("\n")
    type_effect("What would you like to do?\n", 0.04)
    answer = input("> ")
    if answer.lower().strip() in directions_list:
        update_player_location(room_map[myPlayer.location][f"{answer}"])
    elif answer.lower().strip() == 'look':
        os.system("clear")
        print_room_details()
    elif answer.lower().strip() == 'items':
        inventory_screen()
    main_prompt()


def lantern_prompt():
    type_effect("Do you want to try to grab the lantern? (yes/no)\n")
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
        type_effect("Do you want to try again? (yes/no)")
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            lantern_attempt()
        else:
            main_prompt()


def dining_room_prompt():
    type_effect("Do you take a bite of the bread? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(
            "You take a bite of the bread, it is astonishingly tasty,"
            " fluffy and warm, yet delightfully crunchy."
            "\n your health has increased by 2 points!"
            )
        update_player_health(-2)
        type_effect("\nWill you take another bite?")
        second_answer = input("> ")
        if second_answer.lower().strip() == 'yes':
            type_effect("You sudddenly hear a loud crash etc.")
            combat(ogre)
        else:
            type_effect("You manage to stop yourself etc.")
    else:
        type_effect("You manage to stop yourself etc.")


# this is the code to move room
# update_player_location(room_map[myPlayer.location]['east'])


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
    type_effect(f"The {enemy.name} attacks!")
    enemy_attack_strength = random.randint(0, 4) + enemy.strength - myPlayer.armour
    type_effect(f"The {enemy.name} hits you for {enemy_attack_strength} damage!")
    print(f"Your health was at {myPlayer.health}")
    update_player_health(enemy_attack_strength)
    print(f"after that attack, it's now at {myPlayer.health}")

    if myPlayer.health <= 0:
        player_death()
        return
    else:
        input("Press ENTER to attack!")

    if myPlayer.weapon == 'No Weapon':
        type_effect(f"You attack the {enemy.name} with your bare fists!")
    else:
        type_effect(f"You attack the {enemy.name} with your {myPlayer.weapon}!")
    attack_strength = random.randint(0, 4) + myPlayer.strength - enemy.armour
    print(f"You hit the {enemy.name} for {attack_strength} damage!")
    print(f"The {enemy.name}'s health was at {enemy.health}")
    update_enemy_health(enemy, attack_strength)
    print(f"After that attack, it's now at {enemy.health}")

    if enemy.health <= 0:
        enemy_death(enemy)
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
