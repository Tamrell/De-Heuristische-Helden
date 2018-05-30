from Algorithms.Helpers.connect import connect
from random import shuffle, choice
import os


def random_connect(grid):
    """
        This function randomly connects random batteries with random houses.

        Takes
            Grid: grid object containing the houses and batteries

        Returns
            Bool: True if the solution is legal, else False
    """
    houses = [h for h in grid.houses.values() if h.free]
    shuffle(houses)
    for h in houses:
        bats = [b for b in h.dists if b.fits(h.output)]
        if bats:
            connect(h, choice(bats))
        else:
            return False
    if grid.legal():
        return True
    else:
        return False


def random_sampler(grid, solutions=1):
    """
        This function runs random connect until there have been solutions
        solutions found.

        Takes
            Grid: grid object containing the houses and batteries
            (optional)int: number of solutions needed

        Returns
            None
    """
    while solutions > 0:
        grid.reset()
        if random_connect(grid):
            solutions -= 1
