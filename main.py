import sys
from Classes.grid import Grid
from Algorithms.hillskipper import *
from Algorithms.greedy_hillclimber import *
from Algorithms.solspace import *
from Results.Solspaces.plotter import plotter

if __name__ == "__main__":

    nbh = input("for which neighbourhood do you want to run an algorithm?: (int) ")

    file1 = nbh
    if file1 == '1':
        file1 = 'Data/wijk1_huizen.csv'
    elif file1 == '2':
        file1 = 'Data/wijk2_huizen.csv'
    elif file1 == '3':
        file1 = 'Data/wijk3_huizen.csv'

    file2 = nbh
    if file2 == '1':
        file2 = 'Data/wijk1_batterijen.txt'
    elif file2 == '2':
        file2 = 'Data/wijk2_batterijen.txt'
    elif file2 == '3':
        file2 = 'Data/wijk3_batterijen.txt'

    grid = Grid(file1, file2, nbh)
    print("Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n")
    print(" n: plot aprox. normal distribution of the solution space\n")
    alg = input()
    if alg == 's':
        solutions = input("How many sample solutions do you want to generate? (int)\n")
        random_sampler(grid, fil, int(solutions))
    elif alg == 'n':
        plotter(nbh)
    #print(grid)
