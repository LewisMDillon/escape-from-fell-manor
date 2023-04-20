# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import sys
import art


def type_print(text, speed=0.03):
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
    type_print(TITLE, 0.0001)


def display_main_menu():
    """
    Displays the main menu
    """
    MAIN_MENU = art.MAIN_MENU
    type_print(MAIN_MENU, 0.0001)


# Player Setup ############
class Player:
    def __init__(self, name, health, location):
        self.name = name
        self.health = health
        self.location = location
        
        
myPlayer = Player('Lewis', 3, 'a1')


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
    else:
        print('Please type play, help, or quit')
        title_screen_options()


def start_game():
    print('Game Starting...')


def help_screen():
    HELP = art.HELP
    print(HELP)
    input("Press ENTER to continue")
    display_main_menu()
    title_screen_options()


def quit_game():
    print('Exiting Game...')
    sys.exit()


def main():
    display_title_screen()
    time.sleep(2)
    display_main_menu()
    title_screen_options()


main()
