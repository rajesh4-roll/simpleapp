
import sys 
sys.path.append('games')
from games_image import game
from images import image
from games import games
from math_main import green

def main():
    print('**********************************************************************')
    print('*                       Simple Application                           *')
    print('**********************************************************************')
    print('1. Games')
    print('2. Images')
    print('3. Mathematics')
    _input = int(input('Enter choice: '))
    print()
    if _input == 1:
        games()
    elif _input == 2:
        image()
    elif _input == 3:
        green()
    else:
        print('Invalid Choice !!!')

if __name__ == '__main__':
    main()