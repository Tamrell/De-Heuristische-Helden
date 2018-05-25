from Algorithms.random_battery_cycler import battery_cycler
from Algorithms.random_bat_config import random_bat_config
from Classes.grid import Grid
import os

def start_recording(nbh):
    for i in range(int(input("range?: "))):
        grid = Grid('Data/wijk' + nbh + '_huizen.csv', None, nbh)
        print(grid)
        random_bat_config(grid)
        battery_cycler(grid, 5)
        add_data(grid.score(), nbh)


def add_data(score, nbh):
    filename =  os.path.abspath('Results/Solspaces/SSB' + nbh +'.csv')
    with open(filename, 'a') as data:
        data.write(str(score) + '\n')
