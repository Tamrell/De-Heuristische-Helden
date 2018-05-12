from random import choice, randint
from copy import deepcopy
from Classes.battery import Battery

def choose_batteries(grid):
    """This function makes a random combination of batteries which have
       a summed capacity that exceeds the sum of all the houses' output.

    Takes
        Grid: grid containing the houses that have to be connected later on

    Returns
        List: list containing tuples: (capacity, battery_type)
    """
    all_batteries = [(450, 'Powerstar'),
                     (900, 'Imerse-II'),
                     (1800, 'Imerse-III')]
    chosen_batteries = []
    needed_capacity = grid.total_output()

    # Add random batteries until needed capacity is surpassed.
    while needed_capacity > 0:
        chosen_batteries.append(choice(all_batteries))
        needed_capacity -= chosen_batteries[-1][0]
    return chosen_batteries

def choose_coordinates(grid, batteries):
    """This function generates a legal random combination of coordinates
       for a corresponding list of battery information.

    Takes
        Grid: grid containing the houses that have to be connected later on
        List: list containing (output, battery_type) tuples

    Returns
        Set: set containing tuples: (x_coordinate, y_coordinate)
    """
    coordinates = set()
    available_coordinates = [(x, y) for x in range(grid.x_dim)
                                    for y in range(grid.y_dim)
                                    if not (x, y) in grid.houses]
    while len(coordinates) < len(batteries):
        coordinates.add(choice(available_coordinates))
    return coordinates

def random_weight_lifter(grid):
    """This function generates a random combination of batteries that have
       a bigger sum of capacity than the total output of all the houses so
       that it can 'lift' their 'weight' and puts the batteries on random
       available locations in the grid.

    Takes
        Grid: grid containing the houses that have to be connected later on

    Returns
        None
    """
    batteries = choose_batteries(grid)
    coordinates = choose_coordinates(grid, batteries)
    for capacity, name in batteries:
        grid.add_battery(Battery(coordinates.pop(), capacity, name))
    grid.initial_batteries = deepcopy(grid.batteries)
