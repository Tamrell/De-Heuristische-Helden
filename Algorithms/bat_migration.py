import sys
import time
from copy import deepcopy
from Classes.grid import *
from Classes.battery import Battery
from Algorithms.hill_leaper import hill_leaper
from Algorithms.greedy_hillclimber import *
from Algorithms.Helpers.density_reset import *
from Algorithms.random_battery_cycler import *
from Algorithms.Helpers.bfcf import all_combos

def migration(grid, combo):
    """
        Goes through a combination of batteries. For each battery, it finds the
        most "locally dense" point on the grid, and places the battery there.
        It then finds the closest houses and connects until the capacity of an
        average battery (the total output of the houses divided by the number
        of batteries) is reached. Then the density is recalculated without
        taking the connected houses into account.

        Takes
            Grid: grid containing the houses that have to be connected later on

            List: A list of batteries (capacity, battery type) that will be
            placed on the Grid.

        Returns
            None
    """

    it = len(combo)
    bats = []

    grid.batteries.clear()
    new_grid = grid.copy()

    houses = [h for h in grid.houses.values()]
    set_local_density(grid, houses)

    output_per_bat = grid.total_output() / it

    for bat in combo:
        sorted_list = sorted(grid.grid_list.values(), key=lambda x: x.loc_probability,
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
