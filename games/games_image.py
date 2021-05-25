from guess_number import guess_number
from nimm import Nimm
from rps import  RPS
from three_in_a_row import three_inarow

def game():
    print()
    print('1. Number Guess')
    print('2. Three in a row')
    print('3. Rock Paper Scissors')
    print('4. Ancient game of Nimm')
    _input  = int(input("Enter your choice: "))
    print()
    if _input == 1:
        guess_number()
    elif _input == 2:
        three_inarow()
    elif _input == 3:
        RPS()
    elif _input == 4:
        Nimm()
    else:
        print('Invalid Choice !!!')


# if __name__ == '__main__':
#     main()