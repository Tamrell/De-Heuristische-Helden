# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden

import statistics
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', '..', 'Classes')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', '..', 'Data')))

from grid import *

fileDir = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'Data'))
grids = {}
for nbh in range(1, 4):
    houses_file = os.path.join(fileDir, 'wijk' + str(nbh) + '_huizen.csv')
    batteries_file = os.path.join(fileDir, 'wijk' + str(nbh) + '_batterijen.txt')
    Battery.color_generator = assign_color()
    grids[nbh] = Grid(houses_file, batteries_file, nbh)

for i in range(1, 4):
    print("#" * 80)
    print("Wijk " + str(i) + ":\t")

    houses = grids[i].houses.values()
    house_outputs = [house.output for house in houses]

    print("Gemiddelde ouptut van huizen:\t", statistics.mean(house_outputs))
    print("Met als deviatie:\t", statistics.stdev(house_outputs))

    distances = []
    for house in houses:
        for distance in house.dists.values():
            distances.append(distance)
    print("Gemiddelde afstand van elk huis tot elke batterij:\t", statistics.mean(distances))
    print("Met als deviatie:\t", statistics.stdev(distances))
