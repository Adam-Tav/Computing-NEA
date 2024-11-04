import json

class Card:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def dealDamage(self):
        pass

class troopCard(Card):
    def __init__(self, name, attack, health, defence):
        super().__init__(self, name, attack)
        self.health = health
        self.defence = defence
    
    def takeDamage(self, health, defence, attack):
        if attack - defence <= 0:
            return health
        
        else:
            return health - (attack-defence)

class spellCard(Card):
    def __init__(self, name, attack):
        super().__init__(self, name, attack)