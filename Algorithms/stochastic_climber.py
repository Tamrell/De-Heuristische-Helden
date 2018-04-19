# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from house import *
from battery import *
from random import sample, choice

def rand_swapper(grid, limit=50000): ##to aanpas
    legit = False
    checkers = 0
    while not legit and checkers < limit:
        checkers += 1
        #print(checkers)
        [b1, b2] = sample(list(grid.batteries.values()), 2)
        [h1] = sample(set(b1.links), 1)
        [h2] = sample(set(b2.links), 1)
        if b1.max_load >= b1.load - h1.output + h2.output:
            if b2.max_load >= b2.load - h2.output + h1.output:
                if h1.dists[b2] + h2.dists[b1] < h1.dists[b1] + h2.dists[b2]:
                    legit = True
    if checkers >= limit:
        return False
    unconnect(h1)
    unconnect(h2)
    connect(h1, b2)
    connect(h2, b1)
    return True
