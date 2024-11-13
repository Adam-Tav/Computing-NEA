from programmingTools import *
import random
from card import *
import json
import pygame as py

#Opens up the .json files that contain the dictionaries with the information about 
# the troop cards
with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

def combat(playerHand, computerHand):
    playerPlayedCards = []
    computerPlayedCards = []
    while True:
#The player's turn to put a card into play or cast a spell
        for i in range(3):
            playerCardChoice = int(input("Which card number do you want to choose (1-5): ")) - 1
            
#Assigns the integer the player chose to the corresponding card in the hand, and 
# ensures the name of the card is a string so it can replace any spaces with dashes 
# for confirmation within the json files            
            chosenCard = str(playerHand[playerCardChoice])
            chosenCard = chosenCard.lower().replace(" ", "-")


            if chosenCard in troopCards.keys():
                troopCardPlayed = troopCards[chosenCard]["name"]
                print(troopCardPlayed)
                playerPlayedCards.append(troopCardPlayed)
            
            elif chosenCard in spellCards.keys():
                spellCardPlayed = spellCards[chosenCard]["name"]
                print(spellCardPlayed)
                playerPlayedCards.append(spellCardPlayed)
#The computer's turn to choose a card
        for i in range(3):
            computerCardChoice = random.randint(0,5)
            computerChosenCard = str(computerHand[computerCardChoice])
            computerChosenCard = computerChosenCard.lower().replace(" ", "-")

            if computerChosenCard in troopCards.keys():
                cpuTroopCardPlayed = troopCards[computerChosenCard]["name"]
                computerPlayedCards.append(cpuTroopCardPlayed)

            elif computerChosenCard in spellCards.keys():
                cpuSpellCardPlayed = spellCards[computerChosenCard]["name"]
                computerPlayedCards.append(cpuSpellCardPlayed)
#Combat commences
        i = 0
        while i != 3:
            if not playerPlayedCards[i] in troopCards:
                if not computerPlayedCards[i] in troopCards:
                    pass
                elif not computerPlayedCards[i] in spellCards:
                    pass

            elif not playerPlayedCards[0] in spellCards:
                if not computerPlayedCards[i] in troopCards:
                    pass
                elif not computerPlayedCards[i] in spellCards:
                    pass
        

        """ if troopCards[playerHand[playerCardChoice]]["attack"] != troopCards[computerHand[computerCardChoice]]["defence"]:
            if troopCards[playerHand[playerCardChoice]]["attack"] > troopCards[computerHand[computerCardChoice]]["defence"]:
                pass
        else:
            pass """

if __name__ == "__main__":
    playerDeck = Stack()
    computerDeck = Stack()

    for i in range(10):
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

    for i in range(10):
        allCards = list(troopCards.keys()) + list(spellCards.keys())
        computerCard = random.choice(allCards)

        if computerCard in troopCards.keys():
            computerDeck.push(troopCards[computerCard]["name"])
        elif computerCard in spellCards.keys():
            computerDeck.push(spellCards[computerCard]["name"])
        allCards.remove(card)
    
    shuffledPlayer = playerDeck.randomise()
    shuffledComputer = computerDeck.randomise()

    playerHand = []
    computerHand = []

    for i in range(5):
        playerTopCard = shuffledPlayer.pop()
        playerHand.append(playerTopCard)
        print(playerHand)
        computerTopCard = shuffledComputer.pop()
        computerHand.append(computerTopCard)
    
    combat(playerHand, computerHand)
