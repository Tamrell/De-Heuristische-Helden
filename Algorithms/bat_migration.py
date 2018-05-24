from copy import deepcopy
import sys
import time
from Classes.grid import *
from Classes.battery import Battery
from Algorithms.hill_leaper import hill_leaper
from Algorithms.greedy_hillclimber import *
from Algorithms.Helpers.density_reset import *
from Algorithms.random_battery_cycler import *
from Algorithms.Helpers.bfcf import all_combos
from Results.Solspaces.plotter import *

def migration(grid, combo):
    it = len(combo)
    bats = []

    grid.batteries.clear()
    new_grid = deepcopy(grid)
    Battery.color_generator = assign_color()

    houses = [h for h in grid.houses.values()]
    reset_global_density(grid, houses)

    output_per_bat = grid.total_output() / it

    for bat in combo:
        sorted_list = sorted(grid.grid_list.values(), key=lambda x: x.rel_probability,
                             reverse=True)

        cap = bat[0]
        location = (sorted_list[0].x, sorted_list[0].y)
        bats.append(location)
        b = Battery(location, cap)
        grid.add_battery(b)

        while True:
            h = b.find_closest_house_max(grid, houses, output_per_bat)
            if not h:
                break
            connect(h, b, True)
            houses.remove(h)
        if houses:
            reset_global_density(grid, houses)

    reset_global_density(grid, grid.houses.values())
    sorted_list = sorted(bats, key=lambda x: grid.grid_list[x].probability)

    Battery.color_generator = assign_color()
    for bat, location in zip(combo, sorted_list):
        new_grid.batteries[location] = Battery(location, bat[0])

    grid.update(new_grid)
    for house in grid.houses.values():
        house.dists = {b: house.distance(house.cord, b.cord) for b in grid.batteries.values()}
