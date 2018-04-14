from imports import *
from connections import *
from plots import *
from random import choice

def shortest_first(h_dict, grid):
    nordered = []
    houses = [h for h in h_dict.values() if h.free]
    for h in houses:
        b = h.find_closest_battery(grid)
        if b:
            d = grid.distance(h.cord, b.cord)
            nordered.append((d, h, b))
    return [(con[1], con[2]) for con in sorted(nordered)]

def remove_them_inneficient_bitches(grid):
    c = Connections()
    for battery in grid.batteries.values():
        c.unconnect(battery.find_furthest_house(grid))

def connect_them_bitches(grid, swap=True):
    c = Connections()
    cons = True
    while cons:
        cons = shortest_first(grid.houses, grid)
        still_good = True
        i = 0
        while still_good and i < len(cons):
            still_good = c.connect(cons[i][0], cons[i][1])
            i += 1
    print(grid.score())
    # while c.rand_swapper(grid) and swap:
    #     connect_them_bitches(grid, False)
    print(grid.score())

def make_sure_them_bitches_be_fitting(h_dict, grid):
    houses = [h for h in h_dict.values() if h.free]
    c = Connections()
    for h in houses:
        print(h.output)
        needed = -20 * h.output 
        candidates = sorted([(h2.output, h2) for h2 in grid.houses.values()
                            if not h2.free])
        for candidate in candidates:
            if needed < 0:
                needed += candidate[1].output
                c.unconnect(candidate[1])
        c.connect(h, h.find_closest_battery(grid))
        return True
        # for candidate in furthest:
        #     if h.output - candidate.output >= needed:
        #         c.unconnect(candidate)
        #         c.connect(h, bat)
        #         return True
    return False

def overload_them_bitches(grid):
    c = Connections()
    for h in grid.houses.values():
        b = h.find_closest_battery(grid, True)
        if not b:
            input(grid)
        c.connect(h, b, True)
    print(c.calculate_score())

def optimize_them_overloaded_bitches(grid):
    # for each underloaded battery, search for the most profitable switch in  house
    # connected to an overloaded battery, and switch the connection
    # most profitable: maybe closest house of an overloaded battery, maybe least increasement of length.

    cheapest = 30 ###### what measure do we use? the smallest?
    for b in grid.batteries.values():
        while b.fits(cheapest):
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
    while make_sure_them_bitches_be_fitting(grid.houses, grid):
        connect_them_bitches(grid)
    # for i in range(10):
    #     for j in range(10):
    #         remove_them_inneficient_bitches(grid)
    #     connect_them_bitches(grid)
    print(grid)
    for b in grid.batteries.values():
        print(b.color, ":", b.load, "of", b.max_load)
    hover_plot(grid)
