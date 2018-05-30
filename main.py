print("Loading modules")
from Classes.grid import Grid
from Classes.battery import *
from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.bat_migration import migration

from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber
from Algorithms.Case_A.random_connect import random_sampler
from Algorithms.Case_A.random_battery_cycler import battery_cycler, random_battery_cycler

from Algorithms.Data_Analysis.evaluate_distribution import evaluate_distribution
from Algorithms.Data_Analysis.random_config_saver import start_recording
from Algorithms.Data_Analysis.plots import hover_plot
from Algorithms.Data_Analysis.k_data import k_data
from Algorithms.Data_Analysis.plotter import custom_plotter, plotter

from Algorithms.Helpers.bounds import lower_bound, upper_bound
from Algorithms.Helpers.bfcf import all_combos
import Algorithms.Helpers.load_data as dt
from Algorithms.Helpers.density_reset import *

from tqdm import tqdm
import sys
import time

def run():
    results = []
    for i in range(100):
        print(i)
        results.append(run_algorithm('b', grid))
        #greedy_hillclimber(grid)
    return(min(results))

if __name__ == "__main__":

    nbh = dt.get_neighbourhood()
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


###############testing purposes##################
    k_data(grid)
    #start_simulation(grid)
    exit()

#################################################
    """
    plotter(nbh)

    alg = get_algorithm()
    alg = run_algorithm(alg, grid)
    """
# for testing purposes
