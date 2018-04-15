# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
import sys
import random
import copy
import time
from operator import itemgetter

from grid import *

best_case = None

def check(connections):
    batteries = {}
    for item in connections:
        house, battery = item
        if battery in batteries:
            batteries[battery] += house.capacity
            if battery.current_capacity > battery.max_capacity:
                return False
        else:
            batteries[battery] = house.capacity
    return True

class House:
    def __init__(self, x, y, capacity):
        self.x, self.y = int(x), int(y)
        self.capacity = capacity

class Battery:
    # hier zit iets fout:
    def __init__(self, x, y, current_capacity, max_capacity = 0):
        self.x, self.y = x, y
        if max_capacity != 0:
            self.max_capacity = max_capacity
        self.current_capacity = current_capacity


main = Grid("wijk1_huizen.csv", "wijk1_batterijen.txt")
batteries = [Battery(battery.cord[0], battery.cord[1], 0, battery.max_load) for battery in main.batteries.values()]
number_of_batteries = len(batteries)
houses = [House(house.cord[0], house.cord[1], house.output) for house in main.houses.values()]

class case:
    def distance(self, house, battery):
        return abs(house.x - battery.x) + abs(house.y - battery.y)

    def connect(self, house, battery):
        if battery.current_capacity + house.capacity > battery.max_capacity:
            return False

        self.houses.remove(house)
        battery.current_capacity += house.capacity
        self.connections.append((house, battery))
        return True

    def value(self):
        score = 0
        for connection in self.connections:
            house, battery = connection
            score += self.distance(house, battery)
        return score

    def __init__(self, houses, batteries, connections, value):
        self.value = value
        self.houses = []
        for house in houses:
            new_house = House(house.x, house.y, house.capacity)
            self.houses.append(new_house)

        self.batteries = []
        for battery in batteries:
            new_battery = Battery(battery.x, battery.y, battery.current_capacity, battery.max_capacity)
            self.batteries.append(new_battery)

        self.connections = copy.deepcopy(connections)

    def apply_change(self, battery_n):
        house = self.houses[0]
        battery = self.batteries[battery_n]
        if self.connect(house, battery):
            self.value += self.distance(house, battery)
            return self.value
        return False

stack = []
current_case = case(houses, batteries, [], 0)
stack.append((current_case.value, current_case))

bound = 10000
iter = 0
scale = 100

start_time = time.time()
if len(sys.argv) == 1:
    print("not enough cmd line args")
    sys.exit()

filename = sys.argv[1]
outputfile = open(filename,"wb")

import csv
rows = []
with open(filename, "a") as outputfile:
    writer = csv.writer(outputfile, dialect = "excel-tab")

    while len(stack) > 0:
        rows.append([str(iter)+";", str(bound)+";"])

        if iter > 35000:
            break
        #if time.time() - start_time > 30:
        #    break

        if iter % scale == 0:
            print(iter, best_case, bound)
            for row in rows:
                writer.writerow(row)
            rows = []


        (value, current_case) = stack.pop()
        if len(current_case.houses) == 0:
            if best_case == None:
                best_case = current_case
            else:
                if value < bound:
                    best_case = current_case
                    bound = value


        else:

            for i in range(number_of_batteries):
                new_case = case(current_case.houses, current_case.batteries, current_case.connections, current_case.value)
                value = new_case.apply_change(i)
                #value /= len(new_case.connections)
                if value != False:
                    if value < bound:
                        try:
                            stack.append((value, new_case))
                        except MemoryError:
                            print("out of memory")
                            for row in rows:
                                writer.writerow(row)
                            sys.exit()

                        if len(sys.argv) >= 3:
                            if sys.argv[2] == "1":
                                #"sorteert neerwaards"
                                stack = sorted(stack, key=itemgetter(0), reverse=True)
                            elif sys.argv[2] == "2":
                                #"sorteert opwaards"
                                stack = sorted(stack, key=itemgetter(0), reverse = False)
                        else:
                            pass#print("sorteer niet")
            iter += 1

    for row in rows:
        writer.writerow(row)

print(iter, time.time() - start_time)
