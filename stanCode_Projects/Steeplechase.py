"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East.
    Post-condition: Karel is on the right side of the wall. 
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing East.
    Post-condition: Karel is facing North.
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def cross():
    """
    Pre-condition: Karel is at the upper left of the wall, facing North.
    Post-condition: Karel is at the upper right of the wall, facing South.
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    Pre-condition: Karel is at the upper right of the wall, facing South.
    """
    while front_is_clear():
        move()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
