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


LINE = '-----------------------------------------------------'


def type_effect(text, speed=0.04):
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
        print(f"{Fore.RED}{Style.NORMAL} ", end="", flush=True)
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
    color_type(TITLE, 'red', 0.003)
    print(f"{Fore.RESET}")
    confirm()
    display_main_menu()


def display_main_menu():
    """
    Displays the main menu
    """
    clear()
    MAIN_MENU = art.MAIN_MENU
    type_effect(MAIN_MENU, 0.003)
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
        name_request()
    elif option.lower().strip() == ('help'):
        help_screen()
    elif option.lower().strip() == ('quit'):
        quit_game()
    elif option.lower().strip() == ('hall of fame'):
        display_hof()
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
        "\nThese are the mighty adventurers who braved"
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
gorehowl = Monster('Arena Beast', 18, 6, 1)
manor_lord = Monster('Lord of Fell Manor', 20, 7, 2)


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
          "that you have \ngathered on your journey so far:")
    print(LINE)
    if myPlayer.weapon == 'Rusty Dagger':
        print(
            f"Weapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}"
            f"-- +{rusty_dagger.strength - 2} damage"
            )
    elif myPlayer.weapon == 'Silver Sword':
        print(
            f"Weapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}"
            f"-- +{silver_sword.strength - 2} damage"
            )
    else:
        print(f"Weapon: {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}")

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
    print(LINE)
    input(CENT(
        f"            -- Press {Fore.GREEN}ENTER {Fore.WHITE}to continue --"
        ))
    clear()
    print_room_description()


def display_map():
    print(f"{map_dict[myPlayer.location]}")
    confirm()


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


def name_request():
    clear()
    type_effect("What is your name,")
    color_type("victim", 'red')
    time.sleep(0.25)
    type_effect('\b\b\b\b\b\b\b', 0.03)
    type_effect('brave adventurer?')
    answer = input('\n> ')
    if validate_name(answer):
        myPlayer.name = answer
        game_introduction()
        return answer

    else:
        name_request()


def game_introduction():
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
        type_effect("You have found all there is to find in this room", 0.01)

    elif myPlayer.location == 'b3':
        storage_room_details()

    elif myPlayer.location == 'b4':
        grand_hall_details()

    elif myPlayer.location == 'a3':
        library_details()

    elif myPlayer.location == 'a4':
        type_effect(gametext.room_details['a4'])
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
            skip_line()
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
                skip_line()
                print(CENT(
                    f"          {Fore.CYAN}**You equip the Rusty Dagger**"
                    f"{Fore.WHITE}"))
                room_map['b3']['looked'] = True
        else:
            type_effect(gametext.room_details_combined['b3'])
            confirm()
            type_effect(
                f"{Fore.WHITE}Not only that, but with the aid of your lantern"
                "\nyou find, at the bottom of an old, rotting"
                "\nwooden crate, a rolled-up scroll of parchment."
                "\nYou carefully unravel and examine it. It's a map"
                "\nof Fell Manor!"
                "\n\nYou can now type 'map' when prompted to see a map of"
                "\nFell Manor's rooms."
            )
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
                skip_line()
                print(CENT(
                    f"          {Fore.CYAN}**You found the Map**"
                    f"{Fore.WHITE}"))
                confirm()
                skip_line()
            else:
                type_effect(gametext.room_details_lesser_item['b3'])
            myPlayer.manormap = True
            room_map['b3']['completed'] = True


def library_details():
    if myPlayer.eyeglass:
        type_effect(gametext.room_details_eyeglass['a3'])
        confirm()
        type_effect(
            "\nSure enough, the script begins to change as it did before,"
            "\nallowing you to decipher the book's contents"
            "\nYou skim along the pages of the book before stopping at a"
            "\npage containing only two words, \n'Password'\n and directly"
            " below it, \n'Ajagar'\n"
            "You make careful note of this word and slam the book shut.",
        )
        myPlayer.password = True
        room_map['a3']['completed'] = True
    else:
        type_effect(gametext.room_details['a3'])


def grand_hall_details():
    if myPlayer.eyeglass:
        type_effect(gametext.room_details_eyeglass['b4'])
        update_player_health(10)
        skip_line()
        print(CENT(
            f"{Fore.GREEN}  **Your health increases by 10 points**{Fore.WHITE}"
            ))
        confirm()
        type_effect(
            "A kind smile creeps over the girl's face as you pull the key"
            "\nback out of the painting and place it in your pocket.")
        skip_line()
        print(CENT(
                f"          {Fore.CYAN}**You found the Silver Key**"
                f"{Fore.WHITE}"))
        myPlayer.silver_key = True
        room_map['b4']['completed'] = True
    else:
        type_effect(gametext.room_details['b4'])
        confirm()
        type_effect(
            "\nAs you peer into the painting, you realise that there is a"
            "\nvoice coming from it!"
            "\nYou press your ear close to it and try to make out what"
            "\nit is saying...",
          )
        type_effect(CENT(
            "\n\n'Return to me when you can see beyond what is shown'\n\n",
        ))


def black_chasm_details():
    if myPlayer.lantern:
        type_effect(gametext.room_details_lantern['a2'])
        room_map['a2']['west'] = 'a1'
        room_map['a2']['completed'] = True
    else:
        black_chasm_prompt()


def black_chasm_prompt():
    clear()
    skip_line()
    type_effect(
            "Do you want to step forward into the"
            f" blackness?"
            f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            clear()
            type_effect(gametext.room_details['a2'])
            player_death()
        elif answer[0].lower().strip() == 'n':
            clear()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        black_chasm_prompt()


def study_details():
    type_effect(gametext.room_details['a1'])
    study_prompt()


def study_prompt():
    skip_line()
    type_effect(
        "Do you want to open the chest?"
        f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            clear()
            type_effect(gametext.enemy_text['haunted_chest'])
            confirm()
            combat(haunted_chest)
            room_map['a1']['completed'] = True
        elif answer[0].lower().strip() == 'n':
            clear()
            type_effect("You step nervously back from the chest.")
            confirm()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        study_prompt()


def candlelit_corridor_details():
    type_effect(gametext.room_details['b1'])
    potion_prompt()


def potion_prompt():
    skip_line()
    type_effect(
        "Do you want to drink the liquid?"
        f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            clear()
            type_effect(gametext.item_text['health_potion'])
            confirm()
            skip_line()
            print(CENT(
                f"{Fore.GREEN}  **Your health increases by "
                f"10 points**{Fore.WHITE}"
            ))
            update_player_health(10)
            room_map['b1']['completed'] = True
        elif answer[0].lower().strip() == 'n':
            clear()
            type_effect(
                "You leave the vial where it is and slide the drawer shut"
                )
            confirm()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        potion_prompt()


def arena_details():
    skip_line()
    type_effect(
        f"{Fore.MAGENTA}'Welcome {myPlayer.name}.'{Fore.WHITE}\n"
                 )
    confirm()
    skip_line()
    type_effect(
        "You spin around to see a tall slender man in a purple cloak,"
        "\nsmiling from ear to ear, his feet floating six inches off the"
        " ground."
        "\nAt the same time, you see all manner of foul creatures scurrying"
        "\naround the upper levels of the arena, fighting for seats."
    )
    type_effect(
        "\nThe cloked man turns and in a grandiose gesture you see"
        "\ntwo unnaturally long, grey-skinned arms emerge from his cloak"
        "\ninto the air before he speaks again:"
    )
    skip_line()
    color_type(
        "\n'Can we please be upstanding for this evening's main event."
        f"\nThe brave adventurer {myPlayer.name} will take on our undefeated"
        "\nchampion, The Arena Beast: GOREHOWL!'", 'magenta'
    )
    skip_line()
    type_effect(
        "With that, the cloaked man vanishes and you hear a terrifying"
        "\nguttural growl from the door on the opposite end of the room."
        "\nSuddenly, a huge beast charges forth from the door! You only"
        "\nget a brief second to take in its huge mass of fur and fangs"
        "\nbefore it is upon you!"
    )
    confirm()
    combat(gorehowl)


def alcove_details():
    type_effect(gametext.room_details['c2'])
    skip_line()
    type_effect(CENT("'See beyond what is shown'"))
    confirm()
    skip_line()
    print(CENT(
                f"          {Fore.CYAN}**You found the Eyeglass**"
                f"{Fore.WHITE}"))
    myPlayer.eyeglass = True
    room_map['c2']['completed'] = True


def final_door_details():
    if myPlayer.password:
        type_effect(gametext.room_details_password['c1'])
        confirm()
        type_effect(
            "\nKnowing the password, you speak the word:"
            "\n\n'Ajagar'\n"
            "\nThe wooden face grimaces, snapping and creaking as the door"
            "\nslowly swings open. Through it you can see Fell Manor's"
            "\nfinal room, and beyond it, the door to your escape..."
            "\n\n **The entrance to the south is now open**\n"
        )
        room_map['c1']['south'] = 'd1'
        room_map['c1']['completed'] = True
    else:
        type_effect(gametext.room_details['c1'])
        confirm()
        type_effect(
          "\n\nYou stare blankly back for a moment before realising that"
          "\nit is expecting an answer from you. "
          "\nYou try to think of what this password could be but nothing"
          "\ncomes to your mind. Perhaps there is a clue hidden somewhere"
          "\nin another room..."
          "\n\nYou step away from the door and the face's eyes slowly"
          "\nclose shut again. Its features sinking back into the surface of"
          "\nthe huge door."
        )


def riddle_room_details():
    incorrect = 0
    confirm()
    color_type(
            f"'Hello, {myPlayer.name}."
            "I thought we'd play a little game before you proceed.'", 'magenta'
            )
    type_effect(
        "\n\nWith that, the figure vanishes and you hear the unmistakeable"
        "\nsound of stone grating on stone as the walls begin to close in!"
        "\nYou panic and search the room for an exit but there is none."
        "\nAt that moment, the same voice of the cloaked figure fills"
        " your head:"
        )

    def wallstate(incorrect):
        if incorrect == 1:
            skip_line()
            type_effect(
                "The walls begin to close in on you,"
                "\nyou press your back against one wall"
                "\nand lift your feet to press against the other"
                "\nbut they continue to advance inwards."
                "\nYou hear the voice again:"
                )
        elif incorrect == 2:
            skip_line()
            type_effect(
                "The walls close in again, pushing against you."
                "\nYou only have a few more seconds left!"
                "\nThe voice comes to you once again:"
                )
        elif incorrect == 3:
            skip_line()
            type_effect(
                "The walls close in one last time, and slam together"
                "\nwith a dull thud."
            )
            player_death()

    def question_one(incorrect):
        color_type(
            "\n\n'What always runs but never walks."
            "\n\nOften murmurs, never talks."
            "\n\nHas a bed but never sleeps."
            "\n\nAn open mouth that never eats?\n'", 'magenta'
            )
        answer = input('\n> ')
        if answer.lower().strip() in [
            'river', 'stream', 'a river', 'a stream', 'the river', 'the stream'
                ]:
            clear()
            skip_line()
            print(CENT(f"{Fore.MAGENTA}       'Correct'{Fore.WHITE}"))
            confirm()
            type_effect(
                "The walls momentarily slow their advance, and"
                "\nthe voice comes to you again:"
                )
            question_two(incorrect)
        else:
            clear()
            color_type("'Heh heh heh, Wrong!'", 'magenta')
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_one(incorrect)

    def question_two(incorrect):
        color_type(
            "\n\n'Heard, I am, but never seen I will be."
            "\n\nI never speak unless you speak to me.'"
            "\n\n In empty air I fly and fly"
            "\n\n If asked, I give the same reply", 'magenta'
            )
        answer = input('\n\n> ')
        if answer.lower().strip() in [
            'echo', 'an echo', 'the echo', 'a echo',
                ]:
            clear()
            skip_line()
            print(CENT(f"{Fore.MAGENTA}       'Correct'{Fore.WHITE}"))
            confirm()
            type_effect(
                "The walls momentarily slow their advance, and"
                "\nthe voice comes to you again:"
                )
            question_three(incorrect)
        else:
            clear()
            color_type("'Heh heh heh, Wrong!'", 'magenta')
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_two(incorrect)

    def question_three(incorrect):
        color_type(
            "\n\n'Brothers and sisters I have none,"
            "\n\nYet this man's father is my father's son."
            "\n\nWho is he?'", 'magenta'
            )
        answer = input('\n\n> ')
        if answer.lower().strip() in [
            'son', 'my son', 'your son', 'the son', 'he is my son',
            'he is your son', 'he is the son', "he's my son",
            "he's your son", "he's the son"
                ]:
            clear()
            skip_line()
            print(CENT(f"{Fore.MAGENTA}       'Correct'{Fore.WHITE}"))
            confirm()
            riddle_complete()
        else:
            clear()
            color_type("'Heh heh heh, Wrong!'", 'magenta')
            incorrect = incorrect + 1
            wallstate(incorrect)
            question_three(incorrect)

    question_one(incorrect)


def riddle_complete():
    type_effect("The walls grind to a stop and you hear the voice again:")
    color_type(
        "\n\n'Well, well... it seems you're sharper than I gave you credit"
        "\nfor. I hope we see each other again soon,"
        "\nHeh heh heh heh\n\n", 'magenta'
        )
    confirm()
    clear()
    type_effect(
        "\nThe voice's ominous laughter fades and you hear the door"
        "\nbehind you unlock. You also see that a section of the wall on"
        "\nthe west side of the room has folded inwards, opening a"
        "\nnarrow passage leading west"
        )
    room_map['d4']['completed'] = True
    room_map['d4']['west'] = 'd3'
    room_map['d4']['north'] = 'c4'


def goblin_cave_details():
    type_effect(gametext.room_details['d3'])
    type_effect(
        "\nYou think you might be able to sneak by without"
        "\nthis creature spotting you..."
        )
    goblin_prompt()


def goblin_prompt():
    skip_line()
    type_effect(
        "Do you want to try to sneak past?"
        f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            coinflip = random.randint(1, 2)
            if coinflip == 1:
                clear()
                type_effect(
                 "You start to slowly creep forward towards"
                 "\nthe cave exit on the west side of the chamber."
                 "\nYou walk carefully, step by step through the"
                 "\nlight of the creature's campfire and back into the dark."
                 "\nYou step forwards and hear a sickening crunch as the"
                 "\nweight of your right foot cracks down through what you"
                 "\nassume to be a pile of rotting bones."
                 f"\nYou hear a shrill scream and spin around as the "
                 f"\n{Fore.RED}goblin{Fore.WHITE} leaps towards you!"
                )
                confirm()
                combat(goblin)
            else:
                clear()
                type_effect(
                  "You start to slowly creep forward towards"
                  "\nthe cave exit on the west side of the chamber."
                  "\nYou walk carefully, step by step through the"
                  "\nlight of the creature's campfire and back into the dark,"
                  "\nand reach the west side of the cave!"
                  "\nYou gather by the sounds of the grunting and crunching"
                  "\nstill coming from behind you, that the creature remains"
                  "\nunaware of your presence as you proceed out of the cave"
                  "\nand exit to the west."
                 )
                confirm()
                room_map['d3']['sneaked'] = True
                room_map['d3']['west'] = 'd2'
                update_player_location('d2')
                main_prompt()
        elif answer[0].lower().strip() == 'n':
            clear()
            type_effect(
                "You creep backwards to the cave entrance"
                )
            confirm()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        goblin_prompt()


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
        skip_line()
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
    color_type(
        f"\n\n'Hello again, {myPlayer.name}."
        "\nYou've done so well to get here."
        "\nAh, where are my manners."
        "\nI am the Lord of Fell Manor"
        "\nand it's been such a pleasure having you as my guest this evening."
        "\nSo much so, that it would be a shame to have you just"
        "\nwalk out of this door, don't you think?"
        "\nNot when there's so much more fun we could have....'", 'magenta'
        )
    skip_line()
    color_type("'Heh heh heh heh'", 'red', 0.2)
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
    skip_two_lines()
    type_effect(f"{Fore.RED}You Died....{Fore.WHITE}")
    confirm()
    main()


def gorehowl_death():
    type_effect("\n\nYou defeated Gorehowl!\n\n")
    type_effect(gametext.enemy_death['gorehowl'])
    room_map['b2']['completed'] = True


def enemy_death(enemy):
    confirm()
    clear()
    type_effect(f"You defeated the {Fore.RED}{enemy.name}{Fore.WHITE}!\n")
    if myPlayer.location == 'a4':
        type_effect(gametext.enemy_death['ogre'])
        update_player_health(15)
        room_map['a4']['completed'] = True
    elif myPlayer.location == 'a1':
        type_effect(gametext.enemy_death['haunted_chest'])
        skip_line()
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
        print(LINE)
        print(
            f"You can {Fore.GREEN}'look' {Fore.WHITE}around"
            " the room for more information,"
            )
        print(f"type {Fore.GREEN}'items' {Fore.WHITE} to view your items"
              " & health, or")
    else:
        print(LINE)
        print(
            f"You can {Fore.GREEN}'look' {Fore.WHITE}around"
            " the room for more information,"
            )
        print(f"type {Fore.GREEN}'items' {Fore.WHITE} to view your items"
              " & health,")
        print(f"type {Fore.GREEN}'map'{Fore.WHITE} to view the map, or")
    directions_list = calculate_valid_directions()
    print("\n")

    choices = ['look', 'l', 'items', 'i', ]
    if myPlayer.manormap:
        choices.append('map')
        choices.append('m')
    for direction in directions_list:
        choices.append(direction)
        choices.append(direction[0])

    type_effect("What would you like to do?", 0.003)
    answer = input("\n> ")
    if validate_choice(answer, choices):

        if answer.lower().strip() == 'north' or answer.lower().strip() == 'n':
            update_player_location(room_map[myPlayer.location][f"{'north'}"])

        elif answer.lower().strip() == 'south' or \
                answer.lower().strip() == 's':
            update_player_location(room_map[myPlayer.location][f"{'south'}"])

        elif answer.lower().strip() == 'east' or answer.lower().strip() == 'e':
            update_player_location(room_map[myPlayer.location][f"{'east'}"])

        elif answer.lower().strip() == 'west' or answer.lower().strip() == 'w':
            update_player_location(room_map[myPlayer.location][f"{'west'}"])

        elif answer.lower().strip() == 'look' or answer.lower().strip() == 'l':
            clear()
            print_room_details()
        elif answer.lower().strip() == 'items' or \
                answer.lower().strip() == 'i':
            clear()
            inventory_screen()
        elif answer.lower().strip() == 'map' or answer.lower().strip() == 'm':
            if myPlayer.manormap:
                clear()
                display_map()
    else:
        print_room_description()
    main_prompt()


def lantern_prompt():
    skip_line()
    type_effect(
        "Do you want to try to grab the lantern?"
        f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            lantern_attempt()
        elif answer[0].lower().strip() == 'n':
            clear()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        lantern_prompt()


def lantern_attempt():
    rng = random.randint(1, 3)
    if rng <= 2:
        clear()
        type_effect(gametext.item_text['lantern_success'])
        skip_line()
        confirm()
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
        type_effect(
            "Do you want to try again?"
            f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
            )
        answer = input("\n> ")
        if validate_yes_or_no(answer):
            if answer[0].lower().strip() == 'y':
                lantern_attempt()
            elif answer[0].lower().strip() == 'n':
                clear()
                room_map[myPlayer.location]['entered'] = False
                print_room_description()
                room_map[myPlayer.location]['entered'] = True
                main_prompt()
        else:
            lantern_prompt()


def dining_room_prompt():
    skip_line()
    type_effect(
        "Do you take a bite?"
        f" ({Fore.GREEN}yes{Fore.WHITE}/{Fore.GREEN}no{Fore.WHITE})"
        )
    answer = input("\n> ")
    if validate_yes_or_no(answer):
        if answer[0].lower().strip() == 'y':
            clear()
            type_effect(
                "You take a bite of the bread, it is astonishingly tasty,"
                "\nfluffy and warm, yet delightfully crunchy."
                )
            skip_line()
            print(CENT(
                f"{Fore.GREEN}  **Your health increases"
                f" by 2 points**{Fore.WHITE}"
                ))
            update_player_health(2)
            skip_line()
            type_effect(gametext.enemy_text['ogre'])
            confirm()
            combat(ogre)

        elif answer[0].lower().strip() == 'n':
            clear()
            type_effect(
                "You resist the temptation, for now..."
                )
            confirm()
            room_map[myPlayer.location]['entered'] = False
            print_room_description()
            room_map[myPlayer.location]['entered'] = True
            main_prompt()
    else:
        dining_room_prompt()


def game_instructions():
    clear()
    skip_line()
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
    print(f"\nThe {Fore.RED}{enemy.name}{Fore.WHITE} attacks!")
    enemy_attack_strength = (
        random.randint(0, 4) + enemy.strength - myPlayer.armour
    )
    if enemy_attack_strength < 0:
        enemy_attack_strength = 0
    time.sleep(0.8)
    print(
        f"\nThe {Fore.RED}{enemy.name}{Fore.WHITE} hits you for "
        f"{Fore.RED}{enemy_attack_strength}{Fore.WHITE} damage!"
        )
    time.sleep(0.8)
    print(f"\nYour health was at {Fore.RED}{myPlayer.health}{Fore.WHITE}")
    print(
        f"\nafter that attack, it's now at "
        f"{Fore.RED}{myPlayer.health - enemy_attack_strength}{Fore.WHITE}"
        )
    update_player_health(enemy_attack_strength * -1)

    input(f"\n-- Press {Fore.GREEN}ENTER {Fore.WHITE}to attack! --")
    clear()
    if myPlayer.weapon == 'No Weapon':
        type_effect(f"\nYou attack the {enemy.name} with your bare fists!")
    else:
        type_effect(
            f"\nYou attack the {Fore.RED}{enemy.name}{Fore.WHITE}"
            f" with your {Fore.CYAN}{myPlayer.weapon}{Fore.WHITE}!"
            )
    attack_strength = random.randint(0, 4) + myPlayer.strength - enemy.armour
    if attack_strength < 0:
        attack_strength = 0
    time.sleep(0.8)
    print(
        f"\n\nYou hit the {Fore.RED}{enemy.name}{Fore.WHITE}"
        f" for {attack_strength} damage!"
        )
    time.sleep(0.8)
    print(
        f"\nThe {Fore.RED}{enemy.name}'s{Fore.WHITE}"
        f" health was at {Fore.RED}{enemy.health}{Fore.WHITE}"
        )
    print(
        "\nAfter that attack, it's now at "
        f"{Fore.RED}{enemy.health - attack_strength}{Fore.WHITE}"
        )
    update_enemy_health(enemy, attack_strength * -1)

    if enemy.health <= 0:
        return
    else:
        input(f"\n-- Press {Fore.GREEN}ENTER {Fore.WHITE}to continue! --")
        combat(enemy)


def credits_screen():
    clear()
    update_hof()
    type_effect(CENT(
        "\n\n       CONGRATULTIONS, You have completed Escape From Fell Manor!"
        " \n\n            Your name has been added to the Hall of Fame,"
        "\n         a list of all those courageous adventurers who have braved"
        "\n               Fell Manor and lived to tell the tale!"
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


# Validator Functions ###########################
def validate_name(answer):
    try:
        if not answer.isalpha() or len(answer) < 2 or len(answer) > 15:
            raise ValueError
    except ValueError:
        clear()
        print(
            f'{Fore.RED}Error: "{answer}" is not'
            f' an acceptable name{Fore.WHITE}'
            )
        print('Please choose a name that is 2-15 letters')
        confirm()
        clear()
        return False

    return True


def validate_yes_or_no(answer):
    try:
        if len(answer) == 0:
            raise ValueError
        if answer[0].lower() != "y" and answer[0].lower() != "n":
            raise ValueError
    except ValueError:
        clear()
        print(
            f"{Fore.RED}Error: You answered '{answer}', please"
            f" type {Fore.GREEN}'yes' {Fore.RED}or {Fore.GREEN}'no'"
            f"{Fore.WHITE}"
            )
        confirm()
        clear()
        return False

    return True


def validate_choice(answer, choices):
    try:
        if answer not in choices:
            raise ValueError
    except ValueError:
        clear()
        print(f"{Fore.RED}Error: '{answer}' is not a valid input{Fore.WHITE}")
        confirm()
        clear()
        return False

    return True


def main():
    display_title_screen()


main()
