#Imports programmingTools. It contains my Stack class, which is needed for the decks and discard piles
from programmingTools import *
from card import *
import json
import customtkinter as ctk
from tkinter import *
from PIL import Image

#Opens up the .json files that contain the dictionaries with the information about the 
# troop cards to allow the addition of the card names to the deck and to create the card objects
with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

cardBack = ctk.CTkImage(dark_image = Image.open("C:\\Users\\adamt\\OneDrive\\School\\Computing\\Computing NEA\\cardBack.webp"), size = (120, 180))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cards and Capers")
        self.geometry("1024x768")
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.playerHand = [] #stores the card objects
        self.cardHolder = [] #stores the card buttons
        self.computerHand = []

#Created a frame to represent the game screen, allowing for the "switching" between several screens such as the deckbuilding 
# screen, game screen and title screen
        self.gameScreen = ctk.CTkFrame(self, fg_color = "transparent")
        self.gameScreen.grid(row = 0, column = 0)

#Creates the frame and displays the buttons that represent the player's draw and discard piles. Buttons used as it provides an 
# element of interactivity and makes it very easy to execute operations through the use of the "command=" argument
        self.playerPilesFrame = ctk.CTkFrame(self.gameScreen, fg_color = "transparent")
        self.playerPilesFrame.grid(row = 3, column = 2, sticky = "se", pady = 15)

        self.playerDrawPile = ctk.CTkButton(self.playerPilesFrame, fg_color = "transparent", text = "", height = 180, width = 120, command = self.drawCard, image = cardBack)
        self.playerDrawPile.pack(side = LEFT)

        self.discardPile = ctk.CTkButton(self.playerPilesFrame, fg_color = "transparent", text = "", height=180, width=120, command = quit, image = cardBack)
        self.discardPile.pack(side = RIGHT, padx = 20)

#creates the frame and displays the buttons that represent the computer's draw and discard piles. Buttons used here because it is 
# an easy way to get the scale correct, and can be programmed to play a card in response to the player playing a card    
        self.computerPilesFrame = ctk.CTkFrame(self.gameScreen, fg_color = "transparent")
        self.computerPilesFrame.grid(row = 0, column = 0, sticky = "nw", pady = 15)

        self.computerDrawPile = ctk.CTkButton(self.computerPilesFrame, fg_color = "transparent", text = "", height = 180, width = 120, hover = False, image = cardBack)
        self.computerDrawPile.pack(side = RIGHT)

        self.computerDiscardPile = ctk.CTkButton(self.computerPilesFrame, fg_color = "transparent", text="", height = 180, width = 120, hover = False, image = cardBack)
        self.computerDiscardPile.pack(side = LEFT, padx = 10)

#creates the frame and displays the buttons for the player's hand. Again, buttons used for the interactivity for the player and the 
# ease of executing commands by button presses
        self.handFrame = ctk.CTkFrame(self.gameScreen, fg_color = "transparent")
        self.handFrame.grid(row = 3, column = 1, pady = 15, padx = 60, sticky = "s")
        
        for i in range(5):
            currentPlayerCard = playerDeck.items[-1]
            self.playerCardIcon = ctk.CTkButton(self.handFrame, fg_color = "transparent", text = "", height = 180, width = 120, command = lambda i=i: self.playCard(i), image = ctk.CTkImage(Image.open(currentPlayerCard.image), size = (120, 180)))
            self.playerCardIcon.pack(side = LEFT, padx = 5)
            self.playerHand.append(currentPlayerCard)
            self.cardHolder.append(self.playerCardIcon)
            playerDeck.pop()


#creates the frame and displays the buttons for the computer's hand. Again, buttons used for uniformity with the player's cards and
# the computer's cards
        self.computerHandFrame = ctk.CTkFrame(self.gameScreen, fg_color = "transparent")
        self.computerHandFrame.grid(row = 0, column = 1, padx = 30, pady = 15, sticky = "n")

        for i in range(5):
            currentComputerCard = computerDeck.items[-1]
            self.computerCardIcon = ctk.CTkButton(self.computerHandFrame, fg_color = "transparent", text = "", height = 180, width = 120, hover = False, image = cardBack)
            self.computerCardIcon.pack(side = LEFT, padx = 5)
            self.computerHand.append(currentComputerCard)
            computerDeck.pop()
        
        self.deckSizeCounter = ctk.CTkLabel(
            self.gameScreen, 
            fg_color = "transparent", 
            text = f"Cards Remaining: {len(playerDeck.items)}"
            )
        self.deckSizeCounter.grid(
            row = 2, 
            column = 2, 
            padx = 10, 
            sticky = "sw"
            )

#creates the frame for the table
        self.tableFrame1 = ctk.CTkFrame(
            self.gameScreen, 
            fg_color = "#704F32"
            )
        self.tableFrame1.grid(
            row = 1, 
            column = 1
            )

        self.tableFrame2 = ctk.CTkFrame(self.gameScreen, fg_color = "#704F32")
        self.tableFrame2.grid(row = 2, column = 1)

#sets the maximum hand size to 5 as per the rules, and sets the maximum number of cards the player or computer can play to 3 as per 
# the rules
        self.maxHandSize = 5
        self.maxPlayedCards = 14

#creates the array that will be used to store the card objects that are stored on the play table
        self.playerPlayTable = []

#assigned to the draw pile, enables the drawing of cards from the draw pile. cards are drawn and given the playCard method to allow
#  them to be played
    def drawCard(self): 
        if len(self.playerHand) < self.maxHandSize:
            #stores the deck size as a variable for simpler calling withing the method
            deckSize = playerDeck.size() 
            #ensures the deck has cards in it before removing the top card, adding it to the player's hand and creating the button 
            # to show the card
            if deckSize > 0: 
                card = playerDeck.pop()
                self.playerHand.append(card)
                self.playerCardIcon = ctk.CTkButton(
                    self.handFrame, 
                    fg_color = "transparent", 
                    text="",
                    height=180, 
                    width=120, 
                    command = lambda:  self.playCard(self.playerHand.index(card)), 
                    image = ctk.CTkImage(Image.open(self.playerHand[self.playerHand.index(card)].image), 
                                         size = (120, 180)
                                         )
                    )

                self.playerCardIcon.pack(side = LEFT, padx = 5)
                self.cardHolder.append(self.playerCardIcon)
                
                #updates the counter to reflect the removal of a card from the deck
                self.deckSizeCounter.destroy() 
                self.deckSizeCounter = ctk.CTkLabel(
                    self.gameScreen, 
                    fg_color = "transparent", 
                    text = f"Cards Remaining: {len(playerDeck.items)}"
                    )
                self.deckSizeCounter.grid(row = 2, column = 2, pady = 5)

                #after a card has been played, checks if there are any cards remaining in the deck. if there aren't, the button 
                # representing the draw pile gets destroyed
                if deckSize == 0:
                    self.playerDrawPile.destroy()

    #given to all drawn cards, this checks to make sure the player hasn't already played the maximum number of cards, before
    # destroying the button stored in the index (i) assigned to the button when it's created, and creating a new button with the
    # stats and card art of the played card
    def playCard(self, cardIndex):
        self.cardHolder[cardIndex].destroy()
        if len(self.playerPlayTable) < self.maxPlayedCards:
            self.playerCard = ctk.CTkButton(
                self.tableFrame2, 
                fg_color = "transparent", 
                text = "", 
                height = 180, 
                width = 120, 
                hover = False, 
                image = ctk.CTkImage(
                    Image.open(
                        self.playerHand[cardIndex].image
                    ), 
                    size = (120, 180)
                )
            )
            self.playerCard.pack(padx = 5, side = LEFT)
            self.playerPlayTable.append(self.playerHand[cardIndex])

            self.playerHand.pop(cardIndex)



#The main part of the program - initialises the decks, discard piles, hands, main element of the game
#and facilitates the deckbuilding element of the game
if __name__ == "__main__":
    #Initialises the decks and the discard piles as stacks, as they will operate on a first in, last out
    #basis
    playerDeck = Stack()
    computerDeck = Stack()
    playerDiscardPile = Stack()
    computerDiscardPile = Stack()

    #creates a list of the keys for the 
    troopCardKeys = list(
        troopCards.keys()
        )
    spellcardKeys = list(
        spellCards.keys()
    )

    for i in range(1, len(troopCardKeys)-1):
        playerDeck.items.append(
            TroopCard(
                *getValuesFromDict(
                    troopCards[troopCardKeys[i]], 
                    "name", 
                    "attack", 
                    "effect", 
                    "health", 
                    "defence", 
                    "image"
                    )
                )
            )
        computerDeck.items.append(
            TroopCard(
                *getValuesFromDict(
                    troopCards[troopCardKeys[i]], 
                    "name", 
                    "attack", 
                    "effect", 
                    "health", 
                    "defence", 
                    "image"
                    )
                )
            )

    for j in range(0, len(spellcardKeys)-1):
        playerDeck.items.append(SpellCard(*getValuesFromDict(spellCards[spellcardKeys[j]], "name", "attack", "effect", "image")))
        computerDeck.items.append(SpellCard(*getValuesFromDict(spellCards[spellcardKeys[j]], "name", "attack", "effect", "image")))

    playerDeck.randomise()
    computerDeck.randomise()

    app = App()
    app.mainloop()
