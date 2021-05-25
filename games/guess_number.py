"""
    File: guess_number.py
    ---------------------------------------------
    Generates a random number between 1 and 99.
    Has the user keep guessing until they figure out 
    what the number is. Tells the user after each guess
    if their guess was too high or too low.
"""

import random

def guess_number():
    print("I am thinking of a number between 0 and 99...")
    secrect_number = random.randint(0,99)
    guess_number = int(input("Enter a number: "))
    while guess_number != secrect_number:
        if guess_number >= secrect_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        print('')
        guess_number = int(input("Enter a number: "))
    print("Congrats! The number was: ",secrect_number)

# if __name__ == '__main__':
#     main()
