"""
    This file contains refltion and crop image from 
    that particular library
"""
from filter import filters
from reflection import made_ref
from trim_crop import crop
def image():
    print()
    print('1. Crop default image')
    print('2. Reflection of image')
    print('3. Filters')
    _input = int(input('Enter your choice: '))
    print()
    if _input == 1:
        crop()
    elif _input == 2:
        made_ref()
    elif _input == 3:
        filters()
    else:
        print('Invalid Choice !!!')


# if __name__ == '__main__':
#     main()