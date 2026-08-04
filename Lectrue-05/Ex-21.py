#This program simulates 10 tosses of a coin.
import random

#Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for count in range(TOSSES):
        #Simulate a coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

#Call the main function.
main()