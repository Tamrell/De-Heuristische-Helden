print("Loading modules")
from Classes.grid import Grid
from Classes.battery import *
from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.bat_migration import migration

from Algorithms.Case_A.hill_leaper import hill_leaper
from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber
from Algorithms.Case_A.random_connect import random_sampler
from Algorithms.Case_A.random_battery_cycler import battery_cycler, random_battery_cycler

from Algorithms.Data_Analysis.evaluate_distribution import evaluate_distribution
from Algorithms.Data_Analysis.random_config_saver import start_recording
from Algorithms.Data_Analysis.plots import hover_plot
from Algorithms.Data_Analysis.plotter import custom_plotter, plotter

from Algorithms.Helpers.bounds import lower_bound, upper_bound
from Algorithms.Helpers.bfcf import all_combos
import Algorithms.Helpers.load_data as dt
from Algorithms.Helpers.density import *

from tqdm import tqdm
import sys
import time

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
    """
        The function run_algorithm(alg, grid) calls one of the primary algorithms,
        depending on the parameter alg.
        Takes:
            alg: string representing the algorithm to run
            grid: grid.Grid object to hand to the selected algorithms
        Returns:
            return name of selected algorithm
    """
    algorithms = {#'bb': ['branch & bound', branch_and_bound],
                  'r': ['Random Connect', random_sampler],
                  'b': ['battery cycler', battery_cycler],
                  'e': ['evaluate', evaluate_distribution],
                  'l': ['lower bound', lower_bound],
                  'u': ['upper bound', upper_bound],
                  #'a': ['A-smart', A_smart]
                  }
    return algorithms[alg][1](grid)
    return algorithms[alg][0]

def run():
    results = []
    for i in range(100):
        print(i)
        results.append(run_algorithm('b', grid))
        #greedy_hillclimber(grid)
    return(min(results))

if __name__ == "__main__":

    nbh = get_neighbourhood()
    h_file = 'Data/wijk' + nbh + '_huizen.csv'
    b_file = 'Data/wijk' + nbh + '_batterijen.txt'
    houses = dt.get_houses(h_file)
    batteries = dt.get_batteries(b_file)

    case = input("Which part of the case do you want to run?\n[a/b]: ")
    while case not in ['a', 'b']:
        case = input("only A or B\n[a/b]: ")

    if case == 'a':
        grid = Grid(nbh, houses, batteries)
    else:
        grid = Grid(nbh, houses)

    print("Battery cycling...")
    print(battery_cycler(grid))
    """
    print("K-meansing")
    grid.print_stats("K-means")
    for i in range(100):
        run_algorithm('b', grid)
        print("Iteration", i, grid.score())
        k_means(grid)
        start_simulation(grid, 5, 5)
    grid.print_stats("K-means")
    """

    """
    combos = all_combos(grid)
    # 22779
    combo1 = ((900, 'Imerse-II'), (900, 'Imerse-II'), (900, 'Imerse-II'), (900, 'Imerse-II'), (900, 'Imerse-II'), (1800, 'Imerse-III'), (1800, 'Imerse-III'))
    # 23625
    combo2 = ((450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (1800, 'Imerse-III'))
    # 23130
    combo3 = ((450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (450, 'Powerstar'), (900, 'Imerse-II'), (900, 'Imerse-II'), (900, 'Imerse-II'), (900, 'Imerse-II'))

    migration(grid, combo2)
    random_battery_cycler(grid, 100)
    print(grid)
    grid.print_stats('RBC')
    for bat in grid.batteries.values():
        move_to_middle(grid, bat)
        for h in bat.links:
            h.dists[bat] = grid.distance(h.cord, bat.cord)
    grid.print_stats('Middle')
    print(grid)
    """


###############testing purposes##################

    #start_simulation(grid)

    #print(run())

    #start_simulation(grid)
    exit()

#################################################
    """
    plotter(nbh)

    alg = get_algorithm()
    alg = run_algorithm(alg, grid)
    """
# for testing purposes
