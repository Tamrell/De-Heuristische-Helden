# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from operator import itemgetter
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', 'Classes')))
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))

from grid import *
from plots import *
from imports import *

best_case = None

def update_grid(main, connections):
    import house, battery
    Battery.color_generator = assign_color()
    for connection in connections:
        # eerst batterijen aanmaken, dan huizen verbinden!
        house_, battery_ = connection
        grid_house = house.House((house_.x, house_.y, house_.capacity),[])
        grid_battery = battery.Battery((battery_.x, battery_.y), battery_.max_capacity)

        grid_house.bat = grid_battery
        grid_battery.links.add(grid_house)

    return main

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

class LocalHouse:
    def __init__(self, x, y, capacity):
        self.x, self.y = int(x), int(y)
        self.capacity = capacity

class LocalBattery:
    def __init__(self, x, y, current_capacity, max_capacity = 0):
        self.x, self.y = x, y
        if max_capacity != 0:
            self.max_capacity = max_capacity
        self.current_capacity = current_capacity

#sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..', 'Classes')))
fileDir = os.path.abspath(os.path.join(__file__, '..', '..', 'Data'))
filename1 = os.path.join(fileDir, 'wijk1_huizen.csv')
filename2 = os.path.join(fileDir, 'wijk1_batterijen.txt')
print(filename1, filename2)
main = Grid(filename1, filename2)
batteries = [LocalBattery(battery.cord[0], battery.cord[1], 0, battery.max_load) for battery in main.batteries.values()]
number_of_batteries = len(batteries)

house_sort = True
if house_sort:
    # betere oplossing met cord[1]
    houses = [(house.cord[1], house.cord[0], LocalHouse(house.cord[0], house.cord[1], house.output)) for house in main.houses.values()]
    houses = sorted(houses, key=itemgetter(0), reverse=True)
    houses = [house_combi[2] for house_combi in houses]

else:
    houses = [LocalHouse(house.cord[0], house.cord[1], house.output) for house in main.houses.values()]

class case:
    def distance(self, house, battery):
        return abs(house.x - battery.x) + abs(house.y - battery.y)

    def connect(self, house, battery):
        if battery.current_capacity + house.capacity > battery.max_capacity:
            return False

        #self.houses.remove(house)
        battery.current_capacity += house.capacity
        self.connections.append((house, battery))
        return True

    def calc_value(self):
        score = 0
        for connection in self.connections:
            house, battery = connection
            score += self.distance(house, battery)
        return score

    def __init__(self, houses, batteries, connections, value):
        self.value = value
        self.houses = [LocalHouse(house.x, house.y, house.capacity) for house in houses]

        self.batteries = [LocalBattery(battery.x, battery.y, battery.current_capacity, battery.max_capacity) for battery in batteries]
        self.connections = copy.deepcopy(connections)

    def apply_change(self, battery_n):
        # idee: houses[0]
        house = self.houses.pop(0)
        #house = self.houses[0]
        battery = self.batteries[battery_n]
        if self.connect(house, battery):
            self.value += self.distance(house, battery)
            return self.value
        return False

stack = []

root = case(houses, batteries, [], 0)
stack.append((root.value, root))

"""
greedy_case = case(houses, batteries, [], 0)
for house in greedy_case.houses:
    best_distance = 10000
    best_battery = None
    for battery in greedy_case.batteries:
        dist = greedy_case.distance(house, battery)
        if dist < best_distance:
            best_battery = battery
            best_distance = dist
    if not greedy_case.connect(house, battery):
        break
    greedy_case.value += dist
stack.append((greedy_case.value, greedy_case))
"""
#print("greedy opening:\t", greedy_case.value, len(greedy_case.connections))

bound = 10000#3800#3517
iter = 0
scale = 100

start_time = time.time()
if len(sys.argv) == 1:
    print("not enough cmd line args")
    sys.exit()

filename = sys.argv[1]

import csv
rows = []
try:
    with open(filename, "a") as outputfile:
        writer = csv.writer(outputfile, dialect = "excel-tab")

        while len(stack) > 0:
            rows.append([str(iter)+";", str(bound)+";"])

            #if iter > 10000:
            #    sys.exit()
            #if time.time() - start_time > 300:
            #    sys.exit()

            if iter % scale == 0:
                print(iter, best_case, bound)
                try:
                    for row in rows:
                        writer.writerow(row)
                except Exception as e:
                    print("could not safe due to error\t", e)
                rows = []

            (value, current_case) = stack.pop()
            if len(current_case.houses) == 0:
                main = update_grid(current_case, current_case.connections)
                plot(main)
                if value < bound:
                    best_case = current_case
                    bound = value
                    print("solution\t", best_case, "\tvalue\t", value, "\ttime\t", time.time() - start_time , "\titer\t", iter)
            else:
                """
                    tot nu toe beste score: wel batterijen sorteren, maar niet schrappen
                    """
                battery_list = [(i, current_case.batteries[i], current_case.distance(current_case.batteries[i], current_case.houses[0])) for i in range(len(batteries))]
                sorted_batteries = sorted(battery_list, key=itemgetter(2), reverse = True) #omgekeerd vanwege appenden
                number_of_batteries = len(sorted_batteries)

                for battery_combi in sorted_batteries:
                    battery_n = battery_combi[0]

                    new_case = case(current_case.houses, current_case.batteries, current_case.connections, current_case.value)
                    value = new_case.apply_change(battery_n)
                    #value /= len(new_case.connections)
                    if value:
                        if value < bound:
                            try:
                                stack.append((value, new_case))
                            except MemoryError:
                                print("out of memory")
                                try:
                                    for row in rows:
                                        writer.writerow(row)
                                except Exception as e:
                                    print("could not safe during memory error due to error\t", e)
                                sys.exit()
                            """
                            if len(sys.argv) >= 3:
                                if sys.argv[2] == "1":
                                    #"sorteert neerwaards"
                                    stack = sorted(stack, key=itemgetter(0), reverse=True)
                                elif sys.argv[2] == "2":
                                    #"sorteert opwaards"
                                    stack = sorted(stack, key=itemgetter(0), reverse = False)
                            else:
                                pass#print("sorteer niet")"""
                iter += 1
        print("out of stack", iter, bound, time.time() - start_time)


except KeyboardInterrupt:
    print("iter\t", iter, "\tbound\t", bound, "\ttime\t", time.time() - start_time)
