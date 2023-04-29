import time
import sys
import os
import random
import copy
from datetime import datetime
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style
import art
import gametext
import dictionary

colorama.init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('escape_from_fell_manor')

HOF = SHEET.worksheet('hall_of_fame')
hof_data = HOF.get_all_values()


def clear():
    os.system('clear')


def type_effect(text, speed=0.0004):
    '''
    prints out text letter by letter, adjust speed argument
    to change speed, lower is faster
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


CENT = "{:^80}".format  # variable for centering text in terminal


def skip_line():
    print("\n")


def skip_two_lines():
    print("\n\n")


def confirm():
    skip_line()
    input(CENT(
        f"            -- Press {Fore.GREEN}ENTER {Fore.WHITE}to continue --"
        ))
    clear()


def color_type(text, color, speed=0.04):
    if color == 'red':
        print(f"{Fore.RED}{Style.BRIGHT} ", end="", flush=True)
    elif color == 'green':
        print(f"{Fore.GREEN} ", end="", flush=True)
    elif color == 'yellow':
        print(f"{Fore.YELLOW} ", end="", flush=True)
    elif color == 'blue':
        print(f"{Fore.BLUE} ", end="", flush=True)
    elif color == 'magenta':
        print(f"{Fore.MAGENTA} ", end="", flush=True)
    elif color == 'cyan':
        print(f"{Fore.CYAN} ", end="", flush=True)
    elif color == 'white':
        print(f"{Fore.WHITE} ", end="", flush=True)
    
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print(f"{Fore.RESET} ", end="", flush=True)


def display_title_screen():
    """
    Displays the Main Game Logo
    """
    clear()
    TITLE = art.TITLE
    color_type(TITLE, 'red', 0.0004)
    print(f"{Fore.RESET}")
    confirm()
    display_main_menu()


def display_main_menu():
    """
    Displays the main menu
    """
    clear()
    MAIN_MENU = art.MAIN_MENU
    type_effect(MAIN_MENU, 0.00003)
    skip_two_lines()
    print(CENT(
        f"               {Fore.WHITE}Type {Fore.GREEN}'play',"
        f" 'help', 'quit', {Fore.WHITE}or"
        f" {Fore.GREEN} 'hall of fame'{Fore.WHITE}."
        ))
    title_screen_options()


def title_screen_options():
    """
    presents user with different selectable options at
    the title screen
    """
    skip_line()
    option = input('\n> ')
    if option.lower().strip() == ('play'):
        gamestate_reset()
        player_setup()
        game_introduction()
    elif option.lower().strip() == ('help'):
        help_screen()
    elif option.lower().strip() == ('quit'):
        quit_game()
    elif option.lower().strip() == ('hall of fame'):
        display_hof()
    elif option.lower().strip() == ('test'):
        test_function()
    else:
        print("Please type 'play', 'help', 'quit', or 'hall of fame'")
        confirm()
        display_main_menu()
        title_screen_options()


def help_screen():
    """
    Displays the game instructions on ASCII art
    background
    """
    clear()
    HELP = art.HELP
    print(HELP)
    confirm()
    display_main_menu()
    title_screen_options()


def display_hof():
    clear()
    type_effect(
        "\nThese are the brave adventurers who braved"
        "\nthe horrors of Fell Manor and lived to tell the tale."
    )
    skip_line()
    print(
        "\nThe table below shows the NAME of the adventurer,"
        "\ntheir remaining HEALTH points upon escaping,"
        "\nand the DATE on which they accomplished this mighty feat."
        )
    skip_line()
    type_effect(tabulate(hof_data, tablefmt="pretty"), 0.003)
    skip_two_lines()
    confirm()
    display_main_menu()
    title_screen_options()


def quit_game():
    print('Exiting Game...')
    sys.exit()


def update_hof():
    date_today = datetime.today().strftime('%Y-%m-%d')
    data = [myPlayer.name, myPlayer.health, date_today]
    HOF.append_row(data)


# Player Setup ############
class Player:
    """
    Player character class
    """
    def __init__(
        self, name, location, health, weapon, strength, shield, armour,
        lantern, manormap, eyeglass, silver_key, password
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
        self.password = password


myPlayer = Player(
    'Player', 'c3', 10, 'No Weapon', 2, 'No Shield', 2,
    False, False, False, False, False
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
goblin = Monster('Goblin', 8, 4, 1)
haunted_chest = Monster('Haunted Chest', 12, 5, 2)
gorehowl = Monster('Gorehowl', 20, 7, 1)
manor_lord = Monster('Lord of Fell Manor', 25, 8, 2)


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
iron_shield = Shield('Iron Shield', 6)


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
    myPlayer.lantern = False
    myPlayer.manormap = False
    myPlayer.eyeglass = False
    myPlayer.silver_key = False
    myPlayer.password = False


def gamestate_reset():
    global room_map
    room_map = copy.deepcopy(dictionary.room_map)
    ogre.health = 10
    goblin.health = 8
    haunted_chest.health = 12
    gorehowl.health = 20
    manor_lord.health = 25


def inventory_screen():
    """
    Displays the player inventory, lists all weapons,
    equipment, and items the player has found & displays player health
    """
    print("\nHere are the items and equipment "
          "that you have gathered on your journey so far:")
    if myPlayer.weapon == 'Rusty Dagger':
        print(
            f"\nWeapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}"
            f"-- +{rusty_dagger.strength - 2} damage"
            )
    elif myPlayer.weapon == 'Silver Sword':
        print(
            f"\nWeapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}"
            f"-- +{silver_sword.strength - 2} damage"
            )
    else:
        print(f"\nWeapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}")

    if myPlayer.shield == 'Wooden Shield':
        print(
            f"\nShield: {Fore.CYAN}{myPlayer.shield}{Fore.WHITE}"
            f"-- +{wooden_shield.armour - 2} armour"
            )
    elif myPlayer.shield == 'Iron Shield':
        print(
            f"\nShield: {Fore.CYAN}{myPlayer.shield}{Fore.WHITE}"
            f"-- +{iron_shield.armour - 2} armour"
            )
    else:
        print(f"\nShield: {myPlayer.shield}")
    skip_line()
    print("Other items:")
    if myPlayer.lantern:
        print("-Lantern")
    else:
        print("None")
    if myPlayer.manormap:
        print("-Map")
    if myPlayer.eyeglass:
        print("-Eyeglass")
    if myPlayer.silver_key:
        print("-Silver Key")
    skip_line()
    print(
        f"Your {Fore.RED}health {Fore.WHITE}is currently "
        f"at {Fore.RED}{myPlayer.health}{Fore.WHITE}"
        )


def display_map():
    print(f"{map_dict[myPlayer.location]}")


# Test Function #######################
def test_function():
    print('The test function ran successfuly')
    confirm()
    type_effect("here is some regular text, in white")
    color_type('this text is blue', 'blue')
    type_effect("this text is regular again!")
    skip_line()
    color_type('This text is a lovely magenta', 'magenta')
    print("")
    color_type("R", 'red')
    color_type('a', 'yellow')
    color_type('i', 'green')
    color_type('n', 'blue')
    color_type('b', 'magenta')
    color_type('o', 'cyan')
    color_type('w', 'white')
    print("")


room_map = copy.deepcopy(dictionary.room_map)

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
    clear()
    type_effect("What is your name,")
    color_type("victim", 'red')
    time.sleep(0.25)
    type_effect('\b\b\b\b\b\b\b', 0.03)
    type_effect('brave adventurer?')
    skip_line()
    name = input('> ')
    myPlayer.name = name
    clear()
    type_effect(f"\nWelcome, {myPlayer.name}, to Fell Manor")
    type_effect("\nPlease, do make yourself at home.")
    type_effect("\nBut you may wish to steer clear of the other guests.")
    type_effect("\nYou might find them...")
    time.sleep(0.5)
    type_effect("\nless than hospitable", 0.05)
    type_effect("\nHeh heh heh heh", 0.18)
    confirm()
    game_instructions()


def update_player_location(destination):
    """
    Sets player location value to value of
    destination, passed as an argument.
    """
    clear()
    myPlayer.location = destination
    print_room_description()
    room_map[myPlayer.location]['entered'] = True


def print_room_description():
    if room_map[myPlayer.location]['completed']:
        print(
                "You are back in the "
                f"{gametext.room_descriptions_completed[myPlayer.location]}"
                )

    elif room_map[myPlayer.location]['entered']:
        if myPlayer.location == 'd3':
            goblin_cave_description()
        else:
            print(
                "You are back in the "
                f"{room_map[myPlayer.location]['description']}"
                )
    
    elif myPlayer.location == 'd1':
        final_room_description()

    else:
        type_effect(
            "You find yourself in"
            f" a {room_map[myPlayer.location]['description']}"
            )
        if myPlayer.location == 'b2':
            arena_details()
        elif myPlayer.location == 'd4':
            riddle_room_details()


def print_room_details():
    if room_map[myPlayer.location]['completed']:
        type_effect("You have found all there is to find in this room", 0.03)

    elif myPlayer.location == 'b3':
        storage_room_details()

    elif myPlayer.location == 'b4':
        grand_hall_details()

    elif myPlayer.location == 'a3':
        library_details()

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

    elif myPlayer.location == 'b1':
        candlelit_corridor_details()

    elif myPlayer.location == 'c1':
        final_door_details()

    elif myPlayer.location == 'd3':
        goblin_cave_details()

    elif myPlayer.location == 'c2':
        alcove_details()

    elif myPlayer.location == 'd2':
        altar_details()

    else:
        type_effect(room_map[myPlayer.location]['details'])


def prison_cell_details():
    if myPlayer.lantern is False:
        type_effect(room_map[myPlayer.location]['details'])
    else:
        if myPlayer.shield == 'No Shield':
            type_effect(gametext.room_details_lantern['c3'])
            skip_two_lines()
            print(CENT(
                    f"          {Fore.CYAN}**You equip the Wooden Shield**"
                    f"{Fore.WHITE}"))
            myPlayer.shield = 'Wooden Shield'
            myPlayer.armour = 4
            (room_map[myPlayer.location]['completed']) = True
        else:
            type_effect(gametext.room_details_lesser_item['c3'])
            (room_map[myPlayer.location]['completed']) = True


def storage_room_details():
    if room_map['b3']['looked'] is True:
        if myPlayer.lantern is False:
            type_effect(gametext.room_details_looked['b3'])
        else:
            type_effect(gametext.room_details_lantern['b3'])
            skip_line()
            print(CENT(
                    f"          {Fore.CYAN}**You found the Map**"
                    f"{Fore.WHITE}"))
            skip_line()
            color_type("You can now type", 'white')
            color_type("'map'", 'green')
            color_type(
                "when prompted to see a map of Fell Manor's rooms", 'white'
                )
            myPlayer.manormap = True
            room_map['b3']['completed'] = True

    else:
        if myPlayer.lantern is False:
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
                type_effect(room_map['b3']['details'])
                skip_two_lines()
                print(CENT(
                    f"          {Fore.CYAN}**You equip the Rusty Dagger**"
                    f"{Fore.WHITE}"))
                room_map['b3']['looked'] = True
        else:
            type_effect(gametext.room_details_combined['b3'])
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
                skip_line()
                print(CENT(
                    f"          {Fore.CYAN}**You found the Map**"
                    f"{Fore.WHITE}"))
                skip_line()
            else:
                type_effect(gametext.room_details_lesser_item['b3'])
            myPlayer.manormap = True
            room_map['b3']['completed'] = True


def library_details():
    if myPlayer.eyeglass:
        type_effect(gametext.room_details_eyeglass['a3'])
        myPlayer.password = True
    else:
        type_effect(gametext.room_details['a3'])


def grand_hall_details():
    if myPlayer.eyeglass:
        type_effect(gametext.room_details_eyeglass['b4'])
        update_player_health(10)
        skip_line()
        print(CENT(f"{Fore.GREEN}  **Your health increases by 10 points**"))
        skip_line()
        type_effect(
            "A kind smile creeps over the girl's face as you pull the key"
            " back out of the painting and place it in your pocket.")
        myPlayer.silver_key = True
        room_map['b4']['completed'] = True
    else:
        type_effect(gametext.room_details['b4'])
        type_effect(CENT(
            "'Return to me when you can see beyond what is shown'\n\n",
        ))


def black_chasm_details():
    if myPlayer.lantern:
        type_effect(gametext.room_details_lantern['a2'])
        room_map['a2']['west'] = 'a1'
        room_map['a2']['completed'] = True
    else:
        type_effect(
            "\nDo you want to step forward into the blackness? (yes/no)"
        )
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            type_effect(gametext.room_details['a2'])
            player_death()
        else:
            main_prompt()


def study_details():
    type_effect(gametext.room_details['a1'])
    type_effect("\nDo you want to open the chest? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.enemy_text['haunted_chest'])
        confirm()
        combat(haunted_chest)
        room_map['a1']['completed'] = True
    else:
        type_effect("You step nervously back from the chest.")


def candlelit_corridor_details():
    type_effect(gametext.room_details['b1'])
    type_effect("\nDo you want to drink the liquid? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.item_text['health_potion'])
        skip_line()
        print(CENT(f"{Fore.GREEN}  **Your health increases by 10 points**"))
        skip_line()
        update_player_health(10)
        room_map['b1']['completed'] = True
    else:
        type_effect(
            "You leave the vial where it is and slide the drawer shut"
            )


def arena_details():
    type_effect(
        f"\n\n'Welcome {myPlayer.name}.\n"
                 )
    type_effect(
        "You spin around to see a tall slender man in a red and gold cloak,"
        "smiling from ear to ear, his feet floating six inches of the ground."
        "\n At the same time, you see all manner of foul creatures scurrying"
        " around the upper levels of the arena, fighting for seats."
    )
    type_effect(
        "The cloked man turns and in a grandiose gesture you see"
        " two unnaturally long, grey-skinned arms emerge from his cloak"
        " into the air before he speaks again:"

        "\n\n'Can we please be upstanding for this evening's main event."
        f"The brave adventurer {myPlayer.name} will take on our undefeated"
        " champion, GOREHOWL!'\n\n"

        "With that, the cloaked man vanishes and you hear a terrifying"
        " guttural growl from the door on the opposite end of the room."
        "\nSuddenly, a huge beast charges forth from the door! You only"
        " get a brief second to take in its huge mass of fur and fangs"
        " before it is upon you!"
    )
    confirm()
    combat(gorehowl)


def alcove_details():
    type_effect(gametext.room_details['c2'])
    myPlayer.eyeglass = True
    room_map['c2']['completed'] = True


def final_door_details():
    if myPlayer.password:
        type_effect(gametext.room_details_password['c1'])
        room_map['c1']['south'] = 'd1'
        room_map['c1']['completed'] = True
    else:
        type_effect(gametext.room_details['c1'])


def riddle_room_details():
    incorrect = 0
    skip_two_lines()
    type_effect(CENT(
        f"'Hello {myPlayer.name},"
        " I thought we'd play a little game before you proceed.'"
        ))
    type_effect(
        "\n\nWith that, the figure vanishes and you hear the unmistakeable"
        " sound of stone grating on stone as the walls begin to close in!"
        " You panic and search the room for an exit but there is none."
        " At that moment, the same voice of the cloaked figure fills"
        " your head:"
        )

    def wallstate(incorrect):
        if incorrect == 1:
            skip_line()
            type_effect(
                "The walls begin to close in on you,"
                " you press your back against one wall"
                " and lift your feet to press against the other"
                " but they continue to advance inwards."
                "\nYou hear the voice again:"
                )
        elif incorrect == 2:
            skip_line()
            type_effect(
                "The walls close in again, pushing against you."
                " You only have a few more seconds left!"
                "\nThe voice comes to you once again:"
                )
        elif incorrect == 3:
            skip_line()
            type_effect(
                "The walls close in one last time, and slam together"
                " with a dull thud."
            )
            player_death()

    def question_one(incorrect):
        type_effect(CENT(
            "\n\n'What always runs but never walks."
            "\n\nOften murmurs, never talks."
            "\n\nHas a bed but never sleeps."
            "\n\nAn open mouth that never eats?'"
            ))
        answer = input('\n\n> ')
        if answer.lower().strip() in [
            'river', 'stream', 'a river', 'a stream', 'the river', 'the stream'
                ]:
            clear()
            type_effect(CENT("'Correct'"))
            confirm()
            type_effect(
                "The walls momentarily slow their advance, and"
                " the voice comes to you again:"
                )
            question_two(incorrect)
        else:
            clear()
            type_effect(CENT("'Heh heh heh, Wrong!'"))
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_one(incorrect)

    def question_two(incorrect):
        type_effect(CENT(
            "\n\n'Heard, I am, but never seen I will be."
            "\n\nI never speak unless you speak to me.'"
            ))
        answer = input('\n\n> ')
        if answer.lower().strip() in [
            'echo', 'an echo', 'the echo', 'a echo',
                ]:
            clear()
            type_effect(CENT("'Correct'"))
            confirm()
            type_effect(
                "The walls momentarily slow their advance, and"
                " the voice comes to you again:"
                )
            question_three(incorrect)
        else:
            clear()
            type_effect(CENT("'Heh heh heh, Wrong!'"))
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_two(incorrect)

    def question_three(incorrect):
        type_effect(CENT(
            "\n\n'Brothers and sisters I have none,"
            "\n\nYet this man's father is my father's son."
            "\n\nWho is he?'"
            ))
        answer = input('\n\n> ')
        if answer.lower().strip() in [
            'son', 'my son', 'your son', 'the son', 'he is my son',
            'he is your son', 'he is the son', "he's my son",
            "he's your son", "he's the son"
                ]:
            clear()
            type_effect(CENT("'Correct'"))
            confirm()
            riddle_complete()
        else:
            clear()
            type_effect(CENT("'Heh heh heh, Wrong!'"))
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_three(incorrect)

    question_one(incorrect)


def riddle_complete():
    type_effect("The walls grind to a stop and you hear the voice again:")
    type_effect(CENT(
        "\n\n'Well, well... it seems you're sharper than I gave you credit"
        " for. I hope we see each other again soon, Heh heh heh heh\n\n"
        ))
    type_effect(
        "\nThe voice's ominous laughter fades and you hear the door"
        " behind you unlock. You also see that a section of the wall on"
        " the west side of the room has folded inwards, opening a"
        " narrow passage leading west"
        )
    room_map['d4']['completed'] = True
    room_map['d4']['west'] = 'd3'
    room_map['d4']['north'] = 'c4'


def goblin_cave_details():
    type_effect(gametext.room_details['d3'])
    type_effect(
        "\n You think you might be able to sneak by without"
        " this creature spotting you..."
        )
    type_effect("\n\nDo you want to try to sneak past? (yes/no)")
    answer = input("\n> ")
    if answer.lower().strip() == 'yes':
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            type_effect(
                "You start to slowly creep forward towards"
                " the cave exit on the west side of the chamber."
                " You walk carefully, step by step through the"
                " light of the creature's campfire and back into the dark."
                " You step forwards and hear a sickening crunch as the"
                " weight of your right foot cracks down through what you"
                " assume to be a pile of rotting bones."
                " You hear a shrill scream and spin around as the goblin"
                " leaps towards you!"
            )
            confirm()
            combat(goblin)
        else:
            type_effect(
                "You start to slowly creep forward towards"
                " the cave exit on the west side of the chamber."
                " You walk carefully, step by step through the"
                " light of the creature's campfire and back into the dark,"
                " and reach the west side of the cave!"
                " You gather by the sounds of the grunting and crunching"
                " still coming from behind you, that the creature remains"
                " unaware of your presence as you proceed out of the cave"
                " and exit to the west."
                )
            confirm()
            room_map['d3']['sneaked'] = True
            room_map['d3']['west'] = 'd2'
            update_player_location('d2')
            main_prompt()


def goblin_cave_description():
    if room_map['d3']['completed']:
        print(
            f"You are back in the"
            f"{gametext.room_descriptions_completed['d3']}"
             )
    else:
        if room_map['d3']['sneaked']:
            goblin_cave_description_sneaked()
        else:
            print((f"{gametext.room_descriptions['d3']}"),)


def goblin_cave_description_sneaked():
    type_effect(gametext.room_descriptions_goblin_attack['d3'])
    confirm()
    combat(goblin)


def altar_details():
    if myPlayer.silver_key:
        type_effect(gametext.room_details_silver_key['d2'])
        skip_two_lines()
        print(CENT(
                f"          {Fore.CYAN}**You equip the Silver Sword**"
                f"{Fore.WHITE}"))
        myPlayer.weapon = 'Silver Sword'
        myPlayer.strength = 8
        room_map['d2']['completed'] = True
    else:
        type_effect(gametext.room_details['d2'])


def final_room_description():
    type_effect(gametext.room_descriptions['d1'])
    type_effect(CENT(
        f"\n\n'Hello again, {myPlayer.name}."
        "\n You've done so well to get here."
        "\n Ah, where are my manners."
        "\n I am the Lord of Fell Manor"
        "\n and it's been such a pleasure having you as my guest this evening."
        "\n So much so, that it would be a shame to have you just"
        "\n walk out of this door, don't you think?"
        "\n Not when there's so much more fun we could have...."
        ))
    skip_line()
    type_effect(CENT("Heh heh heh heh"))
    skip_line()
    type_effect(
        "With that, he spreads wide his long, sickly grey arms"
        " and leaps towards you!"
        )
    confirm()
    combat(manor_lord)


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
    confirm()
    main()


def gorehowl_death():
    type_effect("\n\nYou defeated Gorehowl!\n\n")
    type_effect(gametext.enemy_death['gorehowl'])
    room_map['b2']['completed'] = True


def enemy_death(enemy):
    skip_two_lines()
    type_effect(f"You defeated the {Fore.RED}{enemy.name}{Fore.WHITE}!\n")
    if myPlayer.location == 'a4':
        type_effect(gametext.enemy_death['ogre'])
        update_player_health(10)
        room_map['a4']['completed'] = True
    elif myPlayer.location == 'a1':
        type_effect(gametext.enemy_death['haunted_chest'])
        skip_two_lines()
        print(CENT(
                f"          {Fore.CYAN}**You equip the Iron Shield**"
                f"{Fore.WHITE}"))
        myPlayer.shield = 'Iron Shield'
        myPlayer.armour = 6
        room_map['a1']['completed'] = True
    elif myPlayer.location == 'b2':
        type_effect(gametext.enemy_death['gorehowl'])
        room_map['b2']['completed'] = True
        room_map['b2']['south'] = 'c2'
    elif myPlayer.location == 'd3':
        type_effect(gametext.enemy_death['goblin'])
        room_map['d3']['completed'] = True
        room_map['d3']['west'] = 'd2'
    elif myPlayer.location == 'd1':
        type_effect(gametext.enemy_death['manor_lord'])
        confirm()
        credits_screen()


def game_begin_message():
    type_effect(f"You awake in a {room_map[myPlayer.location]['description']}")


def calculate_valid_directions():
    directions_list = []
    for key, value in room_map[myPlayer.location].items():
        if key in ['north', 'south', 'east', 'west']:
            if value is not False:
                directions_list.append(key)
    type_effect("you can travel: \n", 0.003)
    for direction in directions_list:
        print(f"{Fore.GREEN}{direction}{Fore.WHITE}")
    return directions_list


def main_prompt():
    skip_line()
    if myPlayer.manormap is False:
        print("-----------------------------------------------------")
        print(
            f"You can {Fore.GREEN}'look' {Fore.WHITE}around"
            " the room for more information,"
            )
        print(f"type {Fore.GREEN}'items' {Fore.WHITE} to view your items"
              " & health, or")
    else:
        print("-----------------------------------------------------")
        print(
            f"You can {Fore.GREEN}'look' {Fore.WHITE}around"
            " the room for more information,"
            )
        print(f"type {Fore.GREEN}'items' {Fore.WHITE} to view your items"
              " & health,")
        print(f"type {Fore.GREEN}'map'{Fore.WHITE} to view the map, or")
    directions_list = calculate_valid_directions()
    print("\n")
    type_effect("What would you like to do?\n", 0.003)
    answer = input("> ")
    if answer.lower().strip() in directions_list:
        update_player_location(room_map[myPlayer.location][f"{answer}"])
    elif answer.lower().strip() == 'look':
        clear()
        print_room_details()
    elif answer.lower().strip() == 'items':
        clear()
        inventory_screen()
    elif answer.lower().strip() == 'map':
        if myPlayer.manormap:
            clear()
            display_map()

    main_prompt()


def lantern_prompt():
    skip_line()
    type_effect("\nDo you want to try to grab the lantern? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        lantern_attempt()
    else:
        main_prompt()


def lantern_attempt():
    rng = random.randint(1, 3)
    if rng <= 2:
        clear()
        type_effect(gametext.item_text['lantern_success'])
        skip_line()
        print(CENT(
                    f"          {Fore.CYAN}**You found the Lantern**"
                    f"{Fore.WHITE}"))
        myPlayer.lantern = True
        room_map['c4']['completed'] = True
    else:
        clear()
        type_effect(gametext.item_text['lantern_failure'])
        update_player_health(-1)
        skip_line()
        type_effect("\nDo you want to try again? (yes/no)")
        answer = input("\n> ")
        if answer.lower().strip() == 'yes':
            lantern_attempt()
        else:
            main_prompt()


def dining_room_prompt():
    type_effect(f"{gametext.room_details['a4']}")
    type_effect("\nDo you take a bite? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(
            "You take a bite of the bread, it is astonishingly tasty,"
            " fluffy and warm, yet delightfully crunchy."
            )
        skip_line()
        print(CENT(f"{Fore.GREEN}  **Your health increases by 2 points**"))
        update_player_health(2)
        skip_two_lines()
        type_effect(gametext.enemy_text['ogre'])
        confirm()
        combat(ogre)


def game_instructions():
    clear()
    print(CENT("You must escape from Fell Manor!"))
    print(CENT(
        f"     To move from room to room, type {Fore.GREEN}'north', 'south'"
        ))
    print(CENT(
        f"           {Fore.GREEN}'east' {Fore.WHITE}or "
        f"{Fore.GREEN}'west' {Fore.WHITE}when prompted."
        ))
    skip_line()
    print(CENT(
        f"        You can also type {Fore.GREEN}'look' {Fore.WHITE}to examine"
        ))
    print(CENT("the room you are in for more information"))
    skip_line()
    print(CENT("Many challenges await you,\n"))
    print(CENT("Good Luck!"))
    skip_two_lines()
    confirm()
    clear()
    game_begin_message()
    main_prompt()


def combat(enemy):
    clear()
    print(f"\nThe {Fore.RED}{enemy.name} attacks!")
    enemy_attack_strength = (
        random.randint(0, 4) + enemy.strength - myPlayer.armour
    )
    if enemy_attack_strength < 0:
        enemy_attack_strength = 0
    time.sleep(0.4)
    print(
        f"\nThe {Fore.RED}{enemy.name}{Fore.WHITE}hits you for "
        f"{Fore.RED}{enemy_attack_strength}{Fore.WHITE} damage!"
        )
    time.sleep(0.4)
    print(f"\nYour health was at {Fore.RED}{myPlayer.health}{Fore.WHITE}")
    print(
        f"\nafter that attack, it's now at "
        f"{Fore.RED}{myPlayer.health - enemy_attack_strength}"
        )
    update_player_health(enemy_attack_strength * -1)

    input(f"\nPress {Fore.GREEN}ENTER {Fore.WHITE}to attack!")
    clear()
    if myPlayer.weapon == 'No Weapon':
        type_effect(f"\nYou attack the {enemy.name} with your bare fists!")
    else:
        type_effect(
            f"\nYou attack the{Fore.RED}{enemy.name}{Fore.WHITE}"
            f" with your {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}!"
            )
    attack_strength = random.randint(0, 4) + myPlayer.strength - enemy.armour
    if attack_strength < 0:
        attack_strength = 0
    print(
        f"\nYou hit the{Fore.RED}{enemy.name}{Fore.WHITE}"
        f" for {attack_strength} damage!"
        )
    print(
        f"\nThe{Fore.RED}{enemy.name}'s{Fore.WHITE}"
        f" health was at {Fore.RED}{enemy.health}{Fore.WHITE}"
        )
    print(
        "\nAfter that attack, it's now at "
        f"{Fore.RED}{enemy.health - attack_strength}"
        )
    update_enemy_health(enemy, attack_strength * -1)

    if enemy.health <= 0:
        return
    else:
        input(f"\nPress {Fore.GREEN}ENTER {Fore.WHITE}to continue!")
        combat(enemy)


def credits_screen():
    time.sleep(2)
    clear()
    update_hof()
    type_effect(CENT(
        "\n\nCONGRATULTIONS, You have completed Escape From Fell Manor!"
        " \n\nYour name has been added to the Hall of Fame,"
        "\n a list of all those courageous adventurers who have braved"
        "\n Fell Manor and lived to tell the tale!"
        ))
    confirm()
    clear()
    type_effect(
        "\n\nI hope you have enjoyed Escape From Fell Manor"
        "\n\nRe-run the programme to see your entry in the Hall of Fame!"
        "\n Thanks for playing!"
        "\n\n                     -Lewis D"

        )
    confirm()
    main()


def main():
    display_title_screen()


main()
