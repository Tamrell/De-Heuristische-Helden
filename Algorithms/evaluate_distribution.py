from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Results.Solspaces.plotter import custom_plotter
import threading as th
import time


def evaluate_distribution(grid):
    '''multithreading to calculate ~20 random samples and ~20 solutions of The
       battery cycler??
       TO DO:
       - multithreading??
       - save plot as score-b_name:cord-b2_name:cord.html
       - change data structure in order to be faster!!!'''
    s1 = []
    s2 = []
    t = time.time()
    for i in range(20): #10? 20? 50?
        random_sampler(grid)
        s1.append(grid.score())
        grid.reset()
        battery_cycler(grid, False)
        s2.append(grid.score())
        grid.reset()
    custom_plotter(grid, s1, s2)
    print('took', time.time() - t, 'seconds.')
