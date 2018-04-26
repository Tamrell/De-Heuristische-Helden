import sys
from Classes.grid import Grid
from Algorithms.hillskipper import hillskipper
from Algorithms.procrastinator import procrastinator
from Algorithms.greedy_hillclimber import greedy_hillclimber
from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import random_battery_cycler
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
    print("\n <key>: <algorithm>\n\n s: Solspace\n p: Procrastinator")
    print(" b: Battery Cycler")
    print(" n: Plot the distribution of the random solution space\n")
    alg = input("(alpha): ")

    if alg == 's':
        print("How many sample solutions do you want to generate?")
        print("(There are currently", count_data(nbh),
              "data points for this neighbourhood)\n")
        solutions = input("(int): ")
        random_sampler(grid, int(solutions))

    elif alg == 'c':
        plotter(nbh)

    elif alg == 'p':
        procrastinator(grid)

    elif alg == 'h':
        hillskipper(grid)

    elif alg == 'b':
        print("How many iterations do you want to run?")
        i = input("(int): ")
        grid = random_battery_cycler(grid, i)

    print('Do you want to print the resulting grid?')
    option = input("y/n\n")
    if option == 'y':
        print(grid)
        grid.print_stats()
