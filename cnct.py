from grid import *
from house import *
from load_batteries import *
from battery import *
from connections import *
import random

house_file = 'Data/wijk1_huizen.csv'
battery_file = 'Data/wijk1_batterijen.txt'

grid = Grid(house_file)
grid.set_batteries(battery_file)
connections = Connections()
houses = grid.houses
batteries = grid.batteries

for coord in houses:
    battery = houses[coord].find_closest_battery(grid)
    connections.connect(houses[coord], batteries[battery])
    while connections.test() is not True:
        connections.disconnect(houses[coord])
