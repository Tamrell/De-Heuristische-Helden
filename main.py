from Classes.grid import Grid

from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.bat_propagation import start_simulation
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.bat_migration import migration

import Algorithms.Data_Analysis.plots as pts
from Algorithms.Data_Analysis.plotter import custom_plotter, plotter

import Algorithms.Helpers.load_data as dt
from Algorithms.Helpers.density import move_to_middle


if __name__ == "__main__":

    nbh = dt.get_neighbourhood()
    houses = dt.get_houses('Data/wijk' + nbh + '_huizen.csv')
    batteries = dt.get_batteries('Data/wijk' + nbh + '_batterijen.txt')
    print(" Which part of the case do you want to run?\n - a:",
          "connecting houses and batteries\n - b: placing batteries\n")
    case = input("[a/b]: ")
    while case not in ['a', 'b']:
        case = input(" Only a or b\n [a/b]: ")

    if case == 'a':
        grid = Grid(nbh, houses, batteries)
    else:
        grid = Grid(nbh, houses)

    alg = dt.get_algorithm(case)
    dt.run_algorithm(alg, grid)
    if case is 'b':
        print(" Move batteries to optimal position for their links?")
        move = input(' [y/n]: ')
        if move is 'y':
            for bat in grid.batteries.values():
                move_to_middle(grid, bat)
    grid.print_stats()
    pts.plot(grid)
