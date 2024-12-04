#Imports programmingTools. It contains my Stack class, which is needed for the decks and discard piles
from programmingTools import *
#Imports random, which is needed for shuffling
import random
#Imports the 
from card import *
import json
import customtkinter as ctk
from tkinter import *

#Opens up the .json files that contain the dictionaries with the information about the 
# troop cards to allow the addition of the card names to the deck and to create the card objects
with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cards and Capers")
        self.geometry("1024x768")
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

#Created the frame and displays the buttons that represent the player's draw and discard piles. Buttons used as it provides an 
# element of interactivity and makes it very easy to execute operations through the use of the "command=" argument
        self.playerPilesFrame = ctk.CTkFrame(self, fg_color = "transparent")
        self.playerPilesFrame.grid(row = 1, column = 2, sticky = "se", pady = 15)
        self.drawPile = ctk.CTkButton(self.playerPilesFrame, fg_color="#C8102E", text="Draw Pile", hover_color="#6d0000", height=180, width=120, command=quit)
        self.drawPile.pack(side = LEFT)
        self.discardPile = ctk.CTkButton(self.playerPilesFrame, fg_color="#C8102E", text="Discard Pile", hover_color="#6d0000", height=180, width=120, command=quit)
        self.discardPile.pack(side = RIGHT, padx = 20)

        self.computerPilesFrame = ctk.CTkFrame(self, fg_color = "transparent")
        self.computerPilesFrame.grid(row = 0, column = 0, sticky = "nw", pady = 15)
        self.drawPile = ctk.CTkButton(self.computerPilesFrame, fg_color="#C8102E", text="Draw Pile", height=180, width=120, hover = False)
        self.drawPile.pack(side = RIGHT)
        self.discardPile = ctk.CTkButton(self.computerPilesFrame, fg_color="#C8102E", text="Discard Pile", height=180, width=120, hover = False)
        self.discardPile.pack(side = LEFT, padx = 20)





def deckBuilding():
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

#the combat element of the game (the main element)
def game(playerHand, computerHand):
    deckBuilding()
    #Creates an array to store the cards the player and computer have played to represent the table
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

#checks if the string stored in chosenCard is a key in the troopCards or spellCards .json files
# and if it is there an object is created to store the card as an object in the "table", represented
# by the array playerPlayedCards
            if chosenCard in troopCards.keys():
                troopCardPlayed = TroopCard(*getValuesFromDict(troopCards[chosenCard], "name", "attack", "effect", "health", "defence"))
                playerPlayedCards.append(troopCardPlayed)
            
            elif chosenCard in spellCards.keys():
                spellCardPlayed = SpellCard(*getValuesFromDict(spellCards[chosenCard], "name", "attack", "effect"))
                playerPlayedCards.append(spellCardPlayed)

#The computer's turn to choose a card
        for i in range(3):
            #generates a random number between 0 and 5 (the current size of the hand), then converts the
            #card name stored in that index to a string and converts it to the format of the keys in the
            #two JSON files
            computerCardChoice = random.randint(0,5)
            computerChosenCard = str(computerHand[computerCardChoice-1])
            computerChosenCard = computerChosenCard.lower().replace(" ", "-")

            #Checks whether the key is in troopCards, creates a TroopCard object with the data that key
            #links to and appends that object to the array that represents the computer's side of the
            #playing table
            if computerChosenCard in troopCards.keys():

                cpuTroopCardPlayed = TroopCard(*getValuesFromDict(troopCards[computerChosenCard], "name", "attack", "effect", "health", "defence"))
                computerPlayedCards.append(cpuTroopCardPlayed)
            #Checks whether the key is in spellCards, creates a SpellCard object with the data that key
            #links to and appends that object to the array that represents the computer's side of the
            #playing table
            elif computerChosenCard in spellCards.keys():
                cpuSpellCardPlayed = SpellCard(*getValuesFromDict(spellCards[computerChosenCard], "name", "attack", "effect"))
                computerPlayedCards.append(cpuSpellCardPlayed)
    
#Combat commences
        i = 0
        while i != 3:
            currentPlayerCard = playerPlayedCards[i]
            currentComputerCard = computerPlayedCards[i]
            #Checking whether the player card is a troop card or a spell card to determine whether it can take and deal damage or only deal damage
            if isinstance(currentPlayerCard, TroopCard) == True:
                #Checking whether the computer card is 
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

#The main part of the program - initialises the decks, discard piles, hands, main element of the game
#and facilitates the deckbuilding element of the game
if __name__ == "__main__":
    #Initialises the decks and the discard piles as stacks, as they will operate on a first in, last out
    #basis
    playerDeck = Stack()
    computerDeck = Stack()
    playerDiscardPile = Stack()
    computerDiscardPile = Stack()

    app = App()
    app.mainloop()
    