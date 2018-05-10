from random import choice, randint
from Algorithms.random_weight_lifter import random_weight_lifter
from Algorithms.evaluate_distribution import evaluate_distribution

def start_simulation(grid):
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
    generations =
    random_weight_lifter(grid)
    evaluate_distribution(grid)
