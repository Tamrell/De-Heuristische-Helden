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
        print(grid)

def best_fit(grid):
    best = (0, None, None)
    for h1 in grid.houses.values():
        for h2 in grid.houses.values():
            if h1 != h2 and h1.bat != h2.bat:
                if deff_diff(h1, h2) > best[0]:
                    best = (deff_diff(h1, h2), h1, h2)
    if best[1] = print('swapping!')
    hard_swap(h1, h2, True)


def least_worsening(grid):
    #### to be finished
    best = (0, None, None)
    for h1 in grid.houses():
        for h2 in grid.houses():
            if h1 != h2:
                pass


def deff_diff(h1, h2):
    deff1 = abs(h1.bat.load - h1.bat.max_load)#**2?
    deff2 = abs((h1.bat.load - h1.output + h2.output) -
                (h2.bat.load - h2.output + h1.output))
    return deff1 - deff2


def defficiency_score(grid):
    # calculates how inefficient all the batteries are used.
    deff = 0
    for b in grid.values():
        deff += abs(b.max_load - b.load)
    return deff

def procrastinator(grid):
    procrastinate(grid)
    reluctantly_sort_it_out(grid)
    print(grid, 'Done!')

if __name__ == "__main__":
    b_count = 0
    for b in grid.batteries.values():
        b_count += b.max_load
        print(b.color, ":", b.load, "of", b.max_load)
    count = 0
    h_count = 0
    for h in grid.houses.values():
        count += h.output
        h_count += 1
    print(grid.score())
    print("total houses:", h_count)
    print("total output:", count)
    print("average output:", count/h_count)
    print("total capacity:", b_count)
