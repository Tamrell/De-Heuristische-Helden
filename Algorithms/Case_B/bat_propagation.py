from Classes.grid import Grid
from Algorithms.Case_A.random_battery_cycler import battery_cycler
from Algorithms.Case_B.random_bat_config import random_bat_config
from Algorithms.Helpers.bounds import get_bound
from random import choice
from multiprocessing import Pool
import time
import statistics


def start_simulation(grid, p_size=20, batteries=[], generations=5):
    """
        Generates a random starting population using the random_bat_config,
        then uses the heuristic function to select the first fittest individual

        Takes
            Grid: grid containing the houses that have to be connected later on
            Int(optional): population size
            List(optional): list containing starting batteries
            Int(optional): number of generations

        Returns
            None
    """
    population = let_there_be_life_exclamation_mark(grid, p_size, batteries)
    for i in range(generations):
        print("\n\nGeneration:\t",i)
        fittest, score = population[0][1], population[0][0]
        population = sorted(new_generation(fittest, score, p_size))
    return population[0][1]


def new_generation(fittest, score, p_size):
    """
        Generates a new population of size p_size based on the fittest
        individual.

        Takes
            Grid: individual containing the batteries and houses
            Int: score of the fittest individual
            int: population size

        Returns
            list: list containing the new population
    """
    population = []
    for i in range(p_size):
        child = mutated(fittest)
        population.append((fitness(child), child))

    # add parent as well
    population.append((score, fittest))
    return population



def let_there_be_life_exclamation_mark(grid, p_size, batteries):
    """
        Generates a random starting population of size p_size.

        Takes
            Grid: grid containing the batteries and houses
            int: population size
            List(optional): list containing starting batteries

        Returns
            list: list containing the population
    """
    population = []
    for i in range(p_size):
        individual = Grid(grid.nbh, grid.houses)
        random_bat_config(individual, batteries)
        population.append([fitness(individual), individual])
    return sorted(population)


def fitness(grid, fit_measure=battery_cycler):
    '''
        Calculates the fitness of a given grid as a function of its total cost.
        The fitness is decided by taking the average of i_size
        battery cycler runs.

        Takes
            Grid: grid containing the batteries and houses
            Function: fitness function

        Returns
            int: fitness of the grid
    '''
    i_size = 5
    score_list = []
    with Pool(processes=5) as p:
        score_list = p.map(fit_measure, [grid for i in range(i_size)])
    return sum(score_list)/len(score_list)


def mutated(parent):
    """
        Returns a randomly mutated child based on the parent

        Takes
            Grid: parent containing the batteries and houses

        Returns
            Grid: randomly mutated child of the input individual
    """
    child = parent.copy()
    mutate_battery_location(child)
    return child


def mutate_battery_location(individual):
    '''randomly mutates the location of a random battery'''
    battery = choice([b for b in individual.batteries.values()])
    new_location = choice([(x, y) for x in range(individual.x_dim)
                                  for y in range(individual.y_dim)
                                  if not (x, y) in individual.houses
                                  if not (x, y) in individual.batteries])
    individual.move_battery(battery, new_location, linked_only=False)
