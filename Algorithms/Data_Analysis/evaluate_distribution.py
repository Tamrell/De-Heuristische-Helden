from Algorithms.Case_A.random_connect import random_sampler
from Algorithms.Case_A.random_battery_cycler import battery_cycler
from Algorithms.Data_Analysis.plotter import custom_plotter
from tqdm import tqdm


def evaluate_distribution(grid):
    '''
       Multithreading to calculate ~20 random samples and ~20 solutions of The
       battery cycler??
       TO DO:
       - multithreading??
       - change data structure in order to be faster!!!
    '''
    random_samples = []
    battery_cycler_samples = []
    tqdm.monitor_interval = 0
    for i in tqdm(range(100)): #10? 20? 50?
        grid.reset()
        random_sampler(grid)
        random_samples.append(grid.score())
        grid.reset()
        battery_cycler(grid, False)
        battery_cycler_samples.append(grid.score())
        grid.reset()
    print(grid)
    custom_plotter(grid, random_samples, battery_cycler_samples)
