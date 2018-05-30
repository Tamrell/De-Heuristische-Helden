from Classes.house import House
from Classes.battery import Battery
import csv

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
    algorithms = {#'bb': ['branch & bound', branch_and_bound],
                  'r': ['Random Connect', random_sampler],
                  'b': ['battery cycler', battery_cycler],
                  'e': ['evaluate', evaluate_distribution],
                  'l': ['lower bound', lower_bound],
                  'u': ['upper bound', upper_bound],
                  #'a': ['A-smart', A_smart]
                  }
    return algorithms[alg][1](grid)
    return algorithms[alg][0]


def get_algorithm():
    """
        This function selects the first algorithm to run, i.e. finding a solution
        to run a secondary algorithm for.

        Takes:
            None

        Returns:
            string: user input resembling the algorithm to run
    """

    print("\n Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n p: Procrastinator")
    print(" lower: Worst (illegal?) Config Finder")
    print(" upper: best (illegal?) Config Finder")
    print(" d: Shortest Depthest First")
    print(" e: evaluator")
    print(" r: Random Connect")
    print(" a: A-smart")
    print(" b: Battery Cycler")
    print(" n: Plot the distribution of the random solution space")
    print(" h: Print Heatmap")
    print(" bb: Branch and bound\n")
    return input("(alpha): ")

def get_neighbourhood():
    """
        This function selects the neighbourhood to run algorithms for,
        depending on user input.

        Takes:
            None

        Returns:
            The number of the neighbourhood to run the algorithms for.
    """
    legal = {'1', '2', '3'}
    print("\n For which neighbourhood do you want to run an algorithm?")
    nbh = input("\n(int): ")

    # validity checking
    while not nbh in legal:
        print(nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n(int): ")
    return nbh
