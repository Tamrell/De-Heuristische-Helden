from Classes.house import House
from Classes.battery import Battery
import csv
from Algorithms.Case_B.k_means import k_means
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Case_B.population_based import start_simulation
from Algorithms.Case_B.bat_migration import migration

from Algorithms.Case_A.greedy_hillclimber import greedy_hillclimber
from Algorithms.Case_A.random_connect import random_sampler
from Algorithms.Case_A.random_battery_cycler import battery_cycler, random_battery_cycler
from Algorithms.Helpers.density import *


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
        algorithms[alg[0]][1](grid, alg[1])


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
        print("\n <key>: <algorithm>")
        print(" m: Bat Migration")
        print(" k: K-Means")
        print(" p: Population Based\n")
        while alg not in ['m', 'k', 'p']:
            alg = input(' [m / k / p]: ')
    it = ''
    print("\n How many iterations of battery cycling would you like to run?")
    while not it:
        userInput = input(' (int): ')
        try:
            it = int(userInput)
        except ValueError:
            print(" That's not an integer \n")

    if case is 'a':
        return(alg, it)
    else:
        random = input("\n Random combination or all possible combinations?\n [r/a]: ")
        while random not in ['a', 'r']:
            random = input(" Only r or a\n [r/a]: ")
        return alg, it, random


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
