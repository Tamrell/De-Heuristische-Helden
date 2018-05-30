from random import shuffle, choice, sample
from copy import deepcopy
from Algorithms.Helpers.connect import connect
from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber

def random_battery_cycler(grid, solutions):
    '''
        Picks a random battery from the grid, finds the closest unlinked house that
        would not overcharge the battery, and connects to the house. If no houses
        are available, battery is removed from the options. Continues until no
        batteries (illegal grid) or houses (solution) are left. If a solution is
        found, a greedy hillclimber is applied to the grid. Saves best config
        and updates grid to this config.

        Takes
            Grid: grid containing the houses and batteries to be connected

            solutions: Number of legal solutions to find before exiting.

        Returns
            None
    '''
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
        grid.light_reset()
    if best[1]:
        grid.update(best[1])

def battery_cycler(grid, s=1):
    '''
        Starts the Random Battery Cycler for s solutions.

        Takes
            Grid: grid containing the houses and batteries to be connected

            solutions: Number of legal solutions to find before exiting.

        Returns
            None
    '''
    random_battery_cycler(grid, s)
    return grid.score()
