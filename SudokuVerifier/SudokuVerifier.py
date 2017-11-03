import csv

def load_puzzle(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        puzzle = []
        for row in reader:
            puzzle.append(row)
            i = i + 1
    return puzzle

def print_puzzle(puzzle):
    i = 0
    for row in puzzle:
        j = 0
        for element in row:
            print(element + " ", end="")
            j = j + 1
            if ( j % 9 == 0 ):
                print("")
            elif ( j % 3 == 0 ):
                print("|", end="")
        i = i + 1
        if ( i % 3 == 0 and i % 9 != 0 ):
            print("-------------------")
    print("");

def check_puzzle(puzzle):
    print("Checking puzzle...\n")

    row = check_row(puzzle);
    if (row == True):
        print("    Rows OK...")
    else:
        print("Row " + str(row) + " invalid.")
        print("Goodbye!")
        return

    col = check_col(puzzle);
    if (col == True):
        print("    Columns OK...")
    else:
        print("\nColumn " + str(col) + " invalid.")
        print("Goodbye!")
        return

    subgrid = check_subgrid(puzzle);
    if (subgrid == True):
        print("    Subgrids OK...\n")
        print("Puzzle solution correct!")
        print("Goodbye!")
    else:
        print("\nSubgrid " + str(subgrid) + " invalid.")
        print("Goodbye!")
        return

def check_row(puzzle):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    j = 0
    for row in puzzle:
        for number in numbers:
            if ( (number in row) == False ):
                return j
        j = j + 1
    return True

def check_col(puzzle):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, 9):
        col = []
        for row in puzzle:
            col.append(row[i])
        for number in numbers:
            if ( (number in col) == False ):
                return i
    return True

def check_subgrid(puzzle):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, 9):
        subgrid = []
        for j in range(int(i/3)*3, int(i/3)*3+3):
            for k in range((i%3)*3, (i%3)*3+3):
                subgrid.append(puzzle[j][k])
        for number in numbers:
            if ( (number in subgrid) == False ):
                return i
    return True

filename = input("Please enter your sudoku puzzle file: ")
puzzle = load_puzzle(filename)
print_puzzle(puzzle)
check_puzzle(puzzle)