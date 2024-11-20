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

def game(playerHand, computerHand):
    playerPlayedCards = []
    computerPlayedCards = []
    while True:
#The player's turn to put a card into play or cast a spell
        for i in range(3):
            print(playerHand)
            print("Which card number do you want to choose (1 - " , len(playerHand) , "): ")
            playerCardChoice = int(input("\n > ")) - 1
            
#Assigns the integer the player chose to the corresponding card in the hand, and 
# ensures the name of the card is a string so it can replace any spaces with dashes 
# for confirmation within the json files            
            chosenCard = str(playerHand[playerCardChoice])
            chosenCard = chosenCard.lower().replace(" ", "-")


            if chosenCard in troopCards.keys():
                troopCardPlayed = TroopCard(*getValuesFromDict(troopCards[chosenCard], "name", "attack", "effect", "health", "defence"))
                playerPlayedCards.append(troopCardPlayed)
            
            elif chosenCard in spellCards.keys():
                spellCardPlayed = SpellCard(*getValuesFromDict(spellCards[chosenCard], "name", "attack", "effect"))
                playerPlayedCards.append(spellCardPlayed)

#The computer's turn to choose a card
        for i in range(3):
            computerCardChoice = random.randint(0,5)
            computerChosenCard = str(computerHand[computerCardChoice-1])
            computerChosenCard = computerChosenCard.lower().replace(" ", "-")

            if computerChosenCard in troopCards.keys():

                cpuTroopCardPlayed = TroopCard(*getValuesFromDict(troopCards[computerChosenCard], "name", "attack", "effect", "health", "defence"))
                computerPlayedCards.append(cpuTroopCardPlayed)

            elif computerChosenCard in spellCards.keys():
                cpuSpellCardPlayed = SpellCard(*getValuesFromDict(spellCards[computerChosenCard], "name", "attack", "effect"))
                computerPlayedCards.append(cpuSpellCardPlayed)
    
#Combat commences
        i = 0
        while i != 3:
            currentPlayerCard = playerPlayedCards[i]
            currentComputerCard = computerPlayedCards[i]
            if isinstance(currentPlayerCard, TroopCard) == True:
                if isinstance(currentComputerCard, TroopCard) == True:
                    if currentPlayerCard.attack > currentComputerCard.defence:
                        print(currentComputerCard.health)
                        currentComputerCard.health -= round(currentPlayerCard.attack - currentComputerCard.defence/2)
                        print(currentComputerCard.name, " has taken "+ str(round(currentPlayerCard.attack - currentComputerCard.defence/2)) + " damage!")
                        print(currentComputerCard.health)
                        if currentComputerCard.health <= 0:
                            print(currentComputerCard.name + " has been defeated by " + currentPlayerCard.name)
                            computerPlayedCards.pop(currentComputerCard)
                    elif currentComputerCard.attack > currentPlayerCard.defence:
                        print(currentPlayerCard.health)
                        currentPlayerCard.health -= (currentComputerCard.attack - currentPlayerCard.defence/2)
                        print(currentPlayerCard.name, " has taken "+ str(round(currentComputerCard.attack - currentPlayerCard.defence/2)) + " damage!")
                        print(currentPlayerCard.health)
                        if currentPlayerCard.health <= 0:
                            print(currentPlayerCard.name + " has been defeated by " + currentComputerCard.name)
                            playerPlayedCards.pop(currentPlayerCard)
                    else:
                        print("The defences of " + currentComputerCard.name + " were too strong for " + currentPlayerCard.name + " to overcome!")
                elif isinstance(currentComputerCard, SpellCard) == True:
                    if currentComputerCard.attack > currentPlayerCard.defence:
                        print(currentPlayerCard.health)
                        currentPlayerCard.health -= (currentComputerCard.attack - currentPlayerCard.defence/2)
                        print(currentPlayerCard.name, " has taken "+ str(round(currentComputerCard.attack - currentPlayerCard.defence/2)) + " damage!")
                        print(currentPlayerCard.health)
                        if currentPlayerCard.health <= 0:
                            print(currentPlayerCard.name + " has been defeated by " + currentComputerCard.name)
                            playerPlayedCards.pop(currentPlayerCard)
                    else:
                        print("The defences of " + currentPlayerCard.name + " were too strong to overcome!")
            elif isinstance(currentPlayerCard,SpellCard) == True:
                if isinstance(currentComputerCard, TroopCard) == True:
                    if currentPlayerCard.attack > currentComputerCard.defence:
                        print(currentComputerCard.health)
                        currentComputerCard.health -= (currentPlayerCard.attack - currentComputerCard.defence/2)
                        print(currentComputerCard.name, " has taken "+ str(round(currentPlayerCard.attack - currentComputerCard.defence/2)) + "damage!")
                        print(currentComputerCard.health)
                        if currentComputerCard.health <= 0:
                            print(currentComputerCard.name + " has been defeated by " + currentPlayerCard.name)
                            computerPlayedCards.pop(currentComputerCard)
                    else:
                        print("The defences of " + currentComputerCard.name + " were too  strong to overcome!")
                elif isinstance(currentComputerCard, SpellCard):
                    pass
            i += 1

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
        computerTopCard = shuffledComputer.pop()
        computerHand.append(computerTopCard)
    
    game(playerHand, computerHand)