class Lightweight_house:
    def __init__(self, cord, capacity):
        self.cord = cord
        self.capacity = capacity

class Lightweight_battery:
    def __init__(self, cord, load, max_load):
        self.cord = cord
        self.load = load
        self.max_load = max_load
        self.links = set()

class Lightweight_grid:
    def __init__(self):
        #cord, battery
        self.score = 0
        self.batteries = {}
        self.houses = {}
        self.connections = []

    def connect(self, house, battery):
        if battery.load + house.output > battery.max_load:
            return False

        battery.load += house.output
        battery.links.add(house)
        house.bat = battery

        self.houses.pop((int(house.cord[0]), int(house.cord[1])))

        self.connections.append((house.cord, battery.cord))
        self.score += house.distance(house.cord, battery.cord)
        return True
