# CMPT120
# Name: Steven Wong
# Protein: Analyzes the amino acids in a protein sequence
# Date: February 7, 2022

# Dictionary containing full names of amino acids
proteinType = {'A': 'Alanine', 'D': 'Aspartic Acid', 'F': 'Phenylalanine',
               'G': 'Glycine', 'M': 'Methionine', 'T': 'Threonine', 'E': 'Error'}

# Dictionary to store count of respective amino acids
proteinCount = {'A': 0, 'D': 0, 'F': 0, 'G': 0, 'M': 0,
                'T': 0, 'error': 0}

# Get DNA sequence from user for analysis
proteinSeq = input("Enter an amino acid sequence: \n").upper()
proteinLength = len(proteinSeq)

# list of valid protein types 
list = ['A', 'D', 'F', 'G', 'M','T']

# Counts frequency of valid amino acids
for char in proteinSeq:
  if char in list: 
    proteinCount[char]+=1
  else:
    proteinCount['error']+=1

# Prints a report based on the first and last characters of the protein sequence
if proteinSeq[0] not in list and proteinSeq[proteinLength-1] not in list:
    print("REPORT ON PROTEIN: * -- *")
elif proteinSeq[0] not in list:
    print("REPORT ON PROTEIN: * --", proteinSeq[proteinLength-1])
elif proteinSeq[proteinLength-1] not in list:
    print("REPORT ON PROTEIN:", proteinSeq[0], "-- *")
else:
    print("REPORT ON PROTEIN: ", proteinSeq[0], "--", proteinSeq[proteinLength-1])

print("Sequence Length:", proteinLength)

# Iterates over the keys of both dictionaries and prints their respective values
for amino,count in zip(proteinType, proteinCount):
    print(f"{proteinType[amino]}: {proteinCount[count]},",
          f"{(proteinCount[count]/proteinLength*100):.3f}", "%")


