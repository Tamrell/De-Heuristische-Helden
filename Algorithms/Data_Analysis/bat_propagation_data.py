from Algorithms.Helpers.bfcf import all_combos
from Algorithms.Case_B.bat_propagation import start_simulation
import csv
import statistics as stat
from tqdm import tqdm


def bat_propagation_data(grid):
    '''
       saves data for bat_propagation, given a grid.
    '''
    for combo in tqdm(all_combos(grid)):
        results = []
        for test in range(2):
            test_grid = grid.copy()
            results.append(start_simulation(test_grid, 5, list(combo)))
        best = min(results)
        worst = max(results)
        avg = stat.mean(results)
        stdev = stat.stdev(results)
        with open('Results/Solspaces/BP' +
                  str(grid.nbh) + '.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([combo[0:], best, worst, avg, stdev])
