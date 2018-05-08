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
    """
    This function applies the solution from B&B to the grid.Grid object given to
    the algorithm.
    Takes:
        lightweight_grid: Lightweight_grid object to apply to a grid.Grid object
        root: grid.Grid object to apply solution to
    Returns
        root: grid.Grid object with solution applied to
    """

    # make sure to start from an empty grid.Grid object
    root.reset()

    # apply solution
    for connection in lightweight_grid.connections:
        (house_c, battery_c) = connection

        # connect house and battery
        root_house, root_battery = root.houses[house_c], root.batteries[battery_c]
        root_battery.load += root_house.output
        root_house.bat = root_battery
        root_house.color = root_battery.color
        root_house.free = False
        root_battery.links.add(root_house)

    return root

# global variable for measuring bound effectivity
cutoffs = []

def feasible(grid, bound):
    """This function finds if a given solution is feasible in terms of the given
    bound.
    Takes:
        grid: Lightweight_grid object to evaluate
        bound: bound to evaluate to
    Returns:
        True if there is a possibility of a solution within bound, else False"""

    # find distance from every house to its closest battery
    min_dist = 0
    for house_c in grid.houses.keys():
        distances = []
        for battery_c in grid.batteries.keys():
            distances.append(abs(house_c[0] - battery_c[0]) + abs(house_c[1] - battery_c[1]))
        min_dist += min(distances)

    # test if bound is feasible
    if not min_dist + grid.score < bound:
        global cutoffs

        # for bound effectivity measurement
        cutoffs.append(len(grid.houses))

    return (min_dist + grid.score < bound)

def sorted_batteries(batteries, house):
    """
    This function sorts the batteries of a grid in terms of distance to a
    specified house.
    Takes:
        batteries: list of batteries
        house: house to sort batteries to in terms of distance
    Returns:
        orderd list of batteries (same batteries, different order)
    """
    b_list = [(house.distance(battery), battery) for battery in batteries]

    # sort from large to small because of stack
    b_list = sorted(b_list, key=operator.itemgetter(0), reverse = True)
    return [battery.cord for (distance, battery) in b_list]

def make_cases(grid, bound):
    """
    This function generates a case for a given case with in each a different
    battery connected to the first free house in the list.
    Takes:
        grid: Lightweight_grid object to branch off
        bound: bound to prune unimportant solutions
    Returns:
        list of generated cases
    """
    cases = []

    # get house
    house_c = list(grid.houses.keys()).pop()
    house = grid.houses[house_c]

    # make case for every battery
    for battery_c in sorted_batteries(grid.batteries.values(), house):

        # create new case
        new_case = Lightweight_grid()
        new_case.houses = copy.deepcopy(grid.houses)
        new_case.batteries = copy.deepcopy(grid.batteries)
        new_case.score = grid.score
        new_case.connections = copy.deepcopy(grid.connections)

        # get house in current_grid
        house = new_case.houses.pop(house_c)

        # try connecting to battery
        if new_case.connect(house, new_case.batteries[battery_c]):

            # check for bound
            if feasible(new_case, bound):
                cases.append(new_case)
    return cases

def running(iter):
    """This function binds the running of an algorithm to 10000 iterations"""
    return iter < 10000

def search(grid):
    """This function is the implementation of a branch and bound with a "looking
    forward in state-space"-element.
    Takes:
        grid: grid.Grid object, which gives the details of houses and batteries, and
            in which to store the found solution.
    Returns:
        True
    """

    old_grid = grid

    print("""Welcome to Branch and Bound Solutions.
    We offer solutions to any problem, as long as it contains
    houses and batteries. We begin searching right away.""")

    start_time, iter, count, best_case = time.time(), 0, 0, None

    # let user define bound
    bound = int(input("Bound: "))

    n_houses = len(grid.houses)

    # transcribe grid to Lightweight_grid object for efficiency
    root = Lightweight_grid()
    for battery in grid.batteries.keys():
        old_battery = grid.batteries[battery]
        root.batteries[battery] = Lightweight_battery(old_battery.cord, old_battery.load, old_battery.max_load)
    for house in grid.houses.keys():
        old_house = grid.houses[house]
        root.houses[house] = Lightweight_house(old_house.cord, old_house.output)

    # init stack
    stack = [(bound, root)]

    while True:
        # no solution
        if len(stack) == 0:
            sys.exit()

        # get case
        score, current_grid = stack.pop()

        # case is a solution
        if len(current_grid.houses) == 0:
            # transcribe back to grid.Grid object
            obese_gr = obese_grid(current_grid, grid)

            # user input for program flow
            score = obese_gr.score()
            print("Branch and Bound found a solution!", score)
            if input("Keep this one, or keep searching? y = stop/n = search on!") == "y":
                return obese_gr
            if score < bound:
                bound = score
                best_case = obese_grid(current_grid, grid)
            continue

        # branch further
        for case in make_cases(current_grid, bound):
            stack.append((case.score, case))

        # show program flow information
        if iter % 100 == 0:
            print(iter, len(stack), bound, time.time() - start_time)
            start_time = time.time()

        iter += 1

def branch_and_bound(grid):
    """
    This function initiates the algorithm and stops it somewhat gracefully if
    the users performs a KeyboardInterrupt.
    Takes:
        grid: grid.Grid item to apply solution to
    Returns
        None
    """
    try:
        search(grid)
    except KeyboardInterrupt:
        # show prune efficiency
        import statistics
        print("Cutoff mean at\t", statistics.mean(cutoffs))
        print("With sd\t", statistics.stdev(cutoffs))
        return grid
