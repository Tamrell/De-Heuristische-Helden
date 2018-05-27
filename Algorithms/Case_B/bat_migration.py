import sys
import time
from copy import deepcopy
from Classes.grid import Grid
from Classes.battery import Battery
from Algorithms.Case_A.greedy_hillclimber import *
from Algorithms.Helpers.density_reset import *
from Algorithms.random_battery_cycler import *
from Algorithms.Helpers.bfcf import all_combos
from Results.Solspaces.plotter import *

def migration(grid, combo):
    it = len(combo)
    bats = []

    grid.batteries.clear()
    new_grid = grid.copy()

    houses = [h for h in grid.houses.values()]
    set_local_density(grid, houses)

    output_per_bat = grid.total_output() / it

    for bat in combo:
        sorted_list = sorted(grid.grid_list.values(), key=lambda x: x.rel_probability,
                             reverse=True)

        location = (sorted_list[0].x, sorted_list[0].y)
        bats.append(location)
        b = Battery(location, bat[0])
        grid.add_battery(b)

        while True:
            h = b.find_closest_house_max(grid, houses, output_per_bat)
            if not h:
                break
            connect(h, b, True)
            houses.remove(h)
        if houses:
            set_local_density(grid, houses)

    set_global_density(grid, grid.houses.values())
    sorted_list = sorted(bats, key=lambda x: grid.grid_list[x].probability)

    Battery.color_generator = assign_color()

    grid.update(new_grid)
    for bat, location in zip(combo, sorted_list):
        grid.add_battery(Battery(location, bat[0], bat[1]))
