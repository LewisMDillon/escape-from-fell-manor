import time
import sys
import os
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
    def __init__(self, name, health, location):
        self.name = name
        self.health = health
        self.location = location


myPlayer = Player('Name', 5, 'b1')


def title_screen_options():
    """
    presents user with different selectable options at
    the title screen
    """
    option = input('> ')
    if option.lower().strip() == ('play'):
        start_game()  # define this later
    elif option.lower().strip() == ('help'):
        help_screen()  # define this later
    elif option.lower().strip() == ('quit'):
        quit_game()  # define this later
    elif option.lower().strip() == ('test'):
        test_function()
    else:
        print('Please type play, help, or quit')
        title_screen_options()


def start_game():
    print('Game Starting...')
    player_setup()
    myPlayer.location = 'c3'
    myPlayer.health = 5
    game_introduction()
    # prompt()


def help_screen():
    HELP = art.HELP
    print(HELP)
    input("Press ENTER to continue")
    display_main_menu()
    title_screen_options()


def quit_game():
    print('Exiting Game...')
    sys.exit()


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

room_map = {
    'a1': {
        'room_name': 'laboratory',
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
        'room_name': 'dungeon',
        'description': 'a scary dungeon',
        'details': "it's a really scary dungeon",
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b2',
        'east': 'a3',
        'west': 'a1'
    },
    'a3': {
        'room_name': 'cellar',
        'description': 'a dingy cellar',
        'details': "it's a really dingy cellar",
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b3',
        'east': 'a4',
        'west': 'a2'
    },
    'a4': {
        'room_name': 'dining room',
        'description': 'a beautiful dining room',
        'details': 'let the feast..... begin',
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b4',
        'east': False,
        'west': 'a3'
    },
    'b1': {
        'room_name': 'Bedroom',
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
        'room_name': 'Bathroom',
        'description': 'a bathroom',
        'details': "you look around and see a toilet",
        'entered': False,
        'completed': False,
        'north': 'a2',
        'south': 'c2',
        'east': 'b3',
        'west': 'b1'
    },
    'b3': {
        'room_name': 'Swimming Pool',
        'description': 'a Swimming Pool',
        'details': "you look around and see a pool",
        'entered': False,
        'completed': False,
        'north': 'a3',
        'south': 'c3',
        'east': 'b4',
        'west': 'b2'
    },
    'b4': {
        'room_name': 'Study',
        'description': 'a Study',
        'details': 'you look around and see a desk',
        'entered': False,
        'completed': False,
        'north': 'a4',
        'south': 'c4',
        'east': False,
        'west': 'b3'
    },
    'c1': {
        'room_name': 'Observatory',
        'description': 'an Observatory',
        'details': 'you look around and see space',
        'entered': False,
        'completed': False,
        'north': 'b1',
        'south': False,
        'east': 'c2',
        'west': False
    },
    'c2': {
        'room_name': 'Library',
        'description': 'a library',
        'details': "you look around and see books",
        'entered': False,
        'completed': False,
        'north': 'b2',
        'south': False,
        'east': 'c3',
        'west': 'c1'
    },
    'c3': {
        'room_name': 'Starting Room',
        'description': ("Cold, stone room. It seems to be a cell of "
                        "some sort\nbut the large iron-barred door "
                        "to the north hangs open.\n"),
        'details': "you look around and see the starting room",
        'entered': True,
        'completed': False,
        'north': 'b3',
        'south': False,
        'east': False,
        'west': False
    },
    'c4': {
        'room_name': 'Spike Pit',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'b4',
        'south': False,
        'east': False,
        'west': 'c3'
    },
}


def player_setup():
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
            f"You find yourself in a {room_map[myPlayer.location]['description']}"
            )


def print_room_details():
    type_effect(room_map[myPlayer.location]['details'])


def update_player_health(num):
    myPlayer.health = myPlayer.health + num


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


def prompt_default():
    print("\n")
    type_effect("\nYou can 'look' around the room for more information, \nor")
    directions_list = calculate_valid_directions()
    print("\n")
    type_effect("What would you like to do?\n", 0.04)
    answer = input("> ")
    if answer.lower().strip() in directions_list:
        update_player_location(room_map[myPlayer.location][f"{answer}"])
    elif answer == 'look':
        os.system("clear")
        print_room_details()
    prompt_default()
    

# this is the code to move room
# update_player_location(room_map[myPlayer.location]['east'])


def game_introduction():
    os.system("clear")
    type_effect("You must escape from Fell Manor! \n", 0.003)
    type_effect("To move from room to room, type 'go north', 'go south',\n", 0.003)
    type_effect("go east' or 'go west' when prompted.", 0.003)
    print('\n')
    time.sleep(0.07)
    type_effect("You can also type 'look' to try to examine", 0.003)
    type_effect(" the room you are in for more information \n", 0.003)
    print("\n")
    time.sleep(0.07)
    type_effect("Many challenges await you,\n", 0.003)
    type_effect("Good Luck!\n", 0.003)
    print("\n \n \n \n")
    input("-- press ENTER to begin --")
    os.system("clear")
    game_begin_message()
    prompt_default()


def main():
    display_title_screen()
    time.sleep(0)
    display_main_menu()
    title_screen_options()


main()
