import json
from programmingTools import *

with open("troopCards.json","r") as troops:
    troopCards = json.load(troops)

with open("spellCards.json","r") as spells:
    spellCards = json.load(spells)

#troop card subclass, will pull on troopCards.json to instantiate the different troop cards available
class TroopCard:
    def __init__(self, name:str, attack:int, effect:str, health:int, defence:int):
        self.name, self.attack, self.effect, self.health, self.defence = name, attack, effect, health, defence
        
    
    def takeDamage(self, health, defence, attack):
        if attack - defence <= 0:
            return health
        
        else:
            return health - (attack-defence)

#spell card subclass, will pull on spellCards.json to instantiate the different spell cards available
class SpellCard:
    def __init__(self, name:str, attack:int, effect:str):
        self.name, self.attack, self.effect = name, attack, effect
