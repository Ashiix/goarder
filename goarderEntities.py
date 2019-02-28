#!/usr/bin/env python3

# goarderItems v1.0
# by Ashiix

class items:
    def __init__ (self):
        # ITEMS

        # Weapons
        self.paladinBroadsword = {"Name":"Paladin's Broadsword", "ID":1, "Attack Min":8, "Attack Max":11, "Recovery":3, "Agi Pen":1, "Description":"This ornate, large blade has seen many battles, yours, and all your own, this weapon was given to you when after your training."}
        self.twinDaggers = {"Name":"Twin Daggers", "ID":7, "Attack Min":11, "Attack Max":15, "Recovery":0, "Agi Pen":0, "Price":1000, "Description":"These daggers are made with the finest steel from the depths of the Centcor mine. Their hilts are embroidered in pure gold."}
        self.niteSword = {"Name":"Nite's Sword", "ID":0, "Attack Min":1200, "Attack Max":15000, "Recovery":10000, "Agi Pen":-100000, "Description":"The sword of a god, struck down to earth by the very being itself, created a vortex of war surrounding it. Every nation wanting to conquer the mighty blade."}

        # Shield
        self.paladinShield = {"Name":"Paladin's Shield", "ID":2, "Recovery":4, "Agi Pen":5, "Description":"A majestc golden phoenix is enscribed on the body of the shied, symbolising the neverending cycle of the Paladins."}
        self.cencorianShield = {"Name":"Centcorian Shield", "ID":8, "Recovery":6, "Agi Pen":2, "Description":"Built from an incredibly strong aluminum alloy buried in the depths of the Centcor mines. The choice of all Centcor warriors."}

        # Helmets
        self.paladinHelm = {"Name":"Paladin's Helm", "ID":3, "Recovery":2, "Agi Pen":2, "Description":"The helm of the legendary Paladins. You were given this after you completed your training."}
        self.cencorianHelm = {"Name":"Centcorian Helm", "ID":9, "Recovery":4, "Agi Pen":3, "Description":"Built from an incredibly strong aluminum alloy buried in the depths of the Centcor mines. The choice of all Centcor warriors."}

        # Tunics
        self.paladinTunic = {"Name":"Paladin's Tunic", "ID":4, "Recovery":5, "Agi Pen":4, "Description":"The tunic of the legendary Paladins. You were given this after you completed your training."}
        self.cencorinTunic = {"Name":"Centcorian Tunic", "ID":10, "Recovery":6, "Agi Pen":5, "Description":"Built from an incredibly strong aluminum alloy buried in the depths of the Centcor mines. The choice of all Centcor warriors."}


        # Gauntlets
        self.paladinGauntlets = {"Name":"Paladin's Gauntlets", "ID":5, "Recovery":1, "Agi Pen":1, "Description":"The gauntlets of the legendary Paladins. You were given this after you completed your training."}

        # Boots
        self.paladinBoots = {"Name":"Paladin's Boots", "ID":6, "Recovery":1, "Agi Pen":2, "Description":"The boots of the legendary Paladins. You were given this after you completed your training."}

        self.itemsByID = {0:self.niteSword, 1:self.paladinBroadsword, 2:self.paladinShield, 3:self.paladinHelm, 4:self.paladinTunic, 5:self.paladinGauntlets, 6:self.paladinBoots, 7:self.twinDaggers, 8:self.cencorianShield, 9:self.cencorianHelm, 10:self.cencorinTunic}

class enemies:
    def __init__(self):
        self.manicDog = {"HP Min":2,"HP Max":5,"Attack Min":1,"Attack Max":4,"Crit Chance":5,"Crit Multi":4,"Recovery":3,"Weapon":"Teeth","Gold Dropped":10, "XP Gain":1}
        self.goblinChief = {"HP Min":10,"HP Max":15,"Attack Min":8,"Attack Max":12,"Crit Chance":10,"Crit Multi":3,"Recovery":4,"Weapon":"Spear of the Goblin Chief","Gold Dropped":100, "XP Gain":5}
        self.goblinMinion = {"HP Min":5,"HP Max":8,"Attack Min":3,"Attack Max":5,"Crit Chance":7,"Crit Multi":4,"Recovery":3,"Weapon":"Goblin Spear","Gold Dropped":30, "XP Gain":3}
        self.babyDragon = {"HP Min":8,"HP Max":12,"Attack Min":12,"Attack Max":15,"Crit Chance":12,"Crit Multi":4,"Recovery":4,"Weapon":"Fire Breath","Gold Dropped":150, "XP Gain":10}
        self.giantSlime = {"HP Min":50,"HP Max":75,"Attack Min":0,"Attack Max":2,"Crit Chance":5,"Crit Multi":8,"Recovery":1,"Weapon":"Slime Slam","Gold Dropped":30, "XP Gain":15}
        self.thief = {"HP Min":6,"HP Max":10,"Attack Min":2,"Attack Max":4,"Crit Chance":25,"Crit Multi":8,"Recovery":2,"Weapon":"Thief's Dagger","Gold Dropped":100, "XP Gain":22}

        self.all = ["Manic Dog","Goblin Chief","Goblin Minion","Baby Dragon","Giant Slime","Thief"]
