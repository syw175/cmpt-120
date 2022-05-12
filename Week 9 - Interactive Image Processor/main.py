# Course: CMPT120
# Program: Interactive Image Processor
# Author: Steven Wong
# Date: March 25, 2022

import cmpt120image
from cmpt120imageManip import swapRedGreen
from cmpt120imageManip import blackWhite
from cmpt120imageManip import reflect
from cmpt120imageManip import brighten
from cmpt120imageManip import reload

# Load bird image to be manipulated
img = cmpt120image.getImage("bird.png")

# Initialize list of available image filter options
optionNum = ("1:", "2:", "3:", "4:", "5:", "0:")
option = ("Swap red and green", "Convert to black and white", "Reflect", "Brighten", "Reload Image", "Quit")

# Print lists of image filter options
print("FILTERS")
for i in range(len(option)):
    print(optionNum[i], option[i])


# Allow user to make multiple image manipulations until '0' is pressed
selection = 1
while selection != 0:
    selection = input("Enter 1 to 5, 0 to quit: ")
    if selection == '1':  # Swap red and green RGB values
        cmpt120image.showImage(swapRedGreen(img))
        cmpt120image.saveImage(swapRedGreen(img), 'swapRedGreen.png')

    elif selection == '2':  # Transform picture into B&W
        cmpt120image.showImage(blackWhite(img))
        cmpt120image.saveImage(blackWhite(img), 'blackWhite.png')

    elif selection == '3':  # Reflect the image across the top
        cmpt120image.showImage(reflect(img))
        cmpt120image.saveImage(reflect(img), 'reflect.png')

    elif selection == '4':  # Brighten all RGB values in the image
        cmpt120image.showImage(brighten(img))
        cmpt120image.saveImage(brighten(img), 'brighten.png')
        img = brighten(img)

    elif selection == '5':  # Reload image to starting state
        img = reload()

    elif selection == '0':  # Quit program
        selection = 0
        print('Goodbye')

