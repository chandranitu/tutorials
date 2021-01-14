

import random

def rollDice():
    roll = random.randint(1,100)
    return roll

# Now, just to test our dice, let's roll the dice 100 times. 

x = 0
while x < 100:
    result = rollDice()
    print(result)
    x+=1


-------
# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        print (roll,'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        print (roll,'roll was 1-50, you lose.')
        return False
    elif 100 > roll >= 50:
        print (roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True
