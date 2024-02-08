# Player has to guess which person on instagram has a higher follower count
# Shown follower count for person A and person term B, guess if the follower count is higher or lower.
# Player is shown their score at the end and asked if they would like to play again.

import art
import game_data as gd
import os
import random as rand

def getPair():
    listData = rand.shuffle(gd.data)
    a = listData.pop(0)


again = True

while again:
    correct = True
    score = 0
    listData = rand.shuffle(gd.data)
    a = listData.pop(0)
    while correct:
        if listData == 0:
            listData = rand.shuffle(gd.data)
            if listData[0] == a:
                listData.pop(0)
        b = listData.pop(0)

        print(art.logo)
        # If scored correct print score
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

        guess = ''
        while guess.lower() != 'a' and guess.lower() != 'b':
            guess = input("Who has more followers? Type 'A' or 'B': ")
        
        # Compare and add score if correct
        higher = ''
        if a['follower_count'] > b['follower_count']:
            higher = 'a'
        else:
            higher = 'b'
        if guess.lower() == higher:
            score += 1
            a = b
        else:
            correct = False:
        
        # Clear screen
        os.system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
)
