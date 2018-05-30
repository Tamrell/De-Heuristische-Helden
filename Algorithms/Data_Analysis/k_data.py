from Algorithms.Helpers.bfcf import all_combos
from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_A.random_battery_cycler import battery_cycler
from Algorithms.Case_B.random_bat_config import random_bat_config
import csv
import statistics as stat
from tqdm import tqdm


def k_data(grid):
    '''
       Multithreading to calculate ~20 random samples and ~20 solutions of The
       battery cycler??
       TO DO:
       - multithreading??
       - change data structure in order to be faster!!!
    '''
    for combo in tqdm(all_combos(grid)):
        results = []
        for test in range(10):
            test_grid = grid.copy()
            random_bat_config(test_grid, list(combo))
            k_means(test_grid)
            results.append(battery_cycler(test_grid))
        best = min(results)
        worst = max(results)
        avg = stat.mean(results)
        stdev = stat.stdev(results)
        with open('Results/Solspaces/K_means' + str(grid.nbh) + '.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([combo[0:], best, worst, avg, stdev])
