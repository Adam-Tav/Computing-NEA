#Imports programmingTools. It contains my Stack class, which is needed for the decks and discard piles
from programmingTools import *
#Imports random, which is needed for shuffling
import random
#Imports the 
from card import *
import json
import customtkinter as ctk
from tkinter import *
from PIL import Image
import requests as rq
import svgwrite as svgw

#Opens up the .json files that contain the dictionaries with the information about the 
# troop cards to allow the addition of the card names to the deck and to create the card objects
with open("troopCards.json","r") as troopOptions:
    troopCards = json.load(troopOptions)

with open("spellCards.json","r") as spellOptions:
    spellCards = json.load(spellOptions)

cardBack = ctk.CTkImage(dark_image = Image.open("cardBack.png"), size = (120, 180))

allCards = list(troopCards.keys()) + list(spellCards.keys())

random.shuffle(allCards)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cards and Capers")
        self.geometry("1024x768")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.gameScreen = ctk.CTkFrame(self, fg_color="transparent")
        self.gameScreen.grid(row=0, column=0)

        self.playerPilesFrame = ctk.CTkFrame(self.gameScreen, fg_color="transparent")
        self.playerPilesFrame.grid(row=3, column=2, sticky="se", pady=15)

        self.drawPile = ctk.CTkButton(self.playerPilesFrame, fg_color="transparent", text="", height=180, width=120, command=self.drawCard, image=cardBack)
        self.drawPile.pack(side=ctk.LEFT)
        self.discardPile = ctk.CTkButton(self.playerPilesFrame, fg_color="transparent", text="", height=180, width=120, command=quit, image=cardBack) #Consider replacing quit with a proper discard function
        self.discardPile.pack(side=ctk.RIGHT, padx=20)

        self.computerPilesFrame = ctk.CTkFrame(self.gameScreen, fg_color="transparent")
        self.computerPilesFrame.grid(row=0, column=0, sticky="nw", pady=15)

        self.computerDrawPile = ctk.CTkButton(self.computerPilesFrame, fg_color="transparent", text="", height=180, width=120, hover=False, image=cardBack) # Give unique names
        self.computerDrawPile.pack(side=ctk.RIGHT)
        self.computerDiscardPile = ctk.CTkButton(self.computerPilesFrame, fg_color="transparent", text="", height=180, width=120, hover=False, image=cardBack) # Give unique names
        self.computerDiscardPile.pack(side=ctk.LEFT, padx=10)

        self.handFrame = ctk.CTkFrame(self.gameScreen, fg_color="transparent")
        self.handFrame.grid(row=3, column=1, pady=15, padx=60, sticky="s")

        self.computerHandFrame = ctk.CTkFrame(self.gameScreen, fg_color="transparent")
        self.computerHandFrame.grid(row=0, column=1, padx=30, pady=15, sticky="n")

        self.tableFrame1 = ctk.CTkFrame(self.gameScreen, fg_color="#704F32")
        self.tableFrame1.grid(row=1, column=1)

        self.tableFrame2 = ctk.CTkFrame(self.gameScreen, fg_color="#704F32")
        self.tableFrame2.grid(row=2, column=1)

        self.maxHandSize = 5
        self.maxPlayedCards = 3
        self.playerHand = []
        self.computerHand = []
        self.playerPlayTable = []

        self.create_hand(self.handFrame, self.playerHand, self.play_card) # Create player hand
        self.create_hand(self.computerHandFrame, self.computerHand, None, hover=False) # Create computer hand

    def create_hand(self, parent_frame, hand_list, command=None, hover=True):
        """Creates a hand of card buttons."""
        for i in range(self.maxHandSize):
            card_button = ctk.CTkButton(parent_frame, fg_color="transparent", text="", height=180, width=120, command=lambda i=i: command(i) if command else None, image=cardBack, hover=hover)
            card_button.pack(side=ctk.LEFT, padx=10 if i % 2 == 0 else 0)  # Alternating padx
            hand_list.append(card_button)

    def drawCard(self):
        if len(self.playerHand) < self.maxHandSize:
            self.cardIndex = random.randint(0, len(allCards) - 1) # Corrected index
            card_name = allCards[self.cardIndex]
            if card_name in troopCards:
                self.newCardObject = TroopCard(*getValuesFromDict(troopCards[card_name], "name", "attack", "effect", "health", "defence", "image"))
            elif card_name in spellCards:
                self.newCardObject = SpellCard(*getValuesFromDict(spellCards[card_name], "name", "attack", "effect", "image"))
            else:
                print(f"Card not found in dictionaries: {card_name}")
                return # Stop drawing if card not found

            # Find the first empty slot in hand
            for i, button in enumerate(self.playerHand):
                if button.cget("image") == cardBack: # Check if it's a placeholder
                    button.configure(image=self.newCardObject.image, command=lambda i=i: self.play_card(i))
                    return # Card added, exit the function
            else:
                print("No empty slots in hand")

    def play_card(self, card_index):
        if len(self.playerPlayTable) < self.maxPlayedCards:
            card_button = self.playerHand[card_index]
            new_card = ctk.CTkButton(self.tableFrame2, fg_color="transparent", text="", height=180, width=120, image=card_button.cget("image"))
            new_card.pack(padx=10, side=ctk.LEFT)
            self.playerPlayTable.append(new_card)

            card_button.configure(image=cardBack, command=None) # Reset the card slot
            print(self.playerPlayTable)

# Example usage (replace with your actual data):
playerHand = []
computerHand = []
# ... (Your card data and image loading)
if __name__ == "__main__":
    app = App()
    app.mainloop()