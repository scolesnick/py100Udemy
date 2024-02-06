############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random as rand
from art import logo
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# deal the cards
def dealCard(playerHand):
    playerHand.append(rand.choice(cards))

# check for 11 (ace) in hand and replace with 1 if over 21
def replaceAce(playerHand):
    if sum(playerHand) > 21 and 11 in playerHand:
        idx = playerHand.index(11) 
        playerHand[idx] = 1

def playGame():
    # Using a dictionary to store dealer and user cards
    hands = {'d': [], 'p1': []}

    # Dealer deals to themself, player, a hidden card to themself and player again
    dealCard(hands['d'])
    dealCard(hands['p1'])
    dealCard(hands['d'])
    dealCard(hands['p1'])

    # Print the cards
    print(f"Your cards: {hands['p1']}")
    print(f"Dealer\'s first card: {hands['d'][0]}\n")

    # The player will choose if they want to hit until they bust or stop
    hit = input('Hit? (type hit or no): ')
    playerBust = False
    while hit.lower() == 'hit' and playerBust == False:
        dealCard(hands['p1'])
        replaceAce(hands['p1'])
        if sum(hands['p1']) > 21:
            playerBust = True
            print(f"You drew {hands['p1'][-1]} and bust at {sum(hands['p1'])}")
        else:
            print(f"You drew {hands['p1'][-1]}")
            hit = input('Hit? (type hit or no): ')

    # Once the player is done and has not bust, the Dealer reveals the card and draws until winning, hitting 21 for draw or busting
    end = sum(hands['d']) == 21 or sum(hands['d']) > sum(hands['p1']) 
    while not end and not playerBust:
        dealCard(hands['d'])
        replaceAce(hands['d'])
        end = sum(hands['d']) >= 21 or sum(hands['d']) > sum(hands['p1'])

    # Show final hands
    print(f"\nYour final hand: {hands['p1']}")
    print(f"Dealer's final hand: {hands['d']}\n")

    # determine who won
    dealerSum = sum(hands['d'])
    playerSum = sum(hands['p1'])

    if playerSum > 21:
        print('Player busts, Dealer wins')
    elif dealerSum > 21:
        print('Dealer busts, Player wins')
    elif dealerSum == playerSum:
        print('It was a draw')
    elif dealerSum > playerSum:
        print(f'Dealer wins with a score of {dealerSum}')
    elif playerSum > dealerSum:
        print(f'Player wins with a score of {playerSum}')

playingGame = True

while playingGame:
    os.system('cls')
    print(logo)
    playGame()
    playingGame = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ') == 'y'