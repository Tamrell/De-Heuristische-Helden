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
        #print("before greedy climber:", grid.score())
        #ex_swapper(grid)
        #print("after greedy climber:", grid.score())
        #while hillskipper(grid):
        #    print("after skipper:", grid.score())
        return True
    else:
        return False

def random_sampler(grid, nbh, solutions=10):
    best = (float('inf'), None)
    while solutions > 0:
        grid = grid.reset()
        if random_connect(grid):
            add_data(grid.score(), nbh)
            solutions -= 1
            if grid.score() < best[0]:
                best = (grid.score(), grid)
    print(best[1])
    print(best[0])
    hover_plot(best[1])

def add_data(score, nbh):
    filename =  os.path.abspath('Results/Solspaces/SS' + nbh +'.csv')
    with open(filename, 'a') as data:
        data.write(str(score) + '\n')
