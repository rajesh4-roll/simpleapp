"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    # TODO: your code here.
    img_width = image.width
    img_height = image.height
    mirror = SimpleImage.blank(img_width,img_height * 2)
    for x in range(img_width):
        for y in range(img_height):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x,y,pixel)
            mirror.set_pixel(x,(img_height * 2)-(y+1),pixel)
    return mirror


def made_ref():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


# if __name__ == '__main__':
#     main()
