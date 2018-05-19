from random import shuffle, choice, sample
from copy import deepcopy
from Algorithms.Helpers.connect import connect
from Algorithms.greedy_hillclimber import greedy_hillclimber

def random_battery_cycler(grid, solutions):
    '''The random battery cycler '''

    best = (float("inf"), None)
    while solutions:
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
        if grid.legal():
            greedy_hillclimber(grid)
            if grid.score() < best[0]:
                best = (grid.score(), deepcopy(grid))
            solutions -= 1
        grid.reset()
    if best[1]:
        grid.update(best[1])

def battery_cycler(grid, s=False):
    if s:
        print("How many solutions do you want to run?\n")
        solutions = int(input("(int): "))
    else:
        solutions = 1
    random_battery_cycler(grid, solutions)
    return grid.score()
