# Course: CMPT120
# Program: Final Assignment: Color Project Helper Program
# Authors: Andrea Reyes (D200, 301539812), Steven Wong (D100, 301337727)
# Canvas Group: 136
# Date: April 11, 2022

# Import functions to manipulate and save images
import cmpt120image as ci

# Takes an RGB tuple, the percentage to be darkened by, and returns a darkened RGB tuple
def darken(col_tuple, percentage):
    lst = list(col_tuple)
    for elem in range(len(lst)):
        lst[elem] = int(lst[elem] * percentage)
    return tuple(lst)


# Takes an RGB tuple, the percentage to be lightened by, and returns a lightened RGB tuple
def lighten(col_tuple, percentage):
    lst = list(col_tuple)
    for col in range(len(lst)):
        lst[col] += int((255 - lst[col]) * percentage)
    return tuple(lst)


# Returns the absolute difference between two RGB tuples as an integer
def get_abs_diff_sum(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2)


# Returns the closest color value from a chosen RGB tuple
def getCloseColor(col_dict, user_col):
    list_colors = list(col_dict.keys())
    closest = list_colors[0]
    lowest_abs_value = get_abs_diff_sum(user_col, list_colors[0])

    for color in list_colors[1:]:
        current_elem_absolute = get_abs_diff_sum(user_col, color)
        if color == user_col:
            return color
        elif current_elem_absolute <= lowest_abs_value:
            lowest_abs_value = current_elem_absolute
            closest = color
    return closest


# Search a color dictionary to see if it contains a chosen RGB value
def find_color(seeking_color, colordic):
    for color in colordic:
        if seeking_color == color:
            return True


# Gets RGB values as input from user, converting it to a RGB tuple
def get_user_color():
    # Create empty List to append user inputted RGB value
    user_rgb = []
    rgb_options = ("R: ", "G: ", "B: ")
    print("Enter the RGB values of your colour. (0-255)")
    for elem in rgb_options:
        k = int(input(elem))
        user_rgb.append(k)
    color_tuple = tuple(user_rgb)
    return color_tuple


# Convert an RGB tuple to hexadecimal string
def hex_conversion(rgb):
    hex_code = "#"
    for i in rgb:
        if i < 15:
            # Replace the single integer with leading zeroes
            hex_code = hex_code + hex(i).replace("0x", "0").upper()
        else:
            hex_code = hex_code + hex(i).lstrip("0x").upper()
    return hex_code


# Generates a 480x240 image containing monochromatic and complementary color schemes
def compandmono(user_color, comp_color):
    new_img = ci.getBlackImage(480, 240)
    height = len(new_img)
    width = len(new_img[0])

    for row in range(height):
        for col in range(width):
            if row < 80 and col < 80:
                new_img[row][col] = lighten(user_color, 0.8)
            elif row < 80 and 160 <= col < 240:
                new_img[row][col] = lighten(user_color, 0.5)
            elif 160 <= row < 240 and col < 80:
                new_img[row][col] = darken(user_color, 0.5)
            elif 160 <= row < 240 and 160 <= col < 240:
                new_img[row][col] = darken(user_color, 0.8)
            elif col < 240:
                new_img[row][col] = [user_color[0], user_color[1], user_color[2]]
            elif row < 80 and 400 <= col < 480:
                new_img[row][col] = lighten(comp_color, 0.8)
            elif row < 80 and 240 <= col < 320:
                new_img[row][col] = lighten(comp_color, 0.5)
            elif 160 < row and 240 <= col < 320:
                new_img[row][col] = darken(comp_color, 0.5)
            elif 160 < row and 400 < col:
                new_img[row][col] = darken(comp_color, 0.8)
            else:
                new_img[row][col] = [comp_color[0], comp_color[1], comp_color[2]]
    ci.showImage(new_img)
    ci.saveImage(new_img, 'cscheme.png')

    # for row in range(height):
    #     for col in range(width):
    #         if col < 80 and row < 80:
    #             new_img[row][col] = lighten(user_color, 0.8)
    #         elif col >= 80 and col <= 160:
    #             new_img[row][col] = user_color
    #         else:
    #             new_img[row][col] = lighten(user_color, 0.5)
    #
    #
    # for row in range(80):
    #     for col in range(240):
    #         if col < 80:
    #             new_img[row][col] = lighten(user_color, 0.8)
    #         elif col >= 80 and col <= 160:
    #             new_img[row][col] = user_color
    #         else:
    #             new_img[row][col] = lighten(user_color, 0.5)
    #
    # for row in range(80, 160):
    #     for col in range(240):
    #         new_img[row][col] = user_color
    #
    # for row in range(160, 240):
    #     for col in range(240):
    #         if col < 80:
    #             new_img[row][col] = darken(user_color, 0.8)
    #         elif col >= 80 and col <= 160:
    #             new_img[row][col] = user_color
    #         else:
    #             new_img[row][col] = darken(user_color, 0.5)
    #
    # for row in range(80):
    #     for col in range(240, 480):
    #         if col < 320:
    #             new_img[row][col] = lighten(comp_color, 0.5)
    #         elif col >= 320 and col <= 400:
    #             new_img[row][col] = comp_color
    #         else:
    #             new_img[row][col] = lighten(comp_color, 0.8)
    #
    # for row in range(80, 160):
    #     for col in range(240, 480):
    #         new_img[row][col] = comp_color
    #
    # for row in range(160, 240):
    #     for col in range(240, 480):
    #         if col < 320:
    #             new_img[row][col] = darken(comp_color, 0.5)
    #         elif col >= 320 and col <= 400:
    #             new_img[row][col] = comp_color
    #         else:
    #             new_img[row][col] = darken(comp_color, 0.8)



# Generates a 240x240 image containing monochromatic color scheme
def monochrome(color):
    img = ci.getBlackImage(240, 240)
    height = len(img)
    width = len(img[0])

    for row in range(height):
        for col in range(width):
            if row < 80 and col < 80:
                img[row][col] = lighten(color, 0.8)
            elif row < 80 and 160 <= col < 240:
                img[row][col] = lighten(color, 0.5)
            elif 160 <= row < 240 and col < 80:
                img[row][col] = darken(color, 0.5)
            elif 160 <= row < 240 and 160 <= col < 240:
                img[row][col] = darken(color, 0.8)
            else:
                img[row][col] = [color[0], color[1], color[2]]

    ci.showImage(img)
    ci.saveImage(img, 'cscheme.png')
