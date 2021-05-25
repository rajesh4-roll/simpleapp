from simpleimage import SimpleImage

def filters():
    print()
    _image_input = input('Press enter for default image: ')
    print('1. Half Light')
    print('2. Red Filter')
    print('3. Blue Filter')
    print('4. Brown Filter')
    print('5. Green Filter')
    print('6. Greyscale Filter')
    _input = int(input('Enter choice: '))
    image = SimpleImage('images/quad.jpg')
    image.show()
    if _input == 1:
        # half light redution filter
        low_image = low_filter_half(image)
        low_image.show()
    elif _input == 2:
        # red filter image
        red_image = red_filter(image)
        red_image.show()
    elif _input == 3:
        # blue filter image
        blue_image = blue_filter(image)
        blue_image.show()
    elif _input == 4:
        # brown filter
        brown_image = brown_filter(image)
        brown_image.show()
    elif _input == 5:
        # green filter image
        green_image = green_filter(image)
        green_image.show()
    elif _input == 6:
        # greyscale filter image
        grey_image = grey_filter(image)
        grey_image.show()
    else:
        print('Invalid Choice !!!')


def red_filter(image):
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image

def brown_filter(image):
    for pixel in image:
        pixel.red = pixel.red / 2
        pixel.green = pixel.red / 2
        pixel.blue = pixel.green / 2
    return image

def green_filter(image):
    for pixel in image:
        pixel.red = 0
        pixel.blue = 0
    return image

def blue_filter(image):
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
    return image

def grey_filter(image):
    for pixel in image:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    return image

def low_filter_half(image):
    for pixel in image:
        pixel.red = pixel.red / 2
        pixel.green = pixel.green / 2
        pixel.blue = pixel.blue / 2
    return image

# if __name__ == '__main__':
#     main()