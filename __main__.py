from programmingTools import *
from random import *
from card import *
import json
import pygame as py


with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

""" shuffle = lambda playerDeck : random.shuffle(playerDeck.contents) """  #shuffling algorithm to shuffle the player's deck, TODO

def deal_cards(): #deals the player's hand of 10 cards
    """     for i in range(10): #deals 10 cards into the player's hand
        nextCard = playerDeck[len(playerDeck)-1]
        del(playerDeck[len(playerDeck)-1])
        playerHand.append(nextCard)
        print(playerHand)
    
    for i in range(10): #deals the computer's hand of 10 cards
        nextCard = computerDeck[len(computerDeck)-1]
        del(computerDeck[len(computerDeck)-1])
        computerHand.append(nextCard)
        print(computerHand)  """
    pass



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

    inf = TroopCard(**troopCards["sword"])
    archer = TroopCard(**troopCards["archer"])
    paladin = TroopCard(**troopCards["paladin"])
    healer = TroopCard(**troopCards["healer"])
    wizard = TroopCard(**troopCards["wizard"])
    rogue = TroopCard(**troopCards["rogue"])
    necro = TroopCard(**troopCards["necro"])
    zombie = TroopCard(**troopCards["zombie"])
    skeleton = TroopCard(**troopCards["skeleton"])
    wolf = TroopCard(**troopCards["wolf"])


    for i in range(2):
        card = input("Enter the name of a card you wish to add to your deck from the following: "+"\n"
        +inf.name+"\n"
        +necro.name+"\n")
        if card == inf.name:
            playerDeck.push(inf.name)
        else:
            playerDeck.push(necro.name)
        print(playerDeck)

    



