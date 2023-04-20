# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import sys
import art


def type_print(text, speed=0.03):
    '''
    Function for typewriter effect for printing the text
    with variable speed, 0.03 speed by default
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


def display_title_screen():
    TITLE = art.TITLE
    MAIN_MENU = art.MAIN_MENU
    type_print(TITLE, 0.001)
    type_print(MAIN_MENU, 0.001)


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
    print('Game Starting')


def help_screen():
    print('Here is some helpful info')


def quit_game():
    print('Exiting Game')
    sys.exit()


display_title_screen()
title_screen_options()
