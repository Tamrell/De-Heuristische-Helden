import sys
from Classes.grid import Grid
from Algorithms.hillskipper import *
from Algorithms.greedy_hillclimber import *
from Algorithms.solspace import *
from Results.Solspaces.plotter import *

if __name__ == "__main__":

    print("\nfor which neighbourhood do you want to run an algorithm?:")
    nbh = input("\n(int): ")

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
    alg = input("(alpha): ")
    if alg == 's':
        print("How many sample solutions do you want to generate?")
        print("(there are currently", count_data(nbh),
              "data points for this neighbourhood)\n")
        solutions = input("(int): ")
        random_sampler(grid, fil, int(solutions))
    elif alg == 'n':
        plotter(nbh)
    #print(grid)
