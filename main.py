import sys
from Classes.grid import Grid
from Algorithms.Helpers.plots import hover_plot
from Algorithms.hill_leaper import hill_leaper
from Algorithms.evaluate_distribution import evaluate_distribution
from Algorithms.Helpers.bounds import lower_bound, upper_bound
from Algorithms.greedy_hillclimber import greedy_hillclimber
from Algorithms.a_smart import A_smart
from Algorithms.random_connect import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Algorithms.Helpers.plotter import custom_plotter
from Algorithms.Helpers.plotter import plotter
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
            return name of selected algorithm
    """
    algorithms = {'bb': ['branch & bound', branch_and_bound],
                  'r': ['Random Connect', random_sampler],
                  'b': ['battery cycler', battery_cycler],
                  'e': ['evaluate', evaluate_distribution],
                  'l': ['lower bound', lower_bound],
                  'u': ['upper bound', upper_bound],
                  'a': ['A-smart', A_smart]                           }
    algorithms[alg][1](grid)
    return algorithms[alg][0]

def mode():
    """
    This function returns the mode in which the algorithm must run
    Takes:
        None
    Returns:
        String representing a running mode
    """
    print("\n Which mode do you want to enter?")
    print("\n <key>: <mode>\n\n p: plot data\n a: run algorithms")
    print(" d: add data\n")
    return input("(alpha): ")

if __name__ == "__main__":

    nbh = get_neighbourhood()
    file1 = 'Data/wijk' + nbh + '_huizen.csv'
    file2 = 'Data/wijk' + nbh + '_batterijen.txt'
    grid = Grid(file1, file2, nbh)
    ########################
    plotter(nbh)
    exit(1)
    ##########################


    alg = get_algorithm()
    alg = run_algorithm(alg, grid)
    grid.print_stats(alg)
