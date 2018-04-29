from contest import *
from plots import *
from random import choice

def shortest_first(grid):

    nordered = []
    houses = [h for h in grid.houses.values() if h.free]
    for h in houses:
        b = h.find_closest_battery(grid)
        if b:
            d = grid.distance(h.cord, b.cord)
            nordered.append((d, h, b))
        else:
            print(grid)
            input('y u no work?')
    return [(con[1], con[2]) for con in sorted(nordered)]

def remove_them_inneficient_bitches(grid):
    for battery in grid.batteries.values():
        unconnect(battery.find_furthest_house(grid))

def connect_them_bitches(grid, swap=True):
    cons = True
    while cons:
        cons = shortest_first(grid.houses, grid)
        still_good = True
        i = 0
        while still_good and i < len(cons):
            still_good = connect(cons[i][0], cons[i][1])
            i += 1
    print(grid.score())

def make_sure_them_bitches_be_fitting(h_dict, grid):
    houses = [h for h in h_dict.values() if h.free]
    for h in houses:
        print(h.output)
        needed = -20 * h.output
        candidates = sorted([(h2.output, h2) for h2 in grid.houses.values()
                            if not h2.free])
        for candidate in candidates:
            if needed < 0:
                needed += candidate[1].output
                unconnect(candidate[1])
        c.connect(h, h.find_closest_battery(grid))
        return True
    return False

def last_fits(grid):
    houses = [h for h in grid.houses.values() if h.free] # in 1 regel?
    f_houses = [h for h in grid.houses.values() if not h.free] # in 1 regel?
    batteries = {b for b in grid.batteries.values()}
    for h in houses:
        pass


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
    connect_them_bitches(grid)
    grid.stats
    hover_plot(grid)