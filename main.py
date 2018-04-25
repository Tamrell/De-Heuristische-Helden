import sys
from Classes.grid import Grid
from Algorithms.hillskipper import *
from Algorithms.greedy_hillclimber import *
from Algorithms.solspace import *
from Results.Solspaces.plotter import *

# neighbourhoods used
NBHS = {'1', '2', '3'}

if __name__ == "__main__":

    print("\nfor which neighbourhood do you want to run an algorithm?:")
    nbh = input("\n(int): ")

    while not nbh in NBHS:
        print(nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n(int): ")
    file1 = 'Data/wijk' + nbh + '_huizen.csv'
    file2 = 'Data/wijk' + nbh + '_batterijen.txt'

    grid = Grid(file1, file2, nbh)
    print("Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n")
    print(" p: plot aprox. normal distribution of the solution space\n")
    alg = input("(alpha): ")

    if alg == 's':
        print("How many sample solutions do you want to generate?")
        print("(there are currently", count_data(nbh),
              "data points for this neighbourhood)\n")
        solutions = input("(int): ")
        random_sampler(grid, nbh, int(solutions))

    elif alg == 'p':
        plotter(nbh)

    elif alg == 'h':
        hillskipper(grid)

    print('do you want a visual representation?')
    option = input("y/n")
    if option == 'y':
        print(grid)
