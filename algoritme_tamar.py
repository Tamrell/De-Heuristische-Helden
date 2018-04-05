# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
import sys
import random
import copy

class House:
    def __init__(self, x, y, capacity):
        self.x, self.y = x, y
        self.capacity = capacity

class Battery:
    def __init__(self, x, y, capacity):
        self.x, self.y = x, y
        self.max_capacity = capacity
        self.current_capacity = 0

number_of_batteries = 5
batteries = [Battery(random.randint(0, 100), random.randint(0, 100), 100) for i in range(5)]
houses = [House(random.randint(0, 100), random.randint(0, 100), 20) for i in range(25)]

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
        if len(houses) == 0:
            print(connections)
            return

        self.houses = copy.copy(houses)
        self.batteries = copy.copy(batteries)
        self.connections = copy.deepcopy(connections)
        self.score = self.value()

    def apply_change(self, battery_n):
        if self.connect(self.houses[0], self.batteries[battery_n]):
            return self.value()
        else:
            return False

stack = []
root = case(houses, batteries, [])
stack.append(root)

best = 1000
iter = 0
falsified = 0
total = 0
for current_case in stack:
    iter += 1
    try:
        appended = 0
        for i in range(number_of_batteries):
            new_case = case(copy.copy(current_case.houses), copy.copy(current_case.batteries), copy.copy(current_case.connections))
            value = new_case.apply_change(i)
            if value != False:
                falsified += 1
                print(len(new_case.connections))
                if value <= best:
                    total += 1
                    stack.append(new_case)
                    appended += 1
        print(appended, len(stack))
    except MemoryError:
        print("out of memory")
        sys.exit()
print(falsified, total)
