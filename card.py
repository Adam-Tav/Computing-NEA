import json
from programmingTools import *
import customtkinter as ctk
from tkinter import *
from dataclasses import dataclass
from typing import List, Union, Optional

with open("troopCards.json","r") as troops:
    troopCards = json.load(troops)

with open("spellCards.json","r") as spells:
    spellCards = json.load(spells)

#troop card class, will pull on troopCards.json to instantiate the different troop cards available
@dataclass
class TroopCard:
    name:str
    attack:int
    effect:Optional[str] # allows a str or none value
    health:int
    defence:int
    image:str = "C:\\Users\\adamt\\OneDrive\\School\\Computing\\Computing NEA\\cardBack.webp"

#spell card class, will pull on spellCards.json to instantiate the different spell cards available
@dataclass
class SpellCard:
    name:str
    attack: Optional[int] # Allows an int or none value
    effect:str
    image:str = "C:\\Users\\adamt\\OneDrive\\School\\Computing\\Computing NEA\\cardBack.webp"

@dataclass
class Hand:
    cards: List[Union[TroopCard, SpellCard]] # Allows a list of Troop and Spell Cards

