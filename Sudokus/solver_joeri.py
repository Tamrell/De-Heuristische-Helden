import numpy as np
import time
import csv

"""

7 9 0 | 0 0 0 | 3 0 1
0 0 0 | 0 0 6 | 9 0 0
8 0 0 | 0 3 0 | 0 7 6
---------------------
0 0 0 | 0 0 5 | 0 0 2
0 0 5 | 4 1 8 | 7 0 0
4 0 0 | 7 0 0 | 0 0 0
---------------------
6 1 0 | 0 9 0 | 0 0 8
0 0 2 | 3 0 0 | 0 0 0
0 0 9 | 0 0 0 | 0 5 4

"""

sudoku1 = np.loadtxt(open("puzzle1.sudoku"), delimiter=",")
sudoku2 = np.loadtxt(open("puzzle2.sudoku"), delimiter=",")
sudoku3 = np.loadtxt(open("puzzle3.sudoku"), delimiter=",")
sudoku4 = np.loadtxt(open("puzzle4.sudoku"), delimiter=",")
sudoku5 = np.loadtxt(open("puzzle5.sudoku"), delimiter=",")
sudoku6 = np.loadtxt(open("puzzle6.sudoku"), delimiter=",")


#=================================================================================================

def not_in_row (sudoku, row_number):
	return [x for x in range(1, 10) if x not in sudoku[row_number]]

#=================================================================================================

def not_in_col (sudoku, col_number):
	return [x for x in range(1, 10) if x not in sudoku[0:9, col_number]]

#=================================================================================================

def not_in_quad (sudoku, col_number, row_number):
	start_col = col_number - (col_number % 3)
	start_row = row_number - (row_number % 3)

	end_col = start_col + 3
	end_row = start_row + 3

	return [x for x in range(1, 10) if x not in sudoku[start_row:end_row, start_col:end_col]]

#=================================================================================================

def options (sudoku, col_number, row_number):
	merge_1 = [x for x in not_in_row(sudoku, row_number) if x in not_in_col(sudoku, col_number)]
	return [x for x in merge_1 if x in not_in_quad(sudoku, col_number, row_number)]

#=================================================================================================

def find_first_empty_spot (sudoku):
    for row in range(9):
        for col in range(9):
            if(sudoku[row][col] == 0):
            	return [row, col]
    return False

#==================================================================================================

def solve(sudoku):

	if(not find_first_empty_spot(sudoku)):
		# print(sudoku, "\n\n")
		return True, sudoku

	free_spot = find_first_empty_spot(sudoku)
	row = free_spot[0]
	col = free_spot[1]

	for option in options(sudoku, free_spot[1], free_spot[0]):
		sudoku[free_spot[0]][free_spot[1]] = option

		if solve(sudoku):
			return True

		sudoku[row][col] = 0

	return False


#==================================================================================================

start_time = time.time()
solve(sudoku1)
print(time.time() - start_time, "\n")
start_time = time.time()
solve(sudoku2)
print(time.time() - start_time, "\n")
start_time = time.time()
solve(sudoku3)
print(time.time() - start_time, "\n")
start_time = time.time()
solve(sudoku4)
print(time.time() - start_time, "\n")
start_time = time.time()
solve(sudoku5)
print(time.time() - start_time, "\n")
start_time = time.time()
solve(sudoku6)
print(time.time() - start_time, "\n")
