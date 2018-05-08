from Algorithms.contest import *
from Algorithms.plots import *

def get_bound(grid, lower=True):
    for h in grid.houses.values():
        if lower:
            b = h.find_closest_battery(grid, True)
        else:
            b = h.find_furthest_battery(grid)
        connect(h, b, True)

def upper_bound(grid):
    return get_bound(grid, False)

def lower_bound(grid):
    return get_bound(grid)
