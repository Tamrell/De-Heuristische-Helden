# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from grid import *
import copy
import random

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
    def __init__(self, x, y, current_capacity, max_capacity = 0):
        self.x, self.y = x, y
        if max_capacity != 0:
            self.max_capacity = max_capacity
        self.current_capacity = current_capacity

#main = Grid("wijk1_huizen.csv", "wijk1_batterijen.txt")
#main = Grid("wijk2_huizen.csv", "wijk2_batterijen.txt")
main = Grid("wijk1_huizen.csv", "wijk1_batterijen.txt")

batteries = [Battery(battery.cord[0], battery.cord[1], 0, battery.max_load) for battery in main.batteries.values()]
number_of_batteries = len(batteries)
houses = [House(house.cord[0], house.cord[1], house.output) for house in main.houses.values()]

class case:
    def distance(self, house, battery):
        return abs(house.x - battery.x) + abs(house.y - battery.y)

    def connect(self, house, battery, test = True):
        if (battery.current_capacity + house.capacity > battery.max_capacity) and test:
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

    def swap(self):
        new_connections = copy.deepcopy(self.connections)
        new_connections[random.randint(0, len(new_connections - 1))] = random.randint(0, len(new_connections - 1))
        if check(new_connections):
            self.connections = new_connections
            return True
        else:
            return False

scene = case(houses, batteries, [])

# stap 1: greedy
iter = 0

while(len(scene.houses) > 0):
    house = scene.houses.pop()

    best_battery = None
    dist = 10000

    for battery in scene.batteries:
        current_distance = scene.distance(house, battery)
        if current_distance < dist:
            best_battery = battery
            dist = current_distance
        iter += 1

    scene.connections.append((house, best_battery))
    best_battery.current_capacity += house.capacity

print("case klopt: ", check(scene.connections))
print(scene.value())
# stap 2: optimize for \Theta
class bfs_case:
    def value(self, batteries):
        score = 0
        for battery in batteries:
            if battery.max_capacity - battery.current_capacity < 0:
                score += battery.max_capacity - battery.current_capacity
        return score

    def normalise(self, batteries):
        for battery in batteries:
            battery.current_capacity = 0

        for i in range(len(houses)):
            batteries[i].current_capacity += houses[i].capacity
        return(batteries)

    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = self.normalise(copy.copy(batteries))
        self.Theta = self.value(self.batteries)

    def swap(self, houses, batteries):
        n1, n2 = 0, 0
        while(n1 == n2):
            while(batteries[n1] == batteries[n2]):
                n1 = random.randint(0, len(houses) - 1)
                n2 = random.randint(0, len(houses) - 1)

        houses[n1], houses[n2] = houses[n2], houses[n1]
        return(houses, self.normalise(batteries))

stack = []
houses = []
batteries = []
for connection in scene.connections:
    house, battery = connection
    houses.append(house)
    batteries.append(battery)
current_case = bfs_case(scene.houses, scene.batteries)
