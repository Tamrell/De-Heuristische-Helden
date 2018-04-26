from Algorithms.contest import *
from Algorithms.plots import *

def procrastinate(grid):
    for h in grid.houses.values():
        b = h.find_closest_battery(grid, True)
        connect(h, b, True)

def reluctantly_sort_it_out(grid):
    # for all connections, connect the one with the least cost that causes the
    # deficiency score to go down until the grid is legal.
    while not grid.legal():
        best_fit(grid)
        print(defficiency_score(grid))

def best_fit(grid):
    best = (0, None, None)
    for h1 in grid.houses.values():
        for h2 in grid.houses.values():
            if h1 != h2 and h1.bat != h2.bat:
                if deff_diff(h1, h2) < best[0]:
                    print('cur_', best[0])
                    best = (deff_diff(h1, h2), h1, h2)
    if best[1] and best[2]:
        if hard_swap(best[1], best[2], True):
            print('swapping!')


def least_worsening(grid):
    #### to be finished
    best = (0, None, None)
    for h1 in grid.houses.values():
        for h2 in grid.houses.values():
            if h1 != h2:
                pass


def deff_diff(h1, h2):
    pre_deff = abs((h1.bat.load - h1.bat.max_load) +
                   (h2.bat.load - h2.bat.max_load))#**2?

    post_deff = abs((h1.bat.load - h1.output + h2.output) - h1.bat.max_load) +\
                abs((h2.bat.load - h2.output + h1.output) - h2.bat.max_load)
    return pre_deff - post_deff


def defficiency_score(grid):
    # calculates how inefficient all the batteries are used.
    deff = 0
    for b in grid.batteries.values():
        deff += abs(b.max_load - b.load)
    return deff

def procrastinator(grid):
    procrastinate(grid)
    reluctantly_sort_it_out(grid)
    print(grid, 'Done!')
