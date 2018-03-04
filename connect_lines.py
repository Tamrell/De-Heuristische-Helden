# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden\
import random
import copy

# list of houses
neighbourhood = []

class house:
    def __init__(self, x, y):
        self.x, self.y = x, y

class battery:
    def __init__(self, x, y):
        # set max amount of connectable houses
        self.capacity = 5

        # set coordinates
        self.x, self.y = x, y

        # amount of houses that can still be connected
        self.free_spots = self.capacity

class battery_pack:
    def __init__(self, batteries):
        self.batteries = batteries

        # list of batteries that can still be connected
        self.available_batteries = copy.deepcopy(batteries)

    def get_random_battery(self):
        """randomly selects a battery in the pack without having a battery
        supply more than its capacity"""

        random.seed()

        # select random battery
        index = random.randrange(0, len(self.available_batteries), 1)
        battery_ = self.available_batteries[index]

        # keep track of battery capacity
        battery_.free_spots -= 1
        if battery_.free_spots == 0:
            self.available_batteries.remove(battery_)

        return battery_

def gen_houses(n):
    """generates n houses at random coordinates - for testing purposes"""

    random.seed()
    array = []

    # generate houses at random coordinates
    for i in range(n):
        array.append(
            house(random.randrange(0, 100, 1), random.randrange(0, 100, 1))
        )

    return array

class line_solver:
    def connect_random(self, neighbourhood, pack):
        """connects houses and batteries at random"""

        connections = []

        # tuple-up every house with random battery
        for house in neighbourhood:
            battery_ = pack.get_random_battery()
            connections.append([house, battery_])

        return connections

    def __init__(self, neighbourhood, batteries):
        self.neighbourhood = neighbourhood
        self.pack = battery_pack(batteries)
        self.connections = self.connect_random(self.neighbourhood, self.pack)

    def calculate_distances(self, connections):
        """calculates the manhattan distance of a connection"""

        def manhattan_distance(obj1, obj2):
            """calculates the manhattan distance between two objects"""

            # get x and y differences
            x_dif = abs(obj1.x - obj2.x)
            y_dif = abs(obj1.y - obj2.y)

            return x_dif + y_dif

        # add distances of all connections
        total_distance = 0
        for connection in connections:
            total_distance += manhattan_distance(connection[0], connection[1])

        return total_distance

    def shuffle(self, connections):
        """randomly swaps the connections of two houses"""

        # get two random connections
        max_num = len(connections)
        house_n_1 = random.randrange(0, max_num)
        house_n_2 = random.randrange(0, max_num)

        # swap selected connections
        connections[house_n_1][0], connections[house_n_2][0] = connections[house_n_2][0], connections[house_n_1][0]

        return connections

    def improve_hillclimber(self, n, connections):
        """improves a list of connections in terms of manhattan distance
        using a hillclimber algoritm"""

        def improve(connections):
            """tries a randomly changed list of connections"""

            # get old score
            old_connections = connections
            old_distance = self.calculate_distances(old_connections)

            # shuffle connections at random and get new score
            new_connections = self.shuffle(copy.deepcopy(old_connections))
            new_distance = self.calculate_distances(new_connections)

            # compare old and new score
            if new_distance < old_distance:
                return new_connections
            else:
                return old_connections

        # iterate the hillclimber n times
        for i in range(n):
            connections = improve(connections)
        return connections
