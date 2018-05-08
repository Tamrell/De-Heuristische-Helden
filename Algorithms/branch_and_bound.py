# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
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
        (house_c, battery_c) = connection
        root_house, root_battery = root.houses[house_c], root.batteries[battery_c]
        root_battery.load += root_house.output
        root_house.bat = root_battery
        root_house.color = root_battery.color
        root_house.free = False
        root_battery.links.add(root_house)

    return root

cutoffs = []
def feasible(grid, bound):
    min_dist = 0
    for house_c in grid.houses.keys():
        distances = []
        for battery_c in grid.batteries.keys():
            distances.append(abs(house_c[0] - battery_c[0]) + abs(house_c[1] - battery_c[1]))
        min_dist += min(distances)

    if not min_dist + grid.score < bound:
        global cutoffs
        cutoffs.append(len(grid.houses))
    return (min_dist + grid.score < bound)

def sorted_batteries(batteries, house):
    b_list = [(house.distance(battery), battery) for battery in batteries]
    b_list = sorted(b_list, key=operator.itemgetter(0), reverse = True)
    return [battery.cord for (distance, battery) in b_list]

def make_cases(grid, bound):
    cases = []
    house_c = list(grid.houses.keys()).pop()
    house = grid.houses[house_c]
    for battery_c in sorted_batteries(grid.batteries.values(), house):

        new_case = Lightweight_grid()
        new_case.houses = copy.deepcopy(grid.houses)
        new_case.batteries = copy.deepcopy(grid.batteries)
        new_case.score = grid.score

        new_case.connections = copy.deepcopy(grid.connections)
        house = new_case.houses.pop(house_c)

        if new_case.connect(house, new_case.batteries[battery_c]):
            if feasible(new_case, bound):
                cases.append(new_case)
    return cases

def running(iter):
    return iter < 10000

def search(grid):
    old_grid = grid
    print("Welcome to Branch and Bound Solutions. We offer solutions to any problem, as long as it contains houses and batteries. We begin searching right away.")

    start_time, iter, count, best_case = time.time(), 0, 0, None
    bound = int(input("Bound: "))
    n_houses = len(grid.houses)

    root = Lightweight_grid()
    for battery in grid.batteries.keys():
        old_battery = grid.batteries[battery]
        root.batteries[battery] = Lightweight_battery(old_battery.cord, old_battery.load, old_battery.max_load)
    for house in grid.houses.keys():
        old_house = grid.houses[house]
        root.houses[house] = Lightweight_house(old_house.cord, old_house.output)

    stack = [(bound, root)]

    while True:
        # no solution
        if len(stack) == 0:
            sys.exit()

        # get case
        score, current_grid = stack.pop()

        if len(current_grid.houses) == 0:
            obese_gr = obese_grid(current_grid, grid)
            score = obese_gr.score()
            print("Branch and Bound found a solution!", score)
            if input("Keep this one, or keep searching? y = stop/n = search on!") == "y":
                return obese_gr
            if score < bound:
                bound = score
                best_case = obese_grid(current_grid, grid)
            continue

        for case in make_cases(current_grid, bound):
            stack.append((case.score, case))

        if iter % 100 == 0:
            print(iter, len(stack), bound, time.time() - start_time)
            start_time = time.time()

        iter += 1

def branch_and_bound(grid):
    try:
        search(grid)
    except KeyboardInterrupt:
        import statistics
        print("Cutoff mean at\t", statistics.mean(cutoffs))
        print("With sd\t", statistics.stdev(cutoffs))
        return grid
