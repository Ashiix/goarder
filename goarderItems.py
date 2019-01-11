#!/usr/bin/env python3

# goarderItems v1.0
# by nitel

class items:
    def __init__ (self):
        # ITEMS

        # Weapons
        self.paladinBroadsword = {"Name":"Paladin's Broadsword", "ID":1, "Attack Min":8, "Attack Max":11, "Recovery":3, "Agi Pen":1, "Description":"This ornate, large blade has seen many battles, yours, and all your own, this weapon was given to you when after your training."}
        self.twinDaggers = {"Name":"Twin Daggers", "ID":7, "Attack Min":11, "Attack Max":15, "Recovery":0, "Agi Pen":0, "Price":1000, "Description":"These daggers are made with the finest steel from the depths of the Centcor mine. Their handles are embroidered by a gold plating."}
        self.niteSword = {"Name":"Nite's Sword", "ID":0, "Attack Min":1200, "Attack Max":15000, "Recovery":10000, "Agi Pen":-10, "Description":"The sword of a god, struck down to earth by the very being itself, created a vortex of war surrounding it. Every nation wanting to conquer the mighty blade."}

        # Shield
        self.paladinShield = {"Name":"Paladin's Shield", "ID":2, "Recovery":4, "Agi Pen":5, "Description":"A majestc golden phoenix is enscribed on the body of the shied, symbolising the neverending cycle of the Paladins."}

        # Helmets
        self.paladinHelm = {"Name":"Paladin's Helm", "ID":3, "Recovery":2, "Agi Pen":2, "Description":"The helm of the legendary Paladins. You were given this after you completed your training."}
        # Tunics
        self.paladinTunic = {"Name":"Paladin's Tunic", "ID":4, "Recovery":5, "Agi Pen":4, "Description":"The tunic of the legendary Paladins. You were given this after you completed your training."}

        # Gauntlets
        self.paladinGauntlets = {"Name":"Paladin's Gauntlets", "ID":5, "Recovery":1, "Agi Pen":1, "Description":"The gauntlets of the legendary Paladins. You were given this after you completed your training."}

        # Boots
        self.paladinBoots = {"Name":"Paladin's Boots", "ID":6, "Recovery":1, "Agi Pen":2, "Description":"The boots of the legendary Paladins. You were given this after you completed your training."}
