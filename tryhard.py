from imports import *
from connections import *
# init grid
# create a list with all houses and their distance to all batteries,
# sort the list on shortest distances
# try to connect them all
# make new list with leftover houses and their distance to non-overloaded battery

def shortest_first(h_dict, grid):
    nordered = []
    houses = [h_dict[cord] for cord in h_dict if h_dict[cord].free]
    for h in houses:
        b = h.find_closest_battery(grid)
        if b:
            d = grid.distance(h.cord, b.cord)
            nordered.append((d, h, b))
    return [(con[1], con[2]) for con in sorted(nordered)]

def connect_them_bitches(grid):
    c = Connections()
    cons = True
    while cons:
        cons = shortest_first(grid.houses, grid)
        still_good = True
        i = 0
        while still_good and i < len(cons):
            still_good = c.connect(cons[i][0], cons[i][1])
            i += 1

def optimize_them_bitches(grid):
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

    print(grid)