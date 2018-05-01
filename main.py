import sys
from Classes.grid import Grid
from Algorithms.hillskipper import hillskipper
from Algorithms.procrastinator import procrastinator
from Algorithms.Helpers.upper_bound import find_worst
from Algorithms.greedy_hillclimber import *
from Algorithms.stochastic_hillclimber import *
from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import *
from Results.Solspaces.plotter import *

# neighbourhoods used
NBHS = {'1', '2', '3'}

if __name__ == "__main__":

    print("\n For which neighbourhood do you want to run an algorithm?")
    nbh = input("\n(int): ")

    while not nbh in NBHS:
        print(nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n(int): ")

    file1 = 'Data/wijk' + nbh + '_huizen.csv'
    file2 = 'Data/wijk' + nbh + '_batterijen.txt'
    grid = Grid(file1, file2, nbh)

    print("\n Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n p: Procrastinator")
    print(" w: Worst (illegal) Config Finder")
    print(" r: Random Connect")
    print(" b: Battery Cycler")
    print(" n: Plot the distribution of the random solution space")
    print(" h: Print Heatmap\n")

    alg = input("(alpha): ")

    print("\n Which iterative algorithm do you want to apply?\n")
    print(" Press return for none\n")
    print(" s: Stochastic Hillclimber")
    print(" g: Greedy Hillclimber")
    print(" l: Greedy Hilll Leaper")
    print(" gl: Greedy Hill Climber + Greedy Hilll Leaper\n")

    itt = input("(alpha): ")

    if alg == 's':
        print("How many sample solutions do you want to generate?")
        print("(There are currently", count_data(nbh),
              "data points for this neighbourhood)\n")
        solutions = input("(int): ")
        random_sampler(grid, int(solutions))

    elif alg == 'r':
        random_sampler(grid)

    elif alg == 'w':
        find_worst(grid)

    elif alg == 'n':
        plotter(nbh)

    elif alg == 'p':
        procrastinator(grid)

    elif alg == 'b':
        print("Press 'f' for fully random, 's' for semi-random")
        rd = input("'s'/'f'\n")
        print("How many iterations do you want to run?")
        i = input("(int): ")
        if rd == 's':
            grid = semi_random_battery_cycler(grid, i)
        elif rd == 'f':
            grid = random_battery_cycler(grid, i)

    elif alg == 'h':
        print(" Press 'g' for global, 'r' for relative")
        rd = input(" 'g'/'r'\n")
        if rd == 'g':
            grid.print_heatmap(0)
        elif rd == 'r':
            grid.print_heatmap(1)

    if itt == 's':
        pre_score = grid.score()
        stochastic_hillclimber(grid)
    elif itt == 'g':
        pre_score = grid.score()
        greedy_hillclimber(grid)
    elif itt == 'l':
        pre_score = grid.score()
        hillskipper(grid)
    elif itt == 'gl':
        pre_score = grid.score()
        greedy_hillclimber(grid)
        print("score after greedy_hillclimber:", grid.score())
        hillskipper(grid)
    else:
        pre_score = False

    print('Do you want to print the resulting grid?')
    option = input("y/n\n")
    if option == 'y':
        print(grid)
        grid.print_stats(pre_score)
