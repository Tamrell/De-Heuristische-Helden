# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
# en we kunnen dit doen: een functie schrijven die de minimale afstand van alle huizen vermenigvuldigt
# met het aantal lege huizen, en kijkt of dit boven de bound komt
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
import random

# get first case
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')

def check_feasability(grid, bound):
    min_dist = 0
    for house in grid.houses.values():
        try:
            min_dist += house.dists[house.find_closest_battery(grid)]
        except:
            return False
    return min_dist + grid.score() < bound

def setup():
    args = len(sys.argv)

    end_condition = str(sys.argv[1])
    if end_condition == "True":
        def running(start_time, iterations):
            return True
    elif end_condition[-1] == "s":
        def running(start_time, iterations):
            return time.time() - start_time < int(sys.argv[1][:-1])
    else:
        def running(start_time, iterations):
            return iterations < int(sys.argv[1])

    sort_method = str(sys.argv[2])
    if sort_method == "dist":
        def battery_list(grid, house):
            return sorted([(grid.houses[house].dists[battery], battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = True)
    elif sort_method == "load":
        def battery_list(grid, house):
            return sorted([(battery.load, battery) for battery in grid.batteries.values()], key = operator.itemgetter(0), reverse = False)
    else:
        def battery_list(grid, house):
            return [(battery.load, battery) for battery in grid.batteries.values()]

    if len(sys.argv) > 3:
        filter_stack = True if str(sys.argv[3]) == "True" else False
        shuffle_stack = True if str(sys.argv[4]) == "True" else False

        if filter_stack:
            def filter(stack, bound):
                init_len = len(stack)
                for grid in stack:
                    if grid[1].score() > bound:
                        stack.remove(grid)
                print("filter removed\t", init_len - len(stack), "\tcases")
                return stack
        else:
            def filter(stack, bound):
                return True

        if shuffle_stack:
            def shuffle(stack):
                print("Shuffelling")
                return random.shuffle(stack)
        else:
            def shuffle(stack):
                return stack
    if len(sys.argv) > 5:
        prune_dist = int(sys.argv[5]) if sys.argv[5].isdigit() else False
        if prune_dist:
            # set limiet aan hoe ver de batterij van het huis mag staan
            def check_battery(battery, house):
                return prune_dist > house.dists[battery]
        else:
            def check_battery(battery, house):
                return True


    return (running, battery_list, filter, shuffle)

def search(root, connections):
    print("Setting up\n")
    (running, battery_list, filter, shuffle) = setup()

    start_time, iter, count, bound, best_case = time.time(), 0, 0, 4000, None

    houses = list(root.houses)
    n_houses = len(houses)
    batteries = list(root.batteries)

    stack = [(bound, root)]

    while running(start_time, iter):
        if len(stack) == 0:
            sys.exit()

        score, current_grid = stack.pop()
        if not check_feasability(current_grid, bound):
            continue

        if len(current_grid.houses) == 0:
            score = current_grid.score()
            if score < bound:
                count = 0
                bound = score
                best_case = current_grid

                stack = filter(stack, bound)

                print("solution", iter, current_grid.score())
            continue

        house = list(current_grid.houses).pop()
        b_list = battery_list(current_grid, house)
        for dist, battery in b_list:
            if connections.connect(current_grid.houses[house], battery):
                if current_grid.score() < bound:

                    new_grid = copy.deepcopy(current_grid)
                    del new_grid.houses[house]

                    stack.append((new_grid.score(), new_grid))
                    connections.unconnect(current_grid.houses[house])

        if iter % 100 == 0:
            print(iter, len(stack), bound)
        if count == 1000:
            if len(stack) < 2000:
                stack == shuffle(stack)
            else:
                print("Sorting")
                stack = sorted(stack, key = operator.itemgetter(0))
            count = 0
        iter += 1
        count += 1

if __name__ == "__main__":
    print("Alles geladen")
    root = Grid(filename1, filename2, "1")
    connections = connections.Connections()
    print("Root geinitialiseerd")
    search(root, connections)
