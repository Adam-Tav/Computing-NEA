import json

with open("troopCards.json", "r") as file:
    troopCards = json.load(file)

with open("spellCards.json", "r") as file1:
    spellCards = json.load(file1)

class Card:
    def __init__(self, name, attack, effect):
        self.name = name
        self.attack = attack
        self.effect = effect

    def dealDamage(self):
        pass

class TroopCard(Card):
    def __init__(self, name, attack, health, defence, effect):
        super().__init__(self, name, attack, effect)
        self.health = health
        self.defence = defence
    
    def takeDamage(self, health, defence, attack):
        if attack - defence <= 0:
            return health
        
        else:
            return health - (attack-defence)

class SpellCard(Card):
    def __init__(self, name, attack, effect):
        super().__init__(self, name, attack, effect)

