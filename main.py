from Classes.grid import Grid

from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.bat_propagation import start_simulation
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.bat_migration import migration

import Algorithms.Data_Analysis.plots as pts
from Algorithms.Data_Analysis.k_data import k_data
from Algorithms.Data_Analysis.plotter import custom_plotter, plotter

from Algorithms.Helpers.bfcf import all_combos
import Algorithms.Helpers.load_data as dt

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
    houses = dt.get_houses('Data/wijk' + nbh + '_huizen.csv')
    batteries = dt.get_batteries('Data/wijk' + nbh + '_batterijen.txt')

    case = input(" Which part of the case do you want to run?\n [a/b]: ")
    while case not in ['a', 'b']:
        case = input(" Only A or B\n [a/b]: ")

    if case == 'a':
        grid = Grid(nbh, houses, batteries)
    else:
        grid = Grid(nbh, houses)

    alg = dt.get_algorithm(case)
    dt.run_algorithm(alg, grid)
    pts.plot(grid)
