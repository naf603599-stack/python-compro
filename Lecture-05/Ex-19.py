#This program simulates 10 toses of a coin.
import random

#Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for count in range(TOSSES):
        #Simulate a coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

#Call the main function.
tosses_coin()