from random import choice, randint
import copy
from Classes.battery import Battery
from Algorithms.evaluate_distribution import evaluate_distribution

def choose_batteries(grid):
    all_batteries = [(450, 'Powerstar'),
                     (900, 'Imerse-II'),
                     (1800, 'Imerse-III')]
    chosen_batteries = []
    needed_capacity = grid.total_output() + 500

    # Add random batteries until minimum capacity is reached
    while needed_capacity > 0:
        chosen_batteries.append(choice(all_batteries))
        needed_capacity -= chosen_batteries[-1][0]
    return chosen_batteries

def choose_coordinates(grid, batteries):
    coordinates = set()
    available_coordinates = [(x, y) for x in range(grid.x_dim)
                                    for y in range(grid.y_dim)
                                    if not (x, y) in grid.houses]
    while len(coordinates) < len(batteries):
        coordinates.add(choice(available_coordinates))
    return coordinates

def start_simulation(grid):
    batteries = choose_batteries(grid)
    coordinates = choose_coordinates(grid, batteries)
    for capacity, name in batteries:
        grid.add_battery(Battery(coordinates.pop(), capacity, name))
    grid.initial_batteries = copy.deepcopy(grid.batteries)
    print(grid)
    evaluate_distribution(grid)
