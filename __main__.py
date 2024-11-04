import stack
import random
import card

#cards will be updated to OOP, each index referring to a different card subclass
#index 0 of each sub-array is the name of the card, index 1 is the health of the card, index 2 is the attack power of each card, index 3 is the defence of each card

shuffle = lambda deck : random.shuffle(deck.contents) #shuffling algorithm to shuffle the player's deck, TODO

def deal_cards(): #deals the player's hand of 10 cards
   """  for i in range(10): #deals 10 cards into the player's hand
        nextCard = playerDeck[len(playerDeck)-1]
        del(playerDeck[len(playerDeck)-1])
        playerHand.append(nextCard)
        print(playerHand)
    
    for i in range(10): #deals the computer's hand of 10 cards
        nextCard = computerDeck[len(computerDeck)-1]
        del(computerDeck[len(computerDeck)-1])
        computerHand.append(nextCard)
        print(computerHand) """
   pass



def combat(): #simple combat algorithm - update when shift over to OOP with more complex combat modules - status effects etc.
   """  playerCardChoice = int(input("Which card number do you want to choose (1-10): ")) - 1
    computerCardChoice = random.randint(1,len(computerHand))
    print(playerCardChoice)
    print(computerCardChoice)
    if playerCand[playerCardChoice, 3] > computerHand[computerCardChoice, 3]:
        computerHand[computerCardChoice, 2] -= (playerHand[playerCardChoice, 3] - computerHand[computerCardChoice, 4])
    
    elif playerHand[playerCardChoice, 3] == computerHand[computerCardChoice, 3]:
        computerHand[computerCardChoice, 2] -= (playerHand[playerCardChoice, 3] - computerHand[computerCardChoice, 4])
        playerHand[playerCardChoice, 2] -= (computerHand[computerCardChoice, 3] - playerHand[playerCardChoice, 4])
    else:
        playerHand[playerCardChoice] """
   pass

if __name__ == "__main__":
    playerDeck = stack()
    computerDeck = stack()

    inf = card.TroopCard()

    for i in range(10):
        playerDeck.addCard()
        print(playerDeck)




