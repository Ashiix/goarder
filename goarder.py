#!/usr/bin/env python3

# Goarder v1.0
# by Ashiix

from goarderEngines import *
stats = stats()
import sys

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

stats.name = input("What is your name?\nName>>> ")
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
    else:
        print("That is not a valid choice. Please re-enter.")

if stats.gender == 'M':
    print("\nWelcome, Sir", stats.name + ". Goarder is currently in very early alpha, and the game is always being developed, if you find any issues with the game, or have any recommended features, please, drop a bug report on Github. Thanks.")
if stats.gender == 'F':
    print("\nWelcome, Ma'am", stats.name + ". Goarder is currently in very early alpha, and the game is always being developed, if you find any issues with the game, or have any recommended features, please, drop a bug report on Github. Thanks.")


while True:

    actionChosen = input("\nWould you like to... explore (1), heal (2), open inventory (3), check paladin stats (4), play the story (5) [HUGE WIP], or exit the game (6).\nAction>>> ")

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
        print("You are leaving with",str(stats.goldCount)+", and",str(stats.XPtotal),"XP.")
        sys.exit("Goodbye!\n")
    else:
        print("That is not a valid choice. Please re-enter.")
