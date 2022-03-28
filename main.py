
##############################################################################################################################################
##### Implementing a Guessing Game where either the computer generates a random number, or the user selects a random number of their own ####
##############################################################################################################################################


import random

def guess (x):

    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input("Guess a number between 1 and {}  : ".format(x)))
        print(guess)

        if guess < random_number:
            print('Sorry, guess again! Guess too low')
        elif guess > random_number: 
            print('Sorry, guess again! Guess too large')
    
    print('Congrats! You guessed the number {} correctly!'.format(random_number))


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input('Is {} too high (h), too low (l) or correct (c)??'.format(guess)).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    
    print('Yay, i guessed your number {} correctly!'.format(guess))


#guess(1000)
computer_guess(1000)