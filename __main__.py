import stack
import random



#cards will be updated to OOP, each index referring to a different card subclass
#index 0 of each sub-array is the name of the card, index 1 is the health of the card, index 2 is the attack power of each card, index 3 is the defence of each card

import random

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
   """  player_card_choice = int(input("Which card number do you want to choose (1-10): ")) - 1
    computer_card_choice = random.randint(1,len(computer_hand))
    print(player_card_choice)
    print(computer_card_choice)
    if player_hand[player_card_choice, 3] > computer_hand[computer_card_choice, 3]:
        computer_hand[computer_card_choice, 2] -= (player_hand[player_card_choice, 3] - computer_hand[computer_card_choice, 4])
    
    elif player_hand[player_card_choice, 3] == computer_hand[computer_card_choice, 3]:
        computer_hand[computer_card_choice, 2] -= (player_hand[player_card_choice, 3] - computer_hand[computer_card_choice, 4])
        player_hand[player_card_choice, 2] -= (computer_hand[computer_card_choice, 3] - player_hand[player_card_choice, 4])
    else:
        player_hand[player_card_choice] """
   pass

if __name__ == "__main__":
    playerDeck = stack()
    computerDeck = stack()
    for i in range(12):
        playerDeck.add_card()
        print(playerDeck)




