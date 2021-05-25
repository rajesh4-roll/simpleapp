"""
    File: nimm.py
    -------------------------------------------
    This program plays an Ancient game of Nimm
"""

def Nimm():
    total_stones = 20
    turn = 1 # first turn for player 1 and 2 turn for player 2
    while (total_stones > 0):
        # total no of stones 
        print("There are",total_stones,"stones left")
        # turn for plaery 1
        if turn ==1 :
            play1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            #taking no of 1 and 2 stones as inputs only up to last 
            while play1 != 1 and play1 != 2:
                play1 = int(input("Please enter 1 or 2: "))
            if play1 <= total_stones:
                total_stones = total_stones - play1
            else:
                while play1 != 1:
                    play1 = int(input("Please enter 1 or 2: "))
            print('')
            # anther players turn
            turn = 2
        #  same as player 1 strategy logic
        else:
            play2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while play2 != 1 and play2 != 2:
                play2 = int(input("Please enter 1 or 2: "))
            if play2 <= total_stones:
                total_stones = total_stones - play2
            else:
                while play2 != 1:
                    play2 = int(input("Please enter 1 or 2: "))
            print('')
            turn = 1
        if total_stones == 0 and turn == 1:
            print("Player 1 wins!")
        if total_stones == 0 and turn == 2:
            print("Player 2 wins!")
        
# if __name__ == '__main__':
#     main()

