print("Loading modules")
from Classes.grid import Grid
from Classes.battery import *

import Algorithms.Data_Analysis.plots as pts
from Algorithms.Data_Analysis.k_data import k_data
from Algorithms.Data_Analysis.plotter import custom_plotter, plotter

from Algorithms.Helpers.bfcf import all_combos
import Algorithms.Helpers.load_data as dt

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
    nbh = input(" (int): ")

    # validity checking
    while not nbh in legal:
        print(" ", nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n (int): ")
    return nbh

def run():
    results = []
    for i in range(100):
        print(i)
        results.append(run_algorithm('b', grid))
    return(min(results))

if __name__ == "__main__":

    nbh = dt.get_neighbourhood()
    h_file = 'Data/wijk' + nbh + '_huizen.csv'
    b_file = 'Data/wijk' + nbh + '_batterijen.txt'
    houses = dt.get_houses(h_file)
    batteries = dt.get_batteries(b_file)

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
