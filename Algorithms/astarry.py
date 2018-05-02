from Algorithms.contest import *
from copy import deepcopy
import queue as Q


# only expands the current cheapest grid, uses PriorityQueue, will find cheapest??
# should probably also check the remaining options when it found the first answer in that grid

# how to prevent morphologically identical grids?


# slow as hell, should try dict: house:(bat, dist)
# needs different data structure

class Route:
    def __init__(self, grid):
        # only coordinate tuples
        # for all moves, use 1 grid to check/calculate
        self.moves = set()
        self.bats = {b.cord: [0, b.max_load] for b in grid.batteries.values()} # available?
        self.houses = {(h.cord, h.output) for h in grid.houses.values()}
        self.cost = 0
        self.estimate = 0

    def __lt__(self, other):
        return True

def fits_light(h, binf):
    if binf[0] + h[1] > binf[1]:
        return False
    else:
        return True

def move(route, grid, h, b, visited):
    copy = deepcopy(route)
    copy.houses.remove(h)
    copy.bats[b][0] += h[1]
    copy.moves.add((h[0], b))
    copy.cost += grid.houses[(int(h[0][0]), int(h[0][1]))].dists[grid.batteries[b]]
    copy.estimated_cost = estimate_cost(copy, grid)
    visited.add(tuple(copy.moves))
    return copy

def estimate_cost(route, grid):
    estimate = 0
    for h in route.houses:
        estimate += min([d for b, d in grid.houses[(int(h[0][0]), int(h[0][1]))].dists.items() \
        if fits_light(h, route.bats[b.cord])])
    return estimate

def A_smart(grid): #A-smartGrid!!!!! ha!
    start = Route(grid)
    visited = set()
    filtered = 0
    it = 0
    pq = Q.PriorityQueue()
    pq.put((start.cost, start))
    while len(pq.queue[0][1].moves) < 150:
        astepper(pq.get()[1], visited, pq, grid, filtered)
        it += 1
        if it % 1000 == 0:
            print('--------')
            print(len(pq.queue[0][1].moves), pq.queue[0][1].cost, pq.qsize())
    best = pq.get()
    for pair in best.moves:
        connect(grid.houses[pair[0]], grid.batteries[pair[1]])

def astepper(route, visited, pq, grid, f):
    for h in route.houses:
        b = min([(d, b) for b, d in grid.houses[(int(h[0][0]), int(h[0][1]))].dists.items()
                 if fits_light(h, route.bats[b.cord])])[1].cord
        if b:
            if not tuple(route.moves | {(h, b)}) in visited:
                new = move(route, grid, h, b, visited)
                pq.put((new.cost + new.estimated_cost, new))
            else:
                f += 1
                print('filtered:', f)

# def astepper(route, visited, pq, grid, f):
#     for h in route.houses:
#         for b in route.bats:
#             if not tuple(route.moves | {(h, b)}) in visited:
#                 if fits_light(h, route.bats[b]):
#                     new = move(route, grid, h, b, visited)
#                     pq.put((new.cost + new.estimated_cost, new))
#             else:
#                 f += 1
#                 print('filtered:', f)

def astarry(grid):
    pq = Q.PriorityQueue()
    pq.put((grid.score(), grid))
    while not pq.queue[0][1].legal():
        print(pq.queue[0][1])
        print(pq.qsize())
        print(pq.queue[0][1])
        astep(pq.queue[0][1], pq)
    print(grid, grid.score())
    grid = pq.get()
    print(grid, grid.score())

def astep(grid, pq):
    grid = pq.get()[1]
    for h in grid.houses:
        if grid.houses[h].free:
            for b in grid.batteries:
                copy = deepcopy(grid)
                if connect(copy.houses[h], copy.batteries[b]):
                    pq.put((copy.score() + estimate_cost(copy), copy))
