# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:10:46 2018

@author: Kostya
"""
from random import shuffle
import sys

#Creating cards deck
suits = ['h','d','s','c']
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = list((x,y) for x in suits for y in cards)
shuffle(deck)
print(deck)

#Function to calculate points
def total(hand):
    t = 0
    aces = 0
    for card in hand:
        t +=  value[cards.index(card[1])]
        if card[1] == 'A':
            aces += 1
    while t > 21 and aces > 0:
        t -= 10
        aces -= 1
    return t

dealer = []
player = []

#Start of the game - pairs
dealer.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
player.append(deck.pop())


#Checking pairs
if total(player) == 21 and total(dealer) == 21: 
    print("Both dealer and you got blackjack, you lost")
    print("Dealer cards: ", dealer)
    print("Your cards: ", player)
    sys.exit()
elif total(player) == 21: 
    print("You got blackjack and won")
    print("Dealer cards: ", dealer)
    print("Your cards: ", player)
    sys.exit()
elif total(dealer) == 21:
    print("Dealer got blackjack, you lost")
    print("Dealer cards: ", dealer)
    print("Your cards: ", player)
    sys.exit()

print("Your cards: ", player)
print("One of dealer cards: ", dealer[0])
decision = input("Please enter 1 if you need another card or 2 if you are done")
while decision not in ('1','2'):
    print("Please enter 1 or 2")
    decision = input("Please enter 1 if you need another card or 2 if you are done")


#Game continues - player's turn
while decision == '1':
    player.append(deck.pop())
    if total(player) > 21:
        print("You exceeded 21 and lost")
        print("Dealer cards: ", dealer)
        print("Your cards: ", player)
        sys.exit()
    elif total(player) == 21:
        print("You got blackjack and won")
        print("Dealer cards: ", dealer)
        print("Your cards: ", player)
        sys.exit()
    print("Your cards: ", player)
    decision = input("Please enter 1 if you need another card or 2 if you are done")
    while decision not in ('1','2'):
        print("Please enter 1 or 2")
        decision = input("Please enter 1 if you need another card or 2 if you are done")


#Dealer's turn
while total(dealer) < 17:
    dealer.append(deck.pop())
    if total(dealer) > 21:
        print("Dealer exceeded 21 and lost")
        print("Dealer cards: ", dealer)
        print("Your cards: ", player)
        sys.exit()
    elif total(dealer) == 21:
        print("Dealer got blackjack, you lost")
        print("Dealer cards: ", dealer)
        print("Your cards: ", player)
        sys.exit()

#Final check
if total(player) > total(dealer):
    print("You got ", total(player), "points. Dealer got ", total(dealer), "points. You won")
    print("Dealer cards: ", dealer)
    print("Your cards: ", player)
    sys.exit()
else:
    print("You got ", total(player), "points. Dealer got ", total(dealer), "points. You lost")
    print("Dealer cards: ", dealer)
    print("Your cards: ", player)
    sys.exit()
    




        
        
