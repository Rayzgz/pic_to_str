""" Transform a RGB256 picture to character picutre 

Theory:
characters can be viewed as a large 'pixel' and therefore a character can be viewed as color
To transform rgb to characters, we use the gray sacle:
    gray can range from black 0-255 white   
Therefore a grayscale picture can also be called black-white picture

The equation to transform rgb --> grayscale is :
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

Execution:
enter the following commands
    $ python3 pic_to_str.py XXX.png
    $ vim output.txt
"""

from PIL import Image
import argparse

# get parser
parser = argparse.ArgumentParser()

# specify the output with arguments
parser.add_argument('file')     
parser.add_argument('-o', '--output')   
parser.add_argument('--width', type = int, default = 80) 
parser.add_argument('--height', type = int, default = 80) 
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# list of available characters
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# function to determine strings from the picture
# transferring from rgb 256 to gray scale
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' ' # default
    length = len(ascii_char) 

    # transform function
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # transfer units to index into the list of characters
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

# will not be executed if imported
if __name__ == '__main__':

    # get the image
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    # transform into characters
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    # output to a file
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
