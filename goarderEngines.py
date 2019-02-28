#!/usr/bin/env python3

# goarderEngines v1.0
# by Ashiix

from goarderEntities import *
import random as rng
import sys
import time
items = items()
enemies = enemies()

class stats:
    def __init__(self):
        self.name = "Paladin"
        self.gender = 'F'
        self.goldCount = 0
        self.XPtotal = 0
        self.XPpoints = 0
        self.paladinHP = 30
        self.paladinHPMax = 30
        self.strength = 0
        self.recovery = 0
        self.agi = 0

class equipped:
    def __init__(self):
        self.helm = items.itemsByID[3]
        self.tunic = items.itemsByID[4]
        self.gauntlets = items.itemsByID[5]
        self.boots = items.itemsByID[6]
        self.weapon = items.itemsByID[1]
        self.shield = items.itemsByID[2]

stats = stats()
equipped = equipped()

def setStats(enemy):
        if enemy == "Manic Dog":
            enemyStats = enemies.manicDog
        elif enemy == "Goblin Chief":
            enemyStats = enemies.goblinChief
        elif enemy == "Goblin Minion":
            enemyStats = enemies.goblinMinion
        elif enemy == "Baby Dragon":
            enemyStats = enemies.babyDragon
        elif enemy == "Giant Slime":
            enemyStats = enemies.giantSlime
        elif enemy == "Thief":
            enemyStats = enemies.thief

        return enemyStats

def combat():

    paladinCritChance = 2 + stats.strength
    paladinCritMulti = 2 + stats.strength/4
    paladinRecovery = 1 + stats.recovery/1.5
    paladinDodgeChance = 12 + stats.agi

    enemyDefeated = False
    userRun = False
    randEnemy = rng.randint(0,len(enemies.all)-1)
    enemy = enemies.all[randEnemy]

    enemyStats = setStats(enemy)

    enemyHP = rng.randint(enemyStats["HP Min"],enemyStats["HP Max"])
    print("\nYou have encountered a",enemy+"! HP="+str(enemyHP))

    while enemyDefeated == False ++ userRun == False:

        userFightChoice = input("Would you like to fight (1), or run (2)\nCombat>>> ")

        if userFightChoice == '1':

            paladinCritRoll = rng.randint(1,100)
            paladinAttack = rng.randint(equipped.weapon["Attack Min"],equipped.weapon["Attack Max"])

            if paladinCritRoll > paladinCritChance:

                enemyHP = enemyHP+enemyStats["Recovery"]-paladinAttack-stats.strength/2
                print("Attacked",enemy,"for",str(paladinAttack+stats.strength/2),"damage with your",equipped.weapon["Name"],"but the enemy has",str(enemyStats["Recovery"]),"recovery.",str(paladinAttack-enemyStats["Recovery"]),"damage has been done. The",enemy,"now has",str(enemyHP),"HP.")

            elif paladinCritRoll <= paladinCritChance:

                enemyHP = enemyHP-paladinAttack*paladinCritMulti-stats.strength/2
                print("CRITICAL HIT! You crit the enemy for",str(paladinAttack*paladinCritMulti+stats.strength/2)+"HP. The enemy has",enemyHP,"HP left.")

            if enemyHP <= 0:

                enemyDefeated = True
                print("\nYou have slain the",enemy+". Well done!\n+"+str(enemyStats["Gold Dropped"]),"G! +"+str(enemyStats["XP Gain"]),"XP.")
                stats.goldCount = stats.goldCount+enemyStats["Gold Dropped"]
                print("You have",str(stats.goldCount),"G.")
                stats.XPtotal += enemyStats["XP Gain"]
                print("You have",str(stats.XPtotal),"experience.\n")
                break

            enemyAttack = rng.randint(enemyStats["Attack Min"],enemyStats["Attack Max"])
            enemyCritRoll = rng.randint(1,100)
            paladinDodgeRoll = rng.randint(1,100)

            if enemyCritRoll > enemyStats["Crit Chance"]:

                if paladinDodgeRoll > paladinDodgeChance:
                    stats.paladinHP = stats.paladinHP-enemyAttack+paladinRecovery

                    if paladinRecovery != 0:
                        print("The enemy retaliates for",(enemyAttack),"damage with their",enemyStats["Weapon"]+". But you have",str(paladinRecovery),"recovery. You now have",str(stats.paladinHP),"health.")

                    elif paladinRecovery == 0:
                        print("The enemy retaliates for",(enemyAttack),"damage with their",enemyStats["Weapon"]+". You now have",str(stats.paladinHP),"health.")

                elif paladinDodgeRoll < paladinDodgeChance:
                    print("You dodged the enemy's attack! No damage was done.")

            elif enemyCritRoll <= enemyStats["Crit Chance"]:
                stats.paladinHP = stats.paladinHP-enemyAttack*enemyStats["Crit Multi"]
                print("CRITICAL HIT! The enemy crits you for",str(enemyAttack*enemyStats["Crit Multi"]),"damage, bypassing your recovery. You now have",str(stats.paladinHP),"HP left.")

        else:
            runChance = rng.randint(1,100)

            if runChance >= 80:
                userRun = True
                print("You managed to escape!")
                break

            else:
                enemyAttack = rng.randint(enemyStats["Attack Min"],enemyStats["Attack Max"])
                enemyCritRoll = rng.randint(1,100)
                paladinDodgeRoll = rng.randint(1,100)

                if enemyCritRoll > enemyStats["Crit Chance"]:
                    stats.paladinHP = stats.paladinHP-enemyAttack+paladinRecovery
                    print("You couldn't make it out, and the enemy hits you for",str(enemyAttack),"HP. You now have",str(stats.paladinHP),"health.")

                elif enemyCritRoll <= enemyStats["Crit Chance"]:
                    stats.paladinHP = stats.paladinHP-enemyAttack*enemyStats["Crit Multi"]
                    print("CRITICAL HIT! The",enemy,"critted you for",str(enemyAttack*enemyStats["Crit Multi"]),"HP while you were trying to escape! You now have",stats.paladinHP,"health left.")

                elif paladinDodgeRoll > paladinDodgeChance:
                    print("You dodged the enemy's attack! No damage was done.")

        if stats.paladinHP <= 0:
            print("\n\nYou have been killed by your foe! Better luck next time.")
            print("You died with",stats.goldCount,"G.")
            sys.exit("Relaunch the program to play again!\n")

def rest():

    print("\nYou decide to rest at the campfire, this will take a bit.")
    for i in range(8):
        print("   -",end="\r")
        time.sleep(0.4)
        print("   \\",end="\r")
        time.sleep(0.4)
        print("   /",end="\r")
        time.sleep(0.4)
    stats.paladinHP = stats.paladinHPMax
    print("You are now at full health! HP="+str(stats.paladinHP)+".\n",end="\r")


def shop():

    print("\nWelcome to the shop!")

    while True:
        shopChoice = input("Would you like to... buy an item (1), view our selection (2), leave the shop (3).\nShop>>> ")

        if shopChoice == '1':
            shopItemChoice = input("What item item would you like to buy. (Please use item ID which can be found before the item in the shop list.)\nID>>> ")

            if shopItemChoice == '7':

                if stats.goldCount >= items.twinDaggers["Price"]:

                    stats.goldCount = stats.goldCount - items.twinDaggers["Price"]
                    equipped.weapon = items.twinDaggers
                    print("Purchase complete! Gold -"+str(items.twinDaggers["Price"])+". Your brand new", items.twinDaggers["Name"], "have been equipped.")

                else: print("Sorry, you do not have the adequite gold amount, you need", items.twinDaggers["Price"]-stats.goldCount, "more gold.")

            else: print("The item that corresponds with that item ID is not purchasable, or the item doesn't exist.\n")

        elif shopChoice == '2': print(str(items.twinDaggers["ID"]) + ".", items.twinDaggers["Name"], "-", items.twinDaggers["Price"], "gold.")

        elif shopChoice == '3': break

        elif shopChoice == '08godsword25':
            print("\nNite's Sword Equipped\n")
            equipped.weapon = items.niteSword

        else: print("That is not a valid choice. Please re-enter.")


def inventory():

    print("\nCurrently equipped:\n", equipped.helm["Name"], "\n", equipped.tunic["Name"], "\n", equipped.gauntlets["Name"], "\n", equipped.boots["Name"], "\n", equipped.weapon["Name"], "\n", equipped.shield["Name"])

    while True:
        invChoice = input("\nWould you like to... view shop (1), exit (2)\nInventory>>> ")

        if invChoice == '1': shop()
        elif invChoice == '2': break
        else: print("That is not a valid choice. Please re-enter.")


def statMenu():

    print("\nStats:")
    print("Max HP:",str(stats.paladinHPMax),"\nCurrent HP:",str(stats.paladinHP),"\nStrength: +"+str(stats.strength),"\nRecovery: +"+str(stats.recovery),"\nAgility: +"+str(stats.agi)+"\n")

    while stats.XPtotal >= 100:

        stats.XPpoints += 1
        stats.XPtotal -= 100

    print("You have",str(stats.XPpoints),"XP points avalible.")

    if stats.XPpoints != 0:

        statSel = input("Would you like to allocate them? (y/n)\nChoice>>> ")

        if statSel == 'y':

            while stats.XPpoints > 0:

                skillChoice = input("What skill would you like to allocate in? (HP, str, recov, agi)\nSkill>>> ")

                if skillChoice == "HP":
                    stats.paladinHPMax += 1
                    stats.XPpoints -= 1

                elif skillChoice == "str":
                    stats.strength += 1
                    stats.XPpoints -= 1

                elif skillChoice == "recov":
                    stats.strength += 1
                    stats.XPpoints -= 1

                elif skillChoice == "agi":
                    stats.agi += 1
                    stats.XPpoints -= 1

        elif statSel == 'n': pass

        else: print("That is not a valid option.")

def save():
    save = open(".save", 'w')
    save.write(stats.name + '\n' + stats.gender + '\n' + str(stats.goldCount) + '\n' + str(stats.XPtotal) + '\n' + str(stats.XPpoints) + '\n' + str(stats.paladinHP) + '\n' + str(stats.paladinHPMax) + '\n' + str(stats.strength) + '\n' + str(stats.recovery) + '\n' + str(stats.agi) + '\n')
    save.write(str(equipped.helm["ID"]) + '\n' + str(equipped.tunic["ID"]) + '\n' + str(equipped.gauntlets["ID"]) + '\n' + str(equipped.boots["ID"]) + '\n' + str(equipped.weapon["ID"]) + '\n' + str(equipped.shield["ID"]))
    save.close

def readSave():
    try:
        save = open(".save", 'r')
        toContinue = str(input("Would you like to continue your previous game? y/n \n"))
        if(toContinue == 'y'):
            newGame = False
            stats.name = save.readline().rstrip('\n')
            stats.gender = save.readline().rstrip('\n')
            stats.goldCount = float(save.readline().rstrip('\n'))
            stats.XPtotal = float(save.readline().rstrip('\n'))
            stats.XPpoints = float(save.readline().rstrip('\n'))
            stats.paladinHP = float(save.readline().rstrip('\n'))
            stats.paladinHPMax = float(save.readline().rstrip('\n'))
            stats.strength = float(save.readline().rstrip('\n'))
            stats.recovery = float(save.readline().rstrip('\n'))
            stats.agi = float(save.readline().rstrip('\n'))
            loadHelm = float(save.readline().rstrip('\n'))
            loadTunic = float(save.readline().rstrip('\n'))
            loadGauntlets = float(save.readline().rstrip('\n'))
            loadBoots = float(save.readline().rstrip('\n'))
            loadWeapon = float(save.readline().rstrip('\n'))
            loadShield = float(save.readline().rstrip('\n'))
            equipped.helm = items.itemsByID[loadHelm]
            equipped.tunic = items.itemsByID[loadTunic]
            equipped.gauntlets = items.itemsByID[loadGauntlets]
            equipped.boots = items.itemsByID[loadBoots]
            equipped.weapon = items.itemsByID[loadWeapon]
            equipped.shield = items.itemsByID[loadShield]
        else:
            newGame = True
        save.close()
    except:
        newGame = True
    return newGame
