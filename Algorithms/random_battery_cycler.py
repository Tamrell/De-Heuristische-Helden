from random import shuffle, choice, sample
from copy import deepcopy
from Algorithms.contest import *

def random_battery_cycler(grid):
    print("How many iterations do you want to run?")
    iterations = int(input("(int): "))
    best = (float("inf"), None)

    while iterations:
        houses = [h for h in grid.houses.values()]
        batteries = [b for b in grid.batteries.values()]
        while houses and batteries:
            b = choice(batteries)
            h = b.find_closest_house(grid, houses)
            if h:
                connect(h, b)
                houses.remove(h)
            else:
                batteries.remove(b)
        if grid.legal() and grid.score() < best[0]:
            best = (grid.score(), deepcopy(grid))
        iterations -= 1
        grid.reset()
    if best[1]:
        grid.update(best[1])
