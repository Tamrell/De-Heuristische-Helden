import sys
from Classes.grid import Grid
from Algorithms.hillskipper import *
from Algorithms.greedy_hillclimber import *
from Algorithms.solspace import *

if __name__ == "__main__":

    file1 = sys.argv[1]
    if file1 == '1':
        file1 = 'Data/wijk1_huizen.csv'
    elif file1 == '2':
        file1 = 'Data/wijk2_huizen.csv'
    elif file1 == '3':
        file1 = 'Data/wijk3_huizen.csv'

    file2 = sys.argv[1]
    if file2 == '1':
        file2 = 'Data/wijk1_batterijen.txt'
    elif file2 == '2':
        file2 = 'Data/wijk2_batterijen.txt'
    elif file2 == '3':
        file2 = 'Data/wijk3_batterijen.txt'

    grid = Grid(file1, file2, sys.argv[1])
    solutions = input("How many sample solutions do you want to generate? (int)\n")
    random_sampler(grid, sys.argv[1], solutions)
    print(grid)
