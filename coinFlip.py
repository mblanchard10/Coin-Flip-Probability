#Mike Blanchard
#Coin Flip Probability 

import random
import math

def coinFlip():
    num_flips = int(input("How many times would you like to flip the coin?: "))
    heads = 0
    tails = 0
    y = 0
    x = 0

    #random coin generator
    for i in range(0,num_flips):
        flip = random.randint(0,1)
        if flip == 0:
            heads += 1
        else:
            tails += 1
    
    #all possible outcomes (f in e/f)
    f = float(2**num_flips)

    #Enter guess for amount of heads
    heads_guess = int(input("\nEnter number of heads: "))

    #calculation for probability of getting the specified number of heads
    x = math.factorial(heads_guess)
    y = math.factorial(num_flips) / (math.factorial(num_flips - heads_guess))

    #e in e/f
    e = float(y / x)
    e_percent = (e/f) * 100
    
    #output
    print("\nThe calculated probability in (E/F): ",e,"/",f)
    print("\nThe calculated probability as a percentage: %",round(e_percent, 3))
    print("\nThe totals for each side regarding this flip were:")
    print("Heads: ", heads)
    print("Tails: ", tails)

def main():
    print("Welcome to coin toss!\n")
    coinFlip()
        
if __name__ == "__main__": 
    main() 
