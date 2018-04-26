# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from operator import itemgetter
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', 'Classes')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))

from grid import *
from plots import *
import connections

# get first case
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')

grid = Grid(filename1, filename2, "1")

houses = list(grid.houses)
n_houses = len(houses)

batteries = list(grid.batteries)

root = connections.Connections()

stack = [([(houses[0], battery)], houses[1:]) for battery in batteries]

connections = connections.Connections()

for iter in range(100000):
    try:
        current_case, current_houses = stack.pop()

        # check for solution
        if len(current_houses) == 0:
            print(iter, len(current_case), len(houses))
            sys.exit()

        # apply change
        for battery in batteries:
            new_case = copy.deepcopy(current_case)
            new_houses = copy.copy(current_houses)

            current_house = new_houses.pop()

            new_case.append((current_house, battery))

            house_o = grid.houses[current_house]
            battery_o = grid.batteries[battery]

            if connections.connect(house_o, battery_o):
                connections.disconnect(house_o)
                stack.append((new_case, new_houses))

        if iter%100 == 0:
            print(iter, len(current_houses))

    except IndexError:
        print(len(current_houses))
