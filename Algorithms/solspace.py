from Algorithms.contest import *
from Algorithms.plots import *
from random import shuffle, choice
import os


def random_connect(grid):
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
    while solutions > 0:
        grid.reset()
        if random_connect(grid):
            if solutions > 1:
                add_data(grid.score(), grid.nbh)
            solutions -= 1


def add_data(score, nbh):
    filename =  os.path.abspath('Results/Solspaces/SS' + nbh +'.csv')
    with open(filename, 'a') as data:
        data.write(str(score) + '\n')
