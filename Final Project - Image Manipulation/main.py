# Course: CMPT120
# Program: Final Assignment: Color Project
# Authors: Andrea Reyes (D200, 301539812), Steven Wong (D100, 301337727)
# Canvas Group: 136
# Date: April 11, 2022


# Import the helper program which contains all the functions necessary for Color Project
import cmpt120colours as cm


# Function that prints the color project menu options
def menu():
    m = {
        '\n1.': 'Load Colour File',
        '2.': 'Print all colours',
        '3.': 'Select Colour',
        '4.': 'Find closest colour',
        '5.': 'Display (save) Colour Scheme',
        '0.': 'Quit'
    }
    for elem in m:
        print(elem, m[elem])


# Function that prints the colors inside the dictionary
def print_colors(colordic):
    print(f"{'Colour Name' : <10}{'Red' : ^10}{'Green' : ^8}{'Blue' : >8}{'Hex': >12}")
    print(f"{'-----------' : <10}{'---' : ^10}{'----' : ^8}{'----' : >8}{'----': >12}")
    for colors in colordic:
        colorname = colordic[colors][0].title()
        r = int(colors[0])
        g = int(colors[1])
        b = int(colors[2])
        rgb = (r, g, b)
        colordic[(rgb)] = colorname, cm.hex_conversion(rgb)
        print(
            f"{colordic[(rgb)][0]: <10}{rgb[0]: ^10}{rgb[1]: ^10}{rgb[2] : >5}"
            f"{colordic[r, g, b][1]:>15}")


# Function that loads colors from a CSV file named colours.csv
def load_color_file():
    file = open('colours.csv')
    numcolor = 0
    for line in file:
        colors = line.split(',')
        colorname = colors[0].title()
        r = int(colors[1])
        g = int(colors[2])
        b = int(colors[3])
        rgb = (r, g, b)
        if rgb not in colordic:
            colordic[(rgb)] = colorname, cm.hex_conversion(rgb)
            numcolor += 1
    print('The file has been processed and ' + str(
        numcolor) + ' colours were entered into the dictionary')
    return colordic


menu()
colordic = {}  # Creates an empty dictionary for use in the color project
color = True
while (color):
    user_choice = input('\nselect an option: ')
    # if user selects Option 1, we load the file and tell the user how many colors are in the file.
    if user_choice == '1':
        colordic.update(load_color_file())
        menu()

    # If user selects Option 2, we print the colors with their hexadecimal and rgb values
    elif user_choice == '2':
        print_colors(colordic)
        menu()

    # if user selects Option 3, we allow the user to select a color
    elif user_choice == '3':
        userColor = cm.get_user_color()
        if cm.find_color(userColor, colordic) is True:
            print(
                f'\nColor {userColor} is {colordic[userColor][0]} and has hex code '
                f'{colordic[userColor][1]}')
            menu()
        else:
            print(f'\nColor {userColor} not found. Would you like to:')
            not_found_choice = input(
                "1. Enter a name for this colour\n2. Return to the Main Menu\n")
            if not_found_choice == '1':
                colName = input("What is the colour's name? ").title()
                colordic[userColor] = [colName, cm.hex_conversion(userColor)]
                print(
                    f'Color {userColor} is {colName} and has hex code '
                    f'{cm.hex_conversion(userColor)}')
            else:
                menu()

    # If user selects Option 4, we print the closest color from the dictionary
    elif user_choice == '4':
        userColor = cm.get_user_color()
        if cm.find_color(userColor, colordic) is True:
            print(
                f'Color {userColor} is {colordic[userColor][0]} and has hex code'
                f' {colordic[userColor][1]}')
            menu()
        else:
            closestColor = cm.getCloseColor(colordic, userColor)
            name_closest_color = colordic[closestColor][0]
            hex_closest_color = colordic[closestColor][1]
            print(
                f'The closest color to {userColor} is {closestColor}, {name_closest_color}'
                f', with hex code {hex_closest_color}.')
            print(
                f'The absolute difference between the two colors is '
                f'{cm.get_abs_diff_sum(userColor, closestColor)}.')
            menu()

    # If user selects Option 5, display a monochromatic or complementary color scheme
    elif user_choice == '5':
        userColor = cm.get_user_color()
        color_comp = [(255 - userColor[0]), (255 - userColor[1]), (255 - userColor[2])]
        print('which color scheme do you wish to display')
        color_display = input('M: Monochrome and C: Complementary ').upper()
        if color_display == 'M':
            cm.monochrome(userColor)
        elif color_display == 'C':
            cm.compandmono(userColor, color_comp)
        menu()

    # If user selects Option 0, quit the program
    elif user_choice == '0':
        print('Goodbye!')
        color = False
