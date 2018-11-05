#!/usr/bin/env python3

# goarderEngines v1.0
# by nitel

global paladinHP
paladinHP = 50
goldCount = 0

from goarderItems import *
inventory = items()

paladinHelm = inventory.paladinHelm
paladinTunic = inventory.paladinTunic
paladinGauntlets = inventory.paladinGauntlets
paladinBoots = inventory.paladinBoots
paladinWeapon = inventory.paladinBroadsword
paladinShield = inventory.paladinShield

def combat():

    import random as rng
    import sys
    global goldCount
    global paladinHP

    paladinCritChance = 2
    paladinCritMulti = 2
    paladinDefense = 1
    paladinDodgeChance = 12

    enemies = ["Manic Dog","Goblin Chief","Goblin Minion","Baby Dragon","Giant Slime"]

    dogStats = {"HP Min":2,"HP Max":5,"Attack Min":1,"Attack Max":4,"Crit Chance":5,"Crit Multi":4,"Defense":3,"Weapon":"Teeth","Gold Dropped":10}
    gchiefStats = {"HP Min":10,"HP Max":15,"Attack Min":8,"Attack Max":12,"Crit Chance":10,"Crit Multi":3,"Defense":4,"Weapon":"Spear of the Goblin Chief","Gold Dropped":100}
    gminionStats = {"HP Min":5,"HP Max":8,"Attack Min":3,"Attack Max":5,"Crit Chance":7,"Crit Multi":4,"Defense":3,"Weapon":"Goblin Spear","Gold Dropped":30}
    bdragonStats = {"HP Min":8,"HP Max":12,"Attack Min":12,"Attack Max":15,"Crit Chance":12,"Crit Multi":4,"Defense":4,"Weapon":"Fire Breath","Gold Dropped":150}
    gslimeStats = {"HP Min":50,"HP Max":75,"Attack Min":0,"Attack Max":2,"Crit Chance":5,"Crit Multi":8,"Defense":1,"Weapon":"Slime Slam","Gold Dropped":30}

    enemyDefeated = False
    userRun = False
    randEnemy = rng.randint(0,4)
    enemy=enemies[randEnemy]

    if enemy == "Manic Dog":
        enemyStats = dogStats
    elif enemy == "Goblin Chief":
        enemyStats = gchiefStats
    elif enemy == "Goblin Minion":
        enemyStats = gminionStats
    elif enemy == "Baby Dragon":
         enemyStats = bdragonStats
    elif enemy == "Giant Slime":
         enemyStats=gslimeStats

    enemyHPmin = enemyStats["HP Min"]
    enemyHPmax = enemyStats["HP Max"]
    enemyAttackMin = enemyStats["Attack Min"]
    enemyAttackMax = enemyStats["Attack Max"]
    enemyCritChance = enemyStats["Crit Chance"]
    enemyCritMulti = enemyStats["Crit Multi"]
    enemyDefense = enemyStats["Defense"]
    enemyWeapon = enemyStats["Weapon"]
    enemyGoldDropped = enemyStats["Gold Dropped"]

    enemyHP = rng.randint(enemyHPmin,enemyHPmax)
    print("\nYou have encountered a",enemy+"! HP="+str(enemyHP))

    while enemyDefeated == False ++ userRun == False:

        userFightChoice = input("Would you like to fight (1), or run (2)\nAction>>> ")

        if userFightChoice == '1':

            paladinCritRoll = rng.randint(1,100)
            paladinAttack = rng.randint(paladinWeapon["Attack Min"],paladinWeapon["Attack Max"])

            if paladinCritRoll > paladinCritChance:

                enemyHP = enemyHP+enemyDefense-paladinAttack
                print("Attacked",enemy,"for",str(paladinAttack),"damage with your",paladinWeapon["Name"],"but the enemy has",str(enemyDefense),"defense.",str(paladinAttack-enemyDefense),"damage has been done. The",enemy,"now has",str(enemyHP),"HP.")

            elif paladinCritRoll <= paladinCritChance:

                enemyHP = enemyHP-paladinAttack*paladinCritMulti
                print("CRITICAL HIT! You crit the enemy for",str(paladinAttack*paladinCritMulti)+"HP. The enemy has",enemyHP,"HP left.")

            if enemyHP <= 0:

                enemyDefeated = True
                print("\nYou have slain the",enemy+". Well done!\n+"+str(enemyGoldDropped),"G!")
                goldCount = goldCount+enemyGoldDropped
                print("You have",str(goldCount),"G.\n")
                break

            enemyAttack = rng.randint(enemyAttackMin,enemyAttackMax)
            enemyCritRoll = rng.randint(1,100)
            paladinDodgeRoll = rng.randint(1,100)

            if enemyCritRoll > enemyCritChance:

                if paladinDodgeRoll > paladinDodgeChance:
                    paladinHP = paladinHP-enemyAttack+paladinDefense

                    if paladinDefense != 0:
                        print("The enemy retaliates for",(enemyAttack),"damage with their",enemyWeapon+". But you have",str(paladinDefense),"defense. You now have",str(paladinHP),"health.")

                    elif paladinDefense == 0:
                        print("The enemy retaliates for",(enemyAttack),"damage with their",enemyWeapon+". You now have",str(paladinHP),"health.")

                elif paladinDodgeRoll < paladinDodgeChance:
                    print("You dodged the enemy's attack! No damage was done.")

            elif enemyCritRoll <= enemyCritChance:
                paladinHP = paladinHP-enemyAttack*enemyCritMulti
                print("CRITICAL HIT! The enemy crits you for",str(enemyAttack*enemyCritMulti),"damage, bypassing your defense. You now have",str(paladinHP),"HP left.")

        else:

            runChance = rng.randint(1,100)

            if runChance >= 80:
                userRun = True
                print("You managed to escape!")
                break

            else:
                enemyAttack = rng.randint(enemyAttackMin,enemyAttackMax)
                enemyCritRoll = rng.randint(1,100)
                paladinDodgeRoll = rng.randint(1,100)

                if enemyCritRoll > enemyCritChance:
                    paladinHP = paladinHP-enemyAttack+paladinDefense
                    print("You couldn't make it out, and the enemy hits you for",str(enemyAttack),"HP. You now have",str(paladinHP),"health.")

                elif enemyCritRoll <= enemyCritChance:
                    paladinHP = paladinHP-enemyAttack*enemyCritMulti
                    print("CRITICAL HIT! The",enemy,"critted you for",str(enemyAttack*enemyCritMulti),"HP while you were trying to escape! You now have",paladinHP,"health left.")

                elif paladinDodgeRoll > paladinDodgeChance:
                    print("You dodged the enemy's attack! No damage was done.")

        if paladinHP <= 0:
            print("\n\nYou have been killed by your foe! Better luck next time.")
            print("You died with",goldCount,"G.")
            sys.exit("Relaunch the program to play again!\n")

def rest():

    global paladinHP
    import time
    print("\nYou decide to rest at the campfire, this will take a bit.")
    time.sleep(15)
    paladinHP = 50
    print("\nYou are now at full health! HP="+str(paladinHP)+".")

def inventory():

    global goldCount
    global paladinHelm
    global paladinTunic
    global paladinGauntlets
    global paladinBoots
    global paladinWeapon
    global paladinShield

    from goarderItems import items
    inventory = items()

    print("\n\nInventory:")
    print("Currently equipped:", "\n", paladinHelm["Name"], "\n", paladinTunic["Name"], "\n", paladinGauntlets["Name"], "\n", paladinBoots["Name"], "\n", paladinWeapon["Name"], "\n", paladinShield["Name"])

    while True:
        invChoice = input("\n\nWould you like to... view shop (1), exit (2)\n")

        if invChoice == '1':
            print("\nWelcome to the shop!")

            while True:
                shopChoice = input("Would you like to... buy an item (1), view our selection (2), leave the shop (3).\n")

                if shopChoice == '1':
                    shopItemChoice = input("What item item would you like to buy. (Please use item ID which can be found before the item in the shop list.)\n")

                    if shopItemChoice == '7':

                        if goldCount >= inventory.twinDaggers["Price"]:

                            goldCount = goldCount - inventory.twinDaggers["Price"]
                            paladinWeapon = inventory.twinDaggers
                            print("Purchase complete! Gold -" + inventory.twinDaggers["Price"] + ". Your brand new", inventory.twinDaggers["Name"], "have been equipped.")

                        else:
                            print("Sorry, you do not have the adequite gold amount, you need", inventory.twinDaggers["Price"]-goldCount, "more gold.")
                    else:
                        print("The item that corresponds with that item ID is not purchasable, or the item doesn't exist.")

                elif shopChoice == '2':
                    print(str(inventory.twinDaggers["ID"]) + ".", inventory.twinDaggers["Name"], "-", inventory.twinDaggers["Price"], "gold.")

                elif shopChoice == '3':
                    break

                elif shopChoice == '08godsword25':
                    print("Nite's Sword Equipped")
                    paladinWeapon = inventory.niteSword

                else:
                    print("That is not a valid choice. Please re-enter.")

        elif invChoice == '2':
            break
            
        else:
            print("That is not a valid choice. Please re-enter.")
