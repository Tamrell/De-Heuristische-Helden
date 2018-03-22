# C:\Users\Eigenaar\Documents\school\Thema 2\De-Heuristische-Helden\De-Heuristische-Helden
class Connections:
    def __init__(self):
        self.connections=[]

    def show_connections(self):
        sorted_connections = sorted(self.connections)
        for connection in sorted_connections:
            house, battery = connection
            print(house.cord, battery.cord)

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
        battery1, battery2 = house1.bat, house2.bat
        house1.bat, house2.bat = house2.bat, house1.bat
        # shit bijhouden in eigen lijst

    def calculate_score(self):
        pass
