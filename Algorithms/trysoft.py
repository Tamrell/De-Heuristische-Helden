from random import shuffle, choice, sample
from copy import deepcopy
from Algorithms.contest import *

def connect_dem_classy_ladies(grid):

    houses = grid.houses
    house_list = [cord for cord in houses]
    batteries = grid.batteries
    battery_list = [cord for cord in batteries]

    while house_list:
        if not battery_list:
            return False
        shuffle(battery_list)
        for b in battery_list:
            if house_list is []:
                return True
            h = batteries[b].find_closest_house(grid, house_list)
            if h == ():
                battery_list.remove(b)
                break
            if not connect(houses[h], batteries[b]):
                return False
            house_list.remove(h)


def random_battery_cycler(grid, max_it):

    best_score = 99999
    max_it = int(max_it)
    i = 0

    while i < max_it:
        house_list = [cord for cord in grid.houses]
        battery_list = [cord for cord in grid.batteries]
        while house_list:
            if not battery_list:
                break
            b = choice(battery_list)
            h = grid.batteries[b].find_closest_house(grid, house_list)
            if h == ():
                battery_list.remove(b)
                continue
            if not connect(grid.houses[h], grid.batteries[b]):
                break
            house_list.remove(h)
        if not house_list:
            score = grid.score()
            if score < best_score:
                best_grid = deepcopy(grid)
                best_score = score
        i += 1
        grid.reset(report=False)
    grid = deepcopy(best_grid)
    return grid
