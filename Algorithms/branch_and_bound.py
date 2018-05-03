# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
# en we kunnen dit doen: een functie schrijven die de minimale afstand van alle huizen vermenigvuldigt
# met het aantal lege huizen, en kijkt of dit boven de bound komt
from operator import itemgetter
import sys
import os
import operator
import copy

sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', 'Classes')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))

from lightweight import *
import time
import random

# get first case
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')

def obese_grid(lightweight_grid, root):
    root.reset()
    for connection in lightweight_grid.connections:
        print(len(lightweight_grid.connections))
        (house_c, battery_c) = connection
        root_house, root_battery = root.houses[house_c], root.batteries[battery_c]

        root_battery.load += root_house.output
        root_house.bat = root_battery
        root_house.color = root_battery.color
        root_house.free = False
        root_battery.links.add(root_house)
    return root

def check_feasability(grid, bound):
    min_dist = 0
    for house_c in grid.houses.keys():
        distances = []
        for battery_c in grid.batteries.keys():
            distances.append(abs(house_c[0] - battery_c[0]) + abs(house_c[1] - battery_c[1]))
        min_dist += min(distances)
    return min_dist + grid.score < bound

def make_cases(grid, bound):
    cases = []
    for battery_c in grid.batteries.keys():

        new_case = Lightweight_grid()
        new_case.houses = copy.deepcopy(grid.houses)
        new_case.batteries = copy.deepcopy(grid.batteries)

        house_c = list(new_case.houses.keys()).pop()
        house = new_case.houses.pop(house_c)

        if new_case.connect(house, new_case.batteries[battery]):
            if check_feasability(new_case, bound):
                cases.append(new_case)
    return cases

def running(iter):
    return iter < 10000

def search(grid):
    old_grid = grid
    print("Welcome to Branch and Bound Solutions. We offer solutions to any problem. We begin searching right away.")

    start_time, iter, count, bound, best_case = time.time(), 0, 0, 10000, None

    n_houses = len(grid.houses)

    root = Lightweight_grid()
    for battery in grid.batteries.keys():
        old_battery = grid.batteries[battery]
        root.batteries[battery] = Lightweight_battery(old_battery.cord, old_battery.load, old_battery.max_load)
    for house in grid.houses.keys():
        old_house = grid.houses[house]
        root.houses[house] = Lightweight_house(old_house.cord, old_house.output)

    stack = [(bound, root)]

    while running(iter):
        # no solution
        if len(stack) == 0:
            sys.exit()

        # get case
        score, current_grid = stack.pop()

        if len(current_grid.houses) == 0:
            print("Branch and Bound found a solution!")
            return obese_grid(current_grid, grid)
            score = current_grid.score()
            if score < bound:
                count = 0
                bound = score
                best_case = current_grid

                stack = filter(stack, bound)
                print("solution", iter, current_grid.score())
            continue

        for case in make_cases(current_grid, bound):
            stack.append((case.score, case))

        if iter % 10 == 0:
            print(iter, len(stack), bound)

        iter += 1
        count += 1

def branch_and_bound(grid):
    return search(grid)
