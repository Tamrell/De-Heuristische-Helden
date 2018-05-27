from Algorithms.Helpers.connect import hard_swap
from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber

def leap(grid):
    '''Hill leaper goes 2 levels deep in order to escape local optima'''
    houses = [h for h in grid.houses.values()]
    best = grid.score()
    for h1 in houses:
        for h2 in houses:
            if hard_swap(h1, h2):
                for h3 in [h1, h2]: # in houses necessary?
                    for h4 in houses:
                        if hard_swap(h3, h4):
                            if grid.score() < best:
                                return True
                            hard_swap(h3, h4)
                hard_swap(h1, h2)
    else:
        return False

def hill_leaper(grid):
    greedy_hillclimber(grid)
    while leap(grid):
        greedy_hillclimber(grid)
