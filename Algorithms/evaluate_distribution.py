from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Results.Solspaces.plotter import custom_plotter

def evaluate_distribution(grid):
    '''multithreading to calculate ~20 random samples and ~20 solutions of The
       battery cycler??
       TO DO:
       - save plot as b_name:cord-b2_name:cord.html
       - change data structure in order to be faster!!!'''
    s1 = []
    s2 = []
    for i in range(100):
        random_sampler(grid)
        s1.append(grid.score())
        grid.reset()
        battery_cycler(grid, False)
        s2.append(grid.score())
        grid.reset()
    custom_plotter(grid, s1, s2)
