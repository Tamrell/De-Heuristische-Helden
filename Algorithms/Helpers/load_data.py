import csv
from random import choice
import copy

from Classes.house import House
from Classes.battery import Battery

from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.bat_propagation import start_simulation
from Algorithms.Case_B.bat_migration import migration

from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber
from Algorithms.Case_A.random_connect import random_sampler
from Algorithms.Case_A.random_battery_cycler import battery_cycler, random_battery_cycler

from Algorithms.Helpers.density import *
from Algorithms.Helpers.bfcf import all_combos

def get_houses(data):
    '''
        Takes a .csv file and add the houses in the file to a
        dictionary with coordinate(tuple): house(House) as key: value.

        Args:
            file: A csv file containing the information about the houses,
            one house per row. Each row contains (in order): x-coordinate,
            y-coordinate, maximum capacity.
    '''
    houses = {}
    with open(data, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            cord, output = (int(row[0]), int(row[1])), float(row[2])
            houses[cord] = House(cord, output)
    return houses


def get_batteries(data):
    '''
        Takes a .csv file and adds the batteries in the file to a
        dictionary with coordinate(tuple): battery(Battery) as key: value.

        Args:
            file: A csv file containing the information about the houses,
            one house per row. Each row contains (in order): x-coordinate,
            y-coordinate, maximum capacity.
    '''
    batteries = []
    with open(data) as f:
        lines = csv.reader(f, delimiter = ",")
        next(lines)
        for line in lines:
            location, capacity = (int(line[0]), int(line[1])), float(line[2])
            batteries.append(Battery(location, capacity))
    return batteries

def run_algorithm(alg, grid):
    """
        The function run_algorithm(alg, grid) calls one of the primary algorithms,
        depending on the parameter alg.
        Takes:
            alg: string representing the algorithm to run
            grid: grid.Grid object to hand to the selected algorithms
        Returns:
            return name of selected algorithm
    """
    algorithms = {
                  'r': ['Random Connect', random_sampler],
                  'b': ['Battery Cycler', battery_cycler],
                  'h': ['Heatmap', print_heatmap],
                  'm': ['Migration', migration],
                  'k': ['K-Means', k_means],
                  'p': ['Bat Propagation', start_simulation]
                 }
    if len(alg) is 1:
        algorithms[alg][1](grid)

    elif len(alg) is 2:
        if type(alg[1]) is int:
            if alg[0] is 'b':
                algorithms[alg[0]][1](grid, alg[1])
            elif alg[0] is 'k':
                random_bat_config(grid)
                algorithms[alg[0]][1](grid)
                random_battery_cycler(grid, alg[1])
            else:
                algorithms[alg[0]][1](grid)
                random_battery_cycler(grid, alg[1])

        elif type(alg[1]) is str:
            results = []
            combos = all_combos(grid)
            combos = list(combos)
            for i in range(5):
                algorithms[alg[0]][1](grid, combos[i])
                results.append(battery_cycler(grid))
                grid.reset()
            best = min(results)
            combo = combos[results.index(best)]
            algorithms[alg[0]][1](grid, combo)
            print("\n The best combination found was:\n\n", combo)
            print("\n With a score of: ", best)
            print("\n Would you like to run more battery cycle iterations with this combo?")
            if input(" y/n? ") is 'y':
                print("\n For how many iterations?")
                i = ''
                while not i:
                    userInput = input(' (int): ')
                    try:
                        i = int(userInput)
                    except ValueError:
                        print(" That's not an integer \n")
                random_battery_cycler(grid, i)
                for bat in grid.batteries.values():
                    move_to_middle(grid, bat)

    else:
        combos = all_combos(grid)
        if alg[2] is 'r':
            combo = choice(list(combos))
            algorithms[alg[0]][1](grid, combo)
            random_battery_cycler(grid, alg[1])
            for bat in grid.batteries.values():
                move_to_middle(grid, bat)


def get_algorithm(case):
    """
    This function selects the algorithm to run.

    Takes:
        None

    Returns:
        string: user input resembling the algorithm to run
    """
    alg = ''
    print("\n Which algorithm do you want to run?")
    if case is 'a':
        print("\n <key>: <algorithm>")
        print(" r: Random Connect")
        print(" b: Battery Cycler")
        print(" h: Print Heatmap\n")
        while alg not in ['r', 'b', 'h']:
            alg = input(' [r / b / h]: ')
        if alg is not 'b':
            return alg
        else:
            it = ''
            print("\n How many iterations of battery cycling would you like to run?")
            while not it:
                userInput = input(' (int): ')
                try:
                    it = int(userInput)
                except ValueError:
                    print(" That's not an integer \n")
            return(alg, it)

    else:
        print("\n <key>: <algorithm>")
        print(" m: Bat Migration")
        print(" k: K-Means")
        print(" p: Population Based\n")
        while alg not in ['m', 'k', 'p']:
            alg = input(' [m / k / p]: ')
        if alg is not 'm':
            it = ''
            print("\n How many iterations of battery cycling would you like to run?")
            while not it:
                userInput = input(' (int): ')
                try:
                    it = int(userInput)
                except ValueError:
                    print(" That's not an integer \n")
            return alg, it

        random = input("\n Random combination or all possible combinations?\n [r/a]: ")
        while random not in ['a', 'r']:
            random = input(" Only r or a\n [r/a]: ")
        if random is 'r':
            it = ''
            print("\n How many iterations of battery cycling would you like to run?")
            while not it:
                userInput = input(' (int): ')
                try:
                    it = int(userInput)
                except ValueError:
                    print(" That's not an integer \n")
            return alg, it, random
        return alg, random

def get_neighbourhood():
    """
        This function selects the neighbourhood to run algorithms for, depending
        on user input.
        Takes:
            None
        Returns:
            The number of the neighbourhood to run the algorithms for.
    """

    legal = {'1', '2', '3'}
    print("\n For which neighbourhood do you want to run an algorithm?")
    nbh = input(" (int): ")

    # validity checking
    while not nbh in legal:
        print(" ", nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n (int): ")
    return nbh
