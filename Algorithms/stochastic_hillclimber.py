from Algorithms.contest import *
from random import choice

def stochastic_hillclimber(grid):
    while True:
        swaps = [(h1, h2) for h1 in grid.houses.values()
                 for h2 in grid.houses.values() if swappable(h1, h2) and
                 swap_cost(h1, h2) < 0] # <=???
        if swaps:
            swap = choice(swaps)
            hard_swap(swap[0], swap[1])
        else:
            return
