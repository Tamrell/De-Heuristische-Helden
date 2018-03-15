# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden

import csv
import copy
import time

# start time
time0 = time.time()

sudokufile = open("puzzle6.sudoku")

sudoku = {}
empty_spaces = []

# load sudoku into dictionary
y = 0
for line in csv.reader(sudokufile):
    x = 0
    for element in line:
        # space is not filled in
        if element == "0":
            empty_spaces.append((x, y))
        else:
        # space is filled in
            sudoku[x, y] = int(element)
        x += 1
    y += 1

def find_base(n):
    """function returns the upper left coördinates of 9-space blocks"""
    if n < 3:
        return 0
    elif n < 6:
        return 3
    else:
        return 6

def possibilities(in_sudoku, empty_space):
    """function returns a list of numbers available to a give space"""

    array = [i for i in range(1, 10)]
    x, y = empty_space

    # remove all numbers already in line
    for x_ in range(9):
        try:
            array.remove(in_sudoku[x_, y])
        except (ValueError, KeyError):
            pass

    # remove all numbers already in column
    for y_ in range(9):
        try:
            array.remove(in_sudoku[x, y_])
        except (ValueError, KeyError):
            pass

    # remove all numbers already in 9-space square block
    x_base, y_base = find_base(x), find_base(y)
    for x_ in range(3):
        for y_ in range(3):
            try:
                array.remove(in_sudoku[x_ + x_base, y_ + y_base])
            except (ValueError, KeyError):
                pass

    return array

def show(sudoku):
    """function for showing the sudoku"""
    grid = []

    # add every line to grid
    for y in range(9):
        line = ""
        for x in range(9):
            try:
                line += str(sudoku[x, y])
            except:
                line += "0"
        grid.append(line)

    # print all lines
    for line in grid:
        print(line)

def best_empty_space(in_sudoku, in_empty_spaces):
    """given the sudoku as it is, this function finds the empty space related
    to fewest other empty spaces"""

    best_place = 0
    best_score = 0

    # find number of filled in places for every empte space
    for empty_space in in_empty_spaces:
        array = []
        x, y = empty_space

        # append all numbers already in the row
        for x_ in range(9):
            try:
                array.append(in_sudoku[x_,y])
            except KeyError:
                pass

        # append all numbers already in the column
        for y_ in range(9):
            try:
                array.append(in_sudoku[x, y_])
            except KeyError:
                pass

        score = len(array)

        # compare present empty_space with best one
        if score > best_score:
            best_score = score
            best_place = empty_space

    return best_place

def evaluate(in_sudoku, in_empty_spaces):
    """this function recursively solves the sudoku"""

    # make copy of parameter scenario
    sudoku = copy.copy(in_sudoku)
    empty_spaces = copy.copy(in_empty_spaces)

    # if sudoku is solved
    if empty_spaces == []:
        show(sudoku)
        print(time.time() - time0)
        return True

    # get empty space in sudoku dependend of fewest other empty spaces
    target = best_empty_space(sudoku, empty_spaces)
    empty_spaces.remove(target)

    # evaluate sudoku with empty space filled in
    OK = False
    possible_sudokus = possibilities(sudoku, target)
    for i in possible_sudokus:
        sudoku[target] = i
        if evaluate(sudoku, empty_spaces):
            OK = True
    return OK

evaluate(sudoku, empty_spaces)
