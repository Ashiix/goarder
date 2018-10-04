#!/usr/bin/env python3

# Goarder v1.0
# by nitel

from goarderCombatEngine import combat
from goarderCombatEngine import rest

firstAct = True

print("\nHello, paladin. Welcome to Goarder alpha!\n")

while True:
    global crusaderHP
    global goldCount
    if firstAct == True:
        goldCount = 0
        crusaderHP = 50
        firstAct = False

    actionChosen = input("\nWould you like to... explore (1), heal (2), open inventory (3) [WIP], check paladin stats (4) [WIP].\n")
    if actionChosen == '1':
        combat()
    elif actionChosen == '2':
        rest()
    elif actionChosen == '3':
        print("Inventory")
    elif actionChosen == '4':
        print("Paladin Stats")

    else:
        print("That is not a valid choice. Please re-enter.")
