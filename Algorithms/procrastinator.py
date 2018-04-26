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
        #best_fit(grid)
        best_score(grid)
        print(grid)
        print(defficiency_score(grid))
        input(grid.print_stats())

def best_fit(grid):
    best = (0, None, None)
    for h in grid.houses.values():
        for b in [b for b in grid.batteries.values() if b.load > b.max_load]:
            if deff_diff(h, b) > best[0]:
                best = (deff_diff(h, b), h, b)
    if best[1]:
        unconnect(best[1])
        connect(best[1], best[2], True)


def best_score(grid):
    best = (None, None, None)
    for h in grid.houses.values():
        for b in grid.batteries.values():
            if deff_diff(h, b) > 0:
                if not best[0] or dist_diff(h, b) > best[0]:
                    best = (dist_diff(h, b), h, b)
    if best[1]:
        unconnect(best[1])
        connect(best[1], best[2], True)

def deff_diff(h, b):
    pre_deff = abs(h.bat.load - h.bat.max_load) + abs(b.load - b.max_load)
    post_deff = abs(h.bat.load - h.output - h.bat.max_load) + \
                abs(b.load + h.output - b.max_load)
    return pre_deff - post_deff

def dist_diff(h, b):
    return h.dists[h.bat] - h.dists[b]

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
