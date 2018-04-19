from Algorithms.contest import *
from Algorithms.plots import *
from random import shuffle, choice

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
        print("before greedy climber:", grid.score())
        #ex_swapper(grid)
        print("after greedy climber:", grid.score())
        #while hillskipper(grid):
        #    print("after skipper:", grid.score())
        return True
    else:
        return False

def random_sampler(grid, solutions=10):
    scores = {}
    best = (100000000, None) ###infinite###
    while solutions > 0:
        grid.reset()
        if random_connect(grid):
            if grid.score() in scores:
                scores[grid.score()] += 1
            else:
                scores[grid.score()] = 1
            print(solutions, grid.score())
            solutions -= 1
            if grid.score() < best[0]:
                best = (grid.score(), grid)
            print(grid.score())
    line_plot(scores)
    for i in range(10000000):
        i += 1
        i -= 1
    print(best[0])
    hover_plot(best[1])
