from random import choice, randint
from Classes.grid import Grid
from Algorithms.random_weight_lifter import random_weight_lifter
from Algorithms.random_battery_cycler import battery_cycler
from tqdm import tqdm
from multiprocessing import Pool
import time

def start_simulation(grid, p_size=20, generations=10):
    """
        Generates a random starting population using the weight lifter,
        then either?????:
        - creates offspring with mutations varying in severity based on
          the 'fitness' of the individual
        - creates a bigger amount of offspring off of individuals with a
          higher 'fitness' and vice versa a lower amount for low fitness
          (in percentages? keeping each generation to 20 individuals??)

        continues untill stopped, then yields information???
        //
        or saves data in .csv files???

        Takes
            Grid: grid containing the houses that have to be connected later on

        Returns
            None
    """
    # individual = list of batteries with their location?
    #for _ in range(gen_size):
    #    create_individual(grid)
    #generations = []
    genetic_history = []
    population = let_there_be_life_exclamation_mark(grid, p_size)
    genetic_history.append(population)
    for i in range(generations):

        # New population will consist of the fittest individual and mutations
        # of it.
        # for j in population:
        #     print(i, j[0])
        fittest, score = population[0][1], population[0][0]
        print(fittest, score)
        population = sorted(new_generation(fittest, score, p_size))
        genetic_history.append(population)

    for i, p in enumerate(genetic_history):
        print("generation:", i)
        print("fittest:", p[0][0])
        print("average:", sum([g[0] for g in p])/len(p), "\n\n")

    #evaluate_distribution(grid)

def new_generation(fittest, score, p_size):
    """
        Generates a new population of size p_size based on the fittest
        individual.

        Takes
            Grid: individual containing the batteries and houses
            int: population size

        Returns
            list: list containing the new population
    """
    population = []
    for i in tqdm(range(p_size)):
        child = mutated(fittest)
        population.append((fitness(child), child))
    # add parent
    population.append((score, fittest))
    return population



def let_there_be_life_exclamation_mark(grid, p_size):
    """
        Generates a random starting population of size p_size.

        Takes
            Grid: grid containing the batteries and houses
            int: population size

        Returns
            list: list containing the population
    """
    population = []
    for i in tqdm(range(p_size)):
        individual = Grid(grid.file1, None, grid.nbh)
        random_weight_lifter(individual)
        population.append([fitness(individual), individual])
    return sorted(population)

def fitness(grid):
    '''
        Calculates the fitness of a given grid as a function of its total cost.
        The fitness is decided by taking the average of i_size
        battery cycler runs.

        Takes
            Grid: grid containing the batteries and houses

        Returns
            int: fitness of the grid
    '''
    i_size = 10
    with Pool(processes=6) as p:
        score_list = p.map(battery_cycler, [grid for i in range(i_size)])
        grid.reset()
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
    # Randomly choose type of mutation
    option = randint(0, 100)

    if option <= 25:
        pass
        #mutate_battery_type(child)

    elif option <= 50:
        pass

    elif option <= 75:
        pass
        #mutate_add_battery(child)

    else:
        pass
        #mutate_remove_battery(child)
    mutate_battery_location(child)
    return child

def mutate_battery_location(individual):
    battery = choice([b for b in individual.batteries.values()])
    new_location = choice([(x, y) for x in range(individual.x_dim)
                                  for y in range(individual.y_dim)
                                  if not (x, y) in individual.houses
                                  if not (x, y) in individual.batteries])
    individual.move_battery(battery, new_location)

def mutate_battery_type(individual):
    battery = choice([b for b in individual.batteries.values()])
