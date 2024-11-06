from programmingTools import *
import random
from card import *
import json
import pygame as py


with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

def combat(): #simple combat algorithm - update when shift over to OOP with more complex combat modules - status effects etc.
    """ playerCardChoice = int(input("Which card number do you want to choose (1-10): ")) - 1
    computerCardChoice = random.randint(1,len(computerHand))
    print(playerCardChoice)
    print(computerCardChoice)
    if playerCand[playerCardChoice, 3] > computerHand[computerCardChoice, 3]:
        computerHand[computerCardChoice, 2] -= (playerHand[playerCardChoice, 3] - computerHand[computerCardChoice, 4])
    
    elif playerHand[playerCardChoice, 3] == computerHand[computerCardChoice, 3]:
        computerHand[computerCardChoice, 2] -= (playerHand[playerCardChoice, 3] - computerHand[computerCardChoice, 4])
        playerHand[playerCardChoice, 2] -= (computerHand[computerCardChoice, 3] - playerHand[playerCardChoice, 4])
    else:"""
    pass

if __name__ == "__main__":
    playerDeck = Stack()
    computerDeck = Stack()

    for i in range(3):
        print("Enter the name of a card you wish to add to your deck from the following: ")
        for j in troopCards.values():
            print(j["name"])
        for j in spellCards.values():
            print(j["name"])
        card = input("\n > ")

        card = card.lower().replace(" ", "-")

        if card in troopCards.keys():
            playerDeck.push(troopCards[card]["name"])
        elif card in spellCards.keys():
            playerDeck.push(spellCards[card]["name"])

    allCards = list(troopCards.keys()) + list(spellCards.keys())

    for i in range(3):
        allCards = list(troopCards.keys()) + list(spellCards.keys())
        card = random.choice(allCards)

        if card in troopCards.keys():
            computerDeck.push(troopCards[card]["name"])
        elif card in spellCards.keys():
            computerDeck.push(spellCards[card]["name"])
        allCards.remove(card)

    print(playerDeck)
    print(computerDeck)
    
    shuffled = playerDeck.randomise()
    computerDeck.randomise()

    print(shuffled)
