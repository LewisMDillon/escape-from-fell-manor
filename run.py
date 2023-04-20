# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import sys
import art

TITLE = art.TITLE


def type_print(text, speed=0.03):
    '''
    Function for typewriter effect for printing the text
    with variable speed, 0.03 speed by default
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


type_print(TITLE, 0.002)
