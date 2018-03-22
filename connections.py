# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
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
                connected to"""

        # determine input type
        element = type(item)
        
        if element == House:
            return item.bat

        elif element == Battery:
            return list({con for con in self.connections if con[1] == item})
        else:
            return None

    def connect(self, house, battery):
        house.bat = battery
        battery.links.append(house)
        self.connections.add((house, battery))

    def disconnect_house(self, house):
        if (house, house.bat) in connections:
            self.connections.remove((house, house.bat))
            house.bat = None
            return True
        else:
            return False

    def disconnect_battery(self, battery):
        battery_links = battery.links
        for item in battery_links:
            self.connections.remove(item)
        battery_links = []

        return True

    def swap_connection(self, house1, house2):

        # swap in set
        self.connections.remove((house1, house1.bat))
        self.connections.add((house1, house2.bat))
        self.connections.remove((house2, house2.bat))
        self.connections.add((house2, house1.bat))

        # swap in grid
        battery1, battery2 = house1.bat, house2.bat
        house1.bat, house2.bat = house2.bat, house1.bat

        return True

    def calculate_score(self):
        score = 0
        for connection in connections:
            score += calculate_distance(connection)
        return score

    def test(self, batteries):
        for connection in self.connections:
            battery = connection[1]
            cap = 0
            for house in battery.links:
                cap += house.output
            if cap > battery.max_load:
                return battery
        return True
