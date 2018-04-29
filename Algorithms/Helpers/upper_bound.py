from Algorithms.contest import *
from Algorithms.plots import *

def raise_hell(grid):
    for h in grid.houses.values():
        b = h.find_furthest_battery(grid)
        connect(h, b, True)

def find_worst(grid):
    raise_hell(grid)
    grid.print_stats()
    print(grid, 'Done!')
