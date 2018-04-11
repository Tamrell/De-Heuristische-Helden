from imports import *
from connections import *
from random import shuffle, choice
import copy

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

    return c.calculate_score()




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
    best_score = 9999
    iterations = 0

    while iterations < 1000:
        score = connect_dem_random_ladies(grid)
        if score and score < best_score:
            best_grid = copy.deepcopy(grid)
            best_score = score
            print(best_score)
        Battery.color_generator = assign_color()
        grid = Grid(file1, file2)
        iterations += 1

    print(best_grid)
    print(best_score)

    # bat = grid.batteries[(3, 45)]
    # house = bat.find_closest_house(grid, grid.houses)
    # print(house)
