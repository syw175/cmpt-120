# CMPT120
# College Major Report
# Author: Steven Wong

# If the user inputted major is found, return the key of the dictionary value, else None
def find_key():
    for key, value in majorCat.items():
        for majors in value:
            if majorName == majors:
                return key
    return None


file = open('major_data.csv')  # Open college major report file
unneeded_header = file.readline()  # Disregard the first line with titles

# PART 1: OVERALL DATA
print("Welcome to the US College Major Earnings Report\n")

# Initialize counting variables
totalPeople = 0
totalIncome = 0
rowCount = 0

# Iterates through file and count #people, #income, and #lines
for line in file:
    majorData = line.split(",")
    totalPeople += int(majorData[3])  # Column of majorData[3] contains the People count
    totalIncome += int(majorData[8])  # Column of majorData[8] contains the Income count
    rowCount += 1  # Count rows in file for avg calculation

avgIncome = totalIncome // rowCount
print("Total number of people surveyed =", totalPeople)  # Prints total people in dataset
print("Overall average median income =", avgIncome, "\n")  # Prints avg median income
print("{:<40}".format("MAJOR"),  # Print Part 1 Title Headers
      "{:>15}".format("#PEOPLE"),
      "{:>15}".format("INCOME"),
      "{:>16}".format("INC/AVG"))

file.seek(0)  # Returns to beginning of file
unneeded_header = file.readline()  # Disregard the first line with titles

# Initialize major category, income, and unemployment dictionaries for use in Part 2
majorCat = {}
majorIncome = {}
majorUnemployment = {}

# Prepares dictionary for Part 2 and prints the list of Majors, # People, Income, and Income/Avg
for line in file:
    row = line.split(',')

    # Prepares the major category dictionary for use in Part 2
    # {'Education': ['GENERAL EDUCATION', 'EDUCATIONAL ADMINISTRATION', 'etc.'...],
    # 'Arts': ['FINE ART', 'DRAMA', 'etc.'...], ...}
    if row[2] not in majorCat:
        majorCat[row[2]] = [row[1]]
    else:
        majorCat[row[2]].append(row[1])

    # Prepares the income dictionary for use in Part 2
    # {'Agriculture & Natural Resources': ['50000', '54000', 'etc.'...], 'Arts': ['45000', ...]}...
    if row[2] not in majorIncome:
        majorIncome[row[2]] = [row[8]]
    else:
        majorIncome[row[2]].append(row[8])

    # Prepares the unemployment rate dictionary for use in Part 2 (See above for sample format)
    if row[2] not in majorUnemployment:
        majorUnemployment[row[2]] = [row[7]]
    else:
        majorUnemployment[row[2]].append(row[7])

    # Print out a table of #people, income, and average income sorted by major
    print("{:<40}".format(row[1].title()),
          "{:>15}".format(row[3]),
          "{:>15}".format(row[8]),
          "{:>15.3f}%".format(int(row[8]) / int(avgIncome) * 100))

print("END OF PART 1\n")

# PART 2: USER INTERACTION REQUIREMENT
# Ask the user to enter a major
majorName = input("Please enter the name of a major --> ").upper().strip(".,?! ")

# Check if the find_key function returned None before assignment of variables
if find_key() is not None:
    majorList = majorCat[find_key()]  # List of majors from the inputted major category
    unemployedList = majorUnemployment[find_key()]  # List of unemployment rates for inputted major
    incomeList = majorIncome[find_key()]  # List of income for inputted major
    majorPos = majorList.index(majorName)  # Index position of inputted major in list of majors

# If the user entered a valid major, print the category, headers, and related major statistics
if find_key() is None:
    print(majorName.title(), 'is not in the list')
else:
    print(majorName, "is in the", find_key(), "major category.")  # Print major category
    print("{:<35}".format("MAJOR"),  # Print out column headers
          "{:>20}".format("UNEMP"),
          "{:>15}".format("INCOME"),
          "{:>15}".format("INC +/-"))

    # Print the user inputted major first with an empty string for INC +/-
    print("{:<35}".format(majorList[majorPos].title()),
          "{:>19.2f}%".format(float(unemployedList[majorPos]) * 100),
          "{:>15}".format(incomeList[majorPos]),
          "{:>15}".format(" "))

    for major in range(len(majorCat[find_key()])):  # Print out statistics of other related majors
        if major != majorPos:  # for all majors that are not user inputted major
            print("{:<35}".format(majorList[major].title()),
                  "{:>19.2f}%".format(float(unemployedList[major]) * 100),
                  "{:>15}".format(incomeList[major]),
                  "{:>15}".format(int(incomeList[major]) - int(incomeList[majorPos])))
