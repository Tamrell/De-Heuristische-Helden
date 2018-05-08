import sys
from Classes.grid import Grid
from Algorithms.plots import hover_plot
from Algorithms.hill_leaper import hill_leaper
from Algorithms.evaluate_distribution import evaluate_distribution
from Algorithms.bounds import lower_bound, upper_bound
from Algorithms.Helpers.upper_bound import find_worst
from Algorithms.greedy_hillclimber import greedy_hillclimber
from Algorithms.a_smart import A_smart
from Algorithms.shortest_depth_first import shortest_depthest_first
from Algorithms.stochastic_hillclimber import *
from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Results.Solspaces.plotter import custom_plotter
from Algorithms.branch_and_bound import *

def get_neighbourhood():
    """
        This function selects the neighbourhood to run algorithms for, depending
        on user input.
        Takes:
            None
        Returns:
            The number of the neighbourhood to run the algorithms for.
    """
    legal = {'1', '2', '3'}
    print("\n For which neighbourhood do you want to run an algorithm?")
    nbh = input("\n(int): ")

    # validity checking
    while not nbh in legal:
        print(nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n(int): ")
    return nbh

def get_algorithm():
    """
        This function selects the first algorithm to run, i.e. finding a solution
        to run a secondary algorithm for.
        Takes:
            None
        Returns:
            string: user input resembling the algorithm to run
    """

    print("\n Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n p: Procrastinator")
    print(" lower: Worst (illegal?) Config Finder")
    print(" upper: best (illegal?) Config Finder")
    print(" d: Shortest Depthest First")
    print(" e: evaluator")
    print(" r: Random Connect")
    print(" a: A-smart")
    print(" b: Battery Cycler")
    print(" n: Plot the distribution of the random solution space")
    print(" h: Print Heatmap")
    print(" bb: Branch and bound\n")
    return input("(alpha): ")

def run_algorithm(alg, grid):
    """The function run_algorithm(alg, grid) calls one of the primary algorithms,
        depending on the parameter alg.
        Takes:
            alg: string representing the algorithm to run
            grid: grid.Grid object to hand to the selected algorithms
        Returns:
            return value of selected algorithm
    """
    algorithms = {'s': ['Shortest DF', shortest_depthest_first],
                  'bb': ['branch & bound', branch_and_bound],
                  'r': ['Random Connect', random_sampler],
                  'b': ['battery cycler', battery_cycler],
                  'e': ['evaluate', evaluate_distribution],
                  'l': ['lower bound', lower_bound],
                  'u': ['upper bound', upper_bound],
                  'a': ['A-smart', A_smart]                           }
    algorithms[alg][1](grid)
    return algorithms[alg][0]

def mode():
    print("\n Which mode do you want to enter?")
    print("\n <key>: <mode>\n\n p: plot data\n a: run algorithms")
    print(" d: add data\n")
    return input("(alpha): ")

if __name__ == "__main__":

    nbh = get_neighbourhood()
    file1 = 'Data/wijk' + nbh + '_huizen.csv'
    file2 = 'Data/wijk' + nbh + '_batterijen.txt'
    grid = Grid(file1, file2, nbh)
    alg = get_algorithm()
    alg = run_algorithm(alg, grid)

    if alg == 'n':
        plotter(nbh)
        exit(1)
    print("\n Which iterative algorithm do you want to apply?\n\n")
    print(" Press return for none\n")
    print(" s: Stochastic Hillclimber")
    print(" g: Greedy Hillclimber")
    print(" l: Hill Leaper\n")

    itt = input("(alpha): ")


    if itt == 's':
        itt = 'stochastic climber'
        pre_score = grid.score()
        stochastic_hillclimber(grid)
    elif itt == 'g':
        itt = 'greedy climber'
        pre_score = grid.score()
        greedy_hillclimber(grid)
    elif itt == 'l':
        itt = 'hill leaper'
        pre_score = grid.score()
        hill_leaper(grid)
    else:
        pre_score = False
    if itt:
        grid.print_stats(alg, pre_score, itt)
    else:
        grid.print_stats(alg)
    print('Do you want to save the resulting grid?')
    option = input("y/n\n")
    if option == 'y':
        print(grid)

        grid.print_stats(alg, pre_score)
