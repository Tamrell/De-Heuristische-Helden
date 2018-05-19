from random import choice, randint
from Classes.grid import Grid
from Algorithms.random_weight_lifter import random_weight_lifter
from Algorithms.random_battery_cycler import battery_cycler
from tqdm import tqdm

def start_simulation(grid, p_size=10, generations=10):
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
        fittest = population[0]
        population = new_generation(fittest)


    for i in population:
        print(i[0])

    #evaluate_distribution(grid)

def new_generation(fittest, p_size):
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
    for i in range(p_size):
        population.append(mutated(fittest))



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
    i_size = 1
    score = 0
    for i in range(i_size):
        score += battery_cycler(grid)
        grid.reset()
    return score/i_size


def mutated(parent):
    """
        Returns a randomly mutated child based on the parent

        Takes
            Grid: parent containing the batteries and houses

        Returns
            Grid: randomly mutated child of the input individual
    """
    child = Grid(parent.file1, None, parent.nbh)

    # Randomly choose type of mutation
    option = randint(0, 100)

    if option <= 25:
        pass
        #mutate_battery_type(child)

    elif option <= 50:
        pass
        #mutate_battery_location(child)

    elif option <= 75:
        pass
        #mutate_add_battery(child)

    else:
        pass
        #mutate_remove_battery(child)
