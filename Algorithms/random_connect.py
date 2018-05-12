from Algorithms.Helpers.connect import connect
from Algorithms.Helpers.plots import *
from random import shuffle, choice
import os


def random_connect(grid):
    """This function randomly connects random batteries with random houses.

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


def add_data(score, nbh):
    filename =  os.path.abspath('Results/Solspaces/SS' + nbh +'.csv')
    with open(filename, 'a') as data:
        data.write(str(score) + '\n')


def random_sampler(grid, solutions=1):
    while solutions > 0:
        grid.reset()
        if random_connect(grid):
            if solutions > 1:
                add_data(grid.score(), grid.nbh)
            solutions -= 1
