# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from operator import itemgetter
import sys
import os
import operator
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', 'Classes')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))

from grid import *
from plots import *
import connections
import time

# get first case
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')

args = len(sys.argv)
if args > 0:
    b_sort = str(sys.argv[1])
else:
    b_sort = None
if args > 1:
    filter_stack = True if sys.argv[2] == "T" else False

root = Grid(filename1, filename2, "1")

houses = list(root.houses)
n_houses = len(houses)

batteries = list(root.batteries)

connections = connections.Connections()
bound = 10000
best_case = None
import random
stack = [(bound, root)]

def filter(stack, bound):
    init_len = len(stack)
    for grid in stack:
        if grid[1].score() > bound:
            stack.remove(grid)
    print("filter removed\t", init_len - len(stack), "\tcases")
    return stack

def b_list(grid, house, sort):
    if sort == "dist":
        return sorted([(grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = True)
    if sort == "load":
        return sorted([(battery.load, battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = False)
    if sort == "None":
        return [(grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()]

start_time = time.time()
iter = 0

count = 0
while True:#time.time() - start_time < 600:
    if len(stack) == 0:
        sys.exit()
        #stack.sort(key=operator.itemgetter(0), reverse = True)

    score, current_grid = stack.pop()

    if len(current_grid.houses) == 0:
        #random.shuffle(stack)
        score = current_grid.score()
        if score < bound:
            count = 0
            bound = score
            best_case = current_grid

            if filter_stack:
                stack = filter(stack, bound)

            print("solution", iter, current_grid.score())
        continue

    house = list(current_grid.houses).pop()
    battery_list = b_list(current_grid, house, b_sort)
    for dist, battery in battery_list:
        if connections.connect(current_grid.houses[house], battery):
            if current_grid.score() < bound:

                new_grid = copy.deepcopy(current_grid)
                del new_grid.houses[house]

                stack.append((new_grid.score(), new_grid))
                connections.unconnect(current_grid.houses[house])

    if iter % 100 == 0:
        print(iter, len(stack), bound)
    if count == 1000:
        random.shuffle(stack)
        print("reset")
        count = 0
    iter += 1
    count += 1
