from Algorithms.Helpers.connect import hard_swap, swappable, swap_cost


def greedy_hillclimber(grid):
    '''
       Calculates which swaps decrease total cost, then picks the swap which
       leads to the biggest decrease and makes the swap. Repeats the process
       until there are no benefitting swaps left.
    '''
    while True:
        swaps = [(swap_cost(h1, h2), h1, h2) for h1 in grid.houses.values()
                 for h2 in grid.houses.values() if swappable(h1, h2)]
        best = min(swaps)
        if best[0] < 0:
            hard_swap(best[1], best[2])
        else:
            return grid.score()
