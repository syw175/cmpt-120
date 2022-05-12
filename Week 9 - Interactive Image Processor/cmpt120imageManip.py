# Course: CMPT120
# Program: Interactive Image Processor
# Author: Steven Wong
# Date: March 25, 2022

import copy
import cmpt120image


# Iterate through 2D image array, returning an image with red and green RGB values swapped
def swapRedGreen(img):
    width = len(img[0])
    height = len(img)
    new_img = cmpt120image.getBlackImage(width, height)
    for row in range(height):
        for column in range(width):
            color = img[row][column]
            swapped = [color[1], color[0], color[2]]
            new_img[row][column] = swapped
    return new_img


# Iterate through 2D image array, returning a black and white image
def blackWhite(img):
    width = len(img[0])
    height = len(img)
    new_img = cmpt120image.getBlackImage(width, height)
    for row in range(height):
        for column in range(width):
            color = img[row][column]
            max_color_value = 256 + 256 + 256
            sum_color_value = color[0] + color[1] + color[2]
            if sum_color_value < (max_color_value/2):
                new_color = [0, 0, 0]
            else:
                new_color = [255, 255, 255]
            new_img[row][column] = new_color
    return new_img


# Iterate through 2D image array, returning an image reflected across the middle
def reflect(img):
    width = len(img[0])
    height = len(img)
    new_img = cmpt120image.getBlackImage(width, height)
    for row in range(height//2):
        for column in range(width):
            color = img[row][column]
            new_img[row][column] = color
            new_img[-row][column] = color
    return new_img


# Iterate through 2D image array, returning an image brightened by a factor of 1.1
def brighten(img):
    new_img = copy.deepcopy(img)
    width = len(new_img[0])
    height = len(new_img)
    for row in range(height):
        for column in range(width):
            color = img[row][column]
            if color[0] < 229 and color[1] < 229 and color[2] < 229:
                new_color = [color[0]*1.1, color[1]*1.1, color[2]*1.1]
            else:
                new_color = img[row][column]
            new_img[row][column] = new_color
    return new_img


# Return the original image before any image processing procedures
def reload():
    img = cmpt120image.getImage('bird.png')
    return img







