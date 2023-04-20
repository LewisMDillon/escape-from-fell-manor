import time
import sys
import os
import art


def type_effect(text, speed=0.04):
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


myPlayer = Player('Name', 5, 'a1')


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
    # update_player_location(location)
    # update_player_health(health)
    # game_introduction()
    # describe_location()
    # player_status()
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


def test_function():
    print('The test function ran successfuly')
    print(room_map[myPlayer.location]['description'])
    myPlayer.location = 'a2'
    print(room_map[myPlayer.location]['description'])
    myPlayer.location = 'a3'
    print(room_map[myPlayer.location]['description'])
    myPlayer.location = 'a4'
    print(room_map[myPlayer.location]['description'])


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
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a3': {
        'room_name': 'cellar',
        'description': 'a dingy cellar',
        'details': "it's a really dingy cellar",
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a4': {
        'room_name': 'dining room',
        'description': 'a beautiful dining room',
        'details': 'let the feast..... begin',
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'b1': {
        'room_name': 'Bedroom',
        'description': 'a bedroom',
        'details': 'you look around and see beds',
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'b2': {
        'room_name': 'Bathroom',
        'description': 'a bathroom',
        'details': "you look around and see a toilet",
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'b3': {
        'room_name': 'Swimming Pool',
        'description': 'a Swimming Pool',
        'details': "you look around and see a pool",
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'b4': {
        'room_name': 'Study',
        'description': 'a Study',
        'details': 'you look around and see a desk',
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'c1': {
        'room_name': 'Observatory',
        'description': 'an Observatory',
        'details': 'you look around and see space',
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'c2': {
        'room_name': 'Library',
        'description': 'a library',
        'details': "you look around and see books",
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'c3': {
        'room_name': 'Starting Room',
        'description': 'the starting room',
        'details': "you look around and see the starting room",
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'c4': {
        'room_name': 'Spike Pit',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
}


def player_setup():
    os.system("clear")
    type_effect("What is your name, victim   ")
    type_effect('\b\b\b\b\b\b\b\b\b')
    type_effect('brave adventurer? \n')
    name = input('> ')
    myPlayer.name = name
    os.system("clear")
    type_effect(f"Welcome, {myPlayer.name}. \n")
    update_player_location('c3')


def update_player_location(destination):
    """
    Sets player location value to value of
    destination, passed as an argument.
    """
    myPlayer.location = destination


def main():
    display_title_screen()
    time.sleep(0)
    display_main_menu()
    title_screen_options()


main()
