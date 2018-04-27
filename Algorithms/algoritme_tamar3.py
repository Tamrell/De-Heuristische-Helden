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

# get first case
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')

root = Grid(filename1, filename2, "1")

houses = list(root.houses)
n_houses = len(houses)

batteries = list(root.batteries)

connections = connections.Connections()
bound = 10000
best_case = None

stack = [(bound, root)]

def sorted_list(grid, house, rev = True):
    return sorted([(grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = rev)
def unsorted_list(grid, house):
    return [(grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()]
def load_list(grid, house, rev = False):
    return sorted([(battery.load, battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = rev)
def concede_list(grid, house):
    return sorted([(battery.load * grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = rev)
import time
start_time = time.time()
iter = 0

while True:#time.time() - start_time < 600:
    if len(stack) == 0:
        sys.exit()

    if iter % 10 == 0:
        print(iter, len(stack), bound)
        #stack.sort(key=operator.itemgetter(0), reverse = True)

    score, current_grid = stack.pop()

    if len(current_grid.houses) == 0:
        score = current_grid.score()
        if score < bound:
            bound = score
            best_case = current_grid
            print("solution", iter, current_grid.score())
        continue

    house = list(current_grid.houses).pop()
    battery_list = load_list(current_grid, house)
    for dist, battery in battery_list:
        if connections.connect(current_grid.houses[house], battery):
            if current_grid.score() < bound:
                new_grid = copy.deepcopy(current_grid)
                del new_grid.houses[house]

                stack.append((new_grid.score(), new_grid))
                connections.unconnect(current_grid.houses[house])
    iter += 1
