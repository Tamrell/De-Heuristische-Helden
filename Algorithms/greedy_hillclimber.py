from Algorithms.contest import *

def greedy_hillclimber(grid):
    while True:
        swaps = [(swap_cost(h1, h2), h1, h2) for h1 in grid.houses.values()
                 for h2 in grid.houses.values() if swappable(h1, h2)]
        best = min(swaps)
        if best[0] < 0: # <=???
            hard_swap(best[1], best[2])
        else:
            return
