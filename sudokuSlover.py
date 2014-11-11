__author__ = 'student'
import math

def enterpuzzle(puzzle):
    while True:
        # puzzle = raw_input('please enter your 81 digit puzzle use "." for blank spots :\n')
        #Validate that user input is len = 81
        if not len(puzzle) == 81:
            print ("please enter a value that is equal to 81 charactors long. Please try again")
            continue
        #Validate that user input only has numbers or .
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        for char in puzzle:
            if not char in valid:
                print (char + " is not a valid value please reenter puzzle without using " + char)
        break
def display(puzzle):
    display = ''
    ii = 0
    for char in puzzle:
        # format first line
        if ii % 81 == 0:
            display = "+---+---+---+\n|" + char
        # format rows
        elif ii % 27 == 0:
            display = display + "|\n+---+---+---+\n|" + char
        # format last column
        elif ii % 9 == 0:
            display = display + "|\n|" + char
        # format columns
        elif ii % 3 == 0:
            display = display + "|" + char
        # insert nonformated data
        else:
            display = display + char
        ii += 1


    display = display + "|\n+---+---+---+"

    print display
def find_row(numbervalue):
    row = numbervalue/9
    row = math.floor(row)
    row = int(row)
    return row
    # given any position in the puzzle this will return the row
def find_column(numbervalue):
    column = numbervalue % 9
    column = int(column)
    return column
    return
    # given any position in the puzzle this will return the column
def find_box(numbervalue):
    # finds the box that a given cell belongs to e.g. start with upper left 0
    row = find_row(numbervalue)
    row = row / 3
    row = math.floor(row)

    column = find_column(numbervalue)
    column = column / 3
    column = math.floor(column)

    box_number = column + row * 3
    box_number = int(box_number)
    return box_number
    # given any position in the puzzle this will return the boxNumber
def cell_current_properties():
    return
def check_for_available_values(cell_index):
    return
def get_all_indexs_for_row(row):
    indexs = []
    for x in range(0,9):
        next_index = x + 9 * row
        indexs.append(next_index)
    return indexs
def get_all_indexs_for_column(column):
    """
    given any index in the puzzle this returns a list of indexs in that column
    :param column: column number
    :return: indexs[]
    """
    indexs = []
    for x in range(0,9):
        next_index = x * 9 + column
        indexs.append(next_index)
    return indexs
def get_all_indexs_for_box(box):
    """
    given any index in the puzzle this returns a list of indexs in that box
    :param box: box number
    :return: indexs[]
    """
    row = box / 3
    row = int(math.floor(row))
    row = row * 27

    column = box % 3
    column = int(math.floor(column))
    column = column * 3
    indexs = []
    for x in range(0,3):
        for y in range(0,3):
            next_index = x * 9 + y + column + row
            indexs.append(next_index)
    return indexs


def get_possable_locations_for_number(unsloved_list, puzzle, value):
    possable_locations = []
    for cell in unsloved_list:
        active_row = find_row(cell)
        active_row_indexs = get_all_indexs_for_row(active_row)
        get_number_values(active_row_indexs,puzzle)
        if value in unsloved_list:


            print active_row, active_row_indexs, cell




        #active_column = find_column(cell)
        #active_box = find_box(cell)


    return
def get_unsloved_cells(puzzle):
    unsloved =[]
    ii = 0
    for char in puzzle:
       if char == ".":
           unsloved.append(ii)
       ii += 1
    #returns unsloved index
    return unsloved
def get_number_values(cell_index_list,puzzle):
    values = []
    for index in cell_index_list:
        if not puzzle[index] == ".":
            value = puzzle[index]
            values.append(value)
    return values




puzzle = '.94...1...............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8'
enterpuzzle(puzzle)
unsloved = get_unsloved_cells(puzzle)
#display(puzzle)
#get_possable_locations_for_number(unsloved,puzzle,1)
row1 = get_all_indexs_for_row(0)
test = get_number_values(row1,puzzle)
print test