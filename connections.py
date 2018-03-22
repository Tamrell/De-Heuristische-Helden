# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
class Connections:
    def __init__(self):
        self.connections=[]

    def show_connections(self):
        sorted_connections = sorted(self.connections)
        for connection in sorted_connections:
            house, battery = connection
            print(house.cord, battery.cord)

    def get_connection(self, item):
        element = type(item)
        if element == Battery:
            return item.links
        elif element == House:
            return item.bat
        else:
            return None

    def connect(self, house, battery):
        house.bat = battery
        battery.links.append(house)
        self.connections.append((house, battery))

    def disconnect_house(self, house):
        if (house, house.bat) in connections:
            self.connections.remove((house, house.bat))
            house.bat = None
            return True
        else:
            return False

    def disconnect_battery(self, battery):
        battery.links = []
        for connection in self.connections:
            if connection[1] == battery:
                self.connections.remove(connection)

        return True

    def swap_connection(self, house1, house2):
        for connection in connections:
            if connection == (house1, house1.bat):
                connection = (house1, house2.bat)
            if connection == (house2, house2.bat):
                connection = (house2, house1.bat)

        battery1, battery2 = house1.bat, house2.bat
        house1.bat, house2.bat = house2.bat, house1.bat

        return True

    def calculate_score(self):
        score = 0
        for connection in connections:
            score += calculate_distance(connection)
        return score

    def test(self, batteries):

        for battery in batteries:
            cap = 0
            for house in battery.links:
                cap += house.output
            if cap > battery.max_load:
                return battery

        return True

# hier maken we zo lekker sets van
