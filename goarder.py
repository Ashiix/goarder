#!/usr/bin/env python3

# Goarder v1.0
# by Ashiix

from goarderEngines import *
import sys
import random as rng

print("\n                                            ___ ")
print("\n                                           (   )")
print("\n  .--.     .--.     .---.   ___ .-.      .-.| |    .--.    ___ .-.")
print("\n /    \   /    \   / .-, \ (   )   \    /   \ |   /    \  (   )   \\")
print("\n;  ,-. ' |  .-. ; (__) ; |  | ' .-. ;  |  .-. |  |  .-. ;  | ' .-. ;")
print("\n| |  | | | |  | |   .'`  |  |  / (___) | |  | |  |  | | |  |  / (___)")
print("\n| |  | | | |  | |  / .'| |  | |        | |  | |  |  |/  |  | |")
print("\n| |  | | | |  | | | /  | |  | |        | |  | |  |  ' _.'  | |")
print("\n| '  | | | '  | | ; |  ; |  | |        | '  | |  |  .'.-.  | |")
print("\n'  `-' | '  `-' / ' `-'  |  | |        ' `-'  /  '  `-' /  | |")
print("\n `.__. |  `.__.'  `.__.'_. (___)        `.__,'    `.__.'  (___)")
print("\n ( `-' ;")
print("\n  `.__.\n")

print("\nHello, paladin. Welcome to Goarder alpha!\n")

if readSave():
    stats.name = input("What is your name?\nName>>> ")
    if stats.name == "" or stats.name == " ":
        stats.name = "Paladin"
        print("Do to your lack of care about your name, it has been set to Paladin.")

    while True:
        stats.gender = input("Are you male (M) or female (F)?\nGender>>> ")
        if stats.gender == 'M' or stats.gender == 'F':
            break
        elif stats.gender == 'm':
            stats.gender = 'M'
            break
        elif stats.gender == 'f':
            stats.gender = 'F'
            break
        elif stats.gender == '':
            print("Randomly selecting gender...")
            ranGend = rng.randint(1,2)
            if ranGend == 1:
                stats.gender = 'M'
                print("You have been chosen as male.")
                break
            elif ranGend == 2:
                stats.gender = 'F'
                print("You have been chosen as female")
                break
            else:
                sys.exit("Something bad just happened, whine on the GitHub page about how it did.")
        else:
            print("That is not a valid choice. Please re-enter.")

if stats.gender == 'M':
    print("\nWelcome, Sir", stats.name + ". Goarder is currently in very early alpha, and the game is always being developed, if you find any issues with the game, or have any recommended features, please, drop a bug report on Github. Thanks.")
if stats.gender == 'F':
    print("\nWelcome, Ma'am", stats.name + ". Goarder is currently in very early alpha, and the game is always being developed, if you find any issues with the game, or have any recommended features, please, drop a bug report on Github. Thanks.")


while True:

    actionChosen = input("\nWould you like to... explore (1), heal (2), open inventory (3), check paladin stats (4), play the story (5) [HUGE WIP], exit the game (6), or save your game (7).\nAction>>> ")

    if actionChosen == '1':
        combat()
    elif actionChosen == '2':
        rest()
    elif actionChosen == '3':
        inventory()
    elif actionChosen == '4':
        statMenu()
    elif actionChosen == '5':
        print("\nStory is a WIP")
        # story()
    elif actionChosen == '6':
        print("You are leaving with",str(stats.goldCount),"gold, and",str(stats.XPtotal),"XP.")
        sys.exit("Goodbye!\n")
    elif actionChosen == '7':
        save()
        print("File saved in slot 1.")
    else:
        print("That is not a valid choice. Please re-enter.")
