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

    def __init__(self, houses, batteries, connections):
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
        if self.connect(self.houses[0], self.batteries[battery_n]):
            return self.value()
        return False

stack = []
root = case(houses, batteries, [])
stack.append((root.value(),root))

bound = 10000
iter = 0
scale = 100

current_case = stack[0]

start_time = time.time()

while len(stack) > 0:
    """
    if iter % scale == 0:
        print(iter, best_case, bound)
        """


    (value, current_case) = stack.pop()
    #print(bound, len(current_case.houses), len(stack))
    if len(current_case.houses) == 0:
        if best_case == None:
            best_case = current_case
        else:
            if value < bound:
                best_case = current_case
                bound = value
                print("iter, time, bound", iter, time.time() - start_time, bound, len(stack))

    else:
        try:
            for i in range(number_of_batteries):
                new_case = case(current_case.houses, current_case.batteries, current_case.connections)
                value = new_case.apply_change(i)

                if value != False:
                    if value < bound:
                        stack.append((value, new_case))
                        stack = sorted(stack, key=itemgetter(0), reverse=True)
            iter += 1

        except MemoryError:
            print("out of memory")
            sys.exit()
"""
        except Exception as e:
            print(e)
"""
print(iter)
