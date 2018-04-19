from imports import *
from connections import *
from random import shuffle, choice, sample
import copy
from plots import *

def connect_dem_classy_ladies(grid):

    houses = grid.houses
    house_list = [cord for cord in houses]
    batteries = grid.batteries
    battery_list = [cord for cord in batteries]
    c = Connections()

    while house_list:
        if not battery_list:
            return False
        shuffle(battery_list)
        for b in battery_list:
            if house_list is []:
                return True
            h = batteries[b].find_closest_house(grid, house_list)
            if h == ():
                battery_list.remove(b)
                break
            if not c.connect(houses[h], batteries[b]):
                return False
            house_list.remove(h)


def connect_dem_random_ladies(grid):
    houses = grid.houses
    house_list = [cord for cord in houses]
    batteries = grid.batteries
    battery_list = [cord for cord in batteries]
    c = Connections()

    while house_list:
        if not battery_list:
            return False
        b = choice(battery_list)
        h = batteries[b].find_closest_house(grid, house_list)
        if h == ():
            battery_list.remove(b)
            continue
        if not c.connect(houses[h], batteries[b]):
            return False
        house_list.remove(h)

    return c


def hillclimb_the_ladies(grid, c):

    best_score = c.calculate_score()
    houses = grid.houses
    iterations = 0

    while iterations < 100:
        [h1, h2] = sample(list(houses), 2)
        c.swap_connection(houses[h1], houses[h2])
        if c.test() is not True or c.calculate_score() > best_score:
            c.swap_connection(houses[h1], houses[h2])
            iterations += 1
            continue
        best_score = c.calculate_score
        print(best_score)
        iterations += 1

if __name__ == "__main__":

    file1 = sys.argv[1]
    if file1 == '1':
        file1 = 'Data/wijk1_huizen.csv'
    elif file1 == '2':
        file1 = 'Data/wijk2_huizen.csv'
    elif file1 == '3':
        file1 = 'Data/wijk3_huizen.csv'

    file2 = sys.argv[1]
    if file2 == '1':
        file2 = 'Data/wijk1_batterijen.txt'
    elif file2 == '2':
        file2 = 'Data/wijk2_batterijen.txt'
    elif file2 == '3':
        file2 = 'Data/wijk3_batterijen.txt'

    grid = Grid(file1, file2)
    houses = grid.houses.values()
    print(len(houses))
    best_score = 9999
    iterations = 0

    while iterations < 10000:
        c = connect_dem_random_ladies(grid)
        if c:
            score = c.calculate_score()
        if c and score < best_score:
            best_grid = copy.deepcopy(grid)
            best_score = score
            best_c = copy.deepcopy(c)
            print(best_score)
        Battery.color_generator = assign_color()
        grid = Grid(file1, file2)
        iterations += 1


    print(best_grid)
    print(best_grid.score())
    hover_plot(best_grid)
