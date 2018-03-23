# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
from house import *
from battery import *

class Connections:
    def __init__(self):
        self.connections=set()

    def show_connections(self):
        """This function prints the list of connections
        Takes
            None
        Returns
            None"""

        print(self.connections)

    def get_connection(self, item):
        """This function returns a list of connections to either a house
        or a battery
        Takes
            item: either a House or a Battery instance
        Returns
            Battery instance: the Battery instance a given House instance is
                connected to
            list of House instances: list of houses a given battery is
                connected to
        Raises
            custom exception: if instance type is neither House nor Battery"""

        # input is house instance
        if isinstance(item, House):
            return item.bat

        # input is battery instance
        elif isinstance(item, Battery):
            return list({con for con in self.connections if con[1] == item})

        # input is something else
        else:
            raise Exception("Invalid input type")

    def connect(self, house, battery):
        """This function connects a house to a battery in the grid and in the
            local representation. Also checks if battery does not get
            overconnected by connecting house
        Takes
            house: a House instance
            battery: the Battery instance house must be connected to
        Returns
            True if battery could be connected; else False"""

        # check for overloadedness
        if battery.load + house.output > battery.max_load:
            return False

        battery.load += house.output

        # connect in grid
        house.bat = battery
        house.color = battery.color
        battery.links.append(house)
        # connect in local repr
        self.connections.add((house, battery))
        return True

    def disconnect(self, item):
        """This function disconnects either a battery or house (given as param)
        both in grid as in local repr

        Takes
            item: either a House or Battery instance to be disconnected
        Returns
            True if disconnection was succesfull; else False"""

        # disconnect house
        if isinstance(item, House):
            try:
                # disconnect in local repr
                self.connections.remove((item, item.bat))

                # disconnect in grid
                item.bat = None

            # instance not connected
            except KeyError:
                return False

            return True

        # disconnect battery
        elif isinstance(item, Battery):

            battery_links = item.links

            # battery not connected
            if len(battery_links) == 0:
                return True

            for house in battery_links:
                try:
                    # disconnect in local repr
                    self.connections.remove((item, house))

                    # disconnect in grid
                    battery_links.remove(house)

                except KeyError:
                    return False

        else:
            raise Exception("unvalid input type")
        return True

    def swap_connection(self, house1, house2):
        """This function swaps two houses from two seperate batteries
        Takes
            house1, house2: House instances from two seperate batteries
        Returns
            True if swap was succesfull"""

        # check if not connected to same battery
        if house1.bat == house2.bat:
            print("U an idiot")
            return False

        # swap in local repr
        self.connections.remove((house1, house1.bat))
        self.connections.add((house1, house2.bat))
        self.connections.remove((house2, house2.bat))
        self.connections.add((house2, house1.bat))

        # swap in grid
        battery1, battery2 = house1.bat, house2.bat
        house1.bat, house2.bat = house2.bat, house1.bat

        return True

    def calculate_distance(self, battery, house):
        """This function calculates the distance between a battery and a house
        Takes:
            battery: Battery instance as starting point of connection
            house: House instance as endpoint
        Returns:
            distance between battery and house"""

        (x1, y1) = battery.cord
        (x2, y2) = house.cord

        return abs(x1-x2) + abs(y1 - y2)

    def calculate_score(self):
        """This function calculates the cost of a given set of connections
        Takes:
            none
        Returns
            score: the sum of manhattan distances between all houses and their
            respective batteries"""

        score = 0
        for connection in connections:
            (house, battery) = connections
            score += calculate_distance(battery, house)
        return score

    def test(self):
        """This function tests if no batteries are overconnected
        Takes:
            none
        Returns:
            list of Battery instances consisting of all overconnected
            Battery instances; else True"""

        overloaded_batteries = []
        for connection in self.connections:
            battery = connection[1]
            cap = 0
            for house in battery.links:
                cap += house.output
            if cap > battery.max_load:
                overloaded_batteries.append(battery)

        # return list if non-empty
        if len(overloaded_batteries):
            return overloaded_batteries
        return True
