from imports import *
from connections import *
from plots import *
from random import choice

def least_cost_first(grid):
    count = 0
    h_count = 0
    for h in grid.houses.values():
        count += h.output
        h_count += 1
    print(h_count)
    a_o = count/h_count
    nordered = []
    houses = [h for h in grid.houses.values() if h.free]
    for h in houses:
        b = h.find_closest_battery(grid)
        if b:
            d = grid.distance(h.cord, b.cord) + 2 * ((b.max_load - b.load - h.output) % a_o) # 50 = average output
            nordered.append((d, h, b))
    return [(con[1], con[2]) for con in sorted(nordered)]

def connect_them_bitches(grid, swap=True):
    c = Connections()
    cons = True
    while cons:
        cons = least_cost_first(grid)
        still_good = True
        i = 0
        while still_good and i < len(cons):
            still_good = c.connect(cons[i][0], cons[i][1])
            i += 1
    print(grid.score())
    while swap and c.rand_swapper(grid):
        connect_them_bitches(grid, False)
    print(grid.score())
    # if [h for h in grid.houses.values() if h.free]:
    #     for h in grid.houses.values():
    #         if h.free:
    #             print(h.cord , h.color)
    #     input("Failed to connect all houses")

def fitting(grid):
    houses = [h for h in grid.houses.values() if h.free]
    c = Connections()
    for h in houses:
        print(h.output)
        b = min((b.load, b) for b in grid.batteries.values())[1]
        needed = 2 * h.output
        candidates = sorted([(h2.output, h2) for h2 in b.links])
        for candidate in candidates:
            if needed > 0:
                needed -= candidate[1].output
                c.unconnect(candidate[1])
        c.connect(h, b)
        connect_them_bitches(grid)
        return True
        # for candidate in furthest:
        #     if h.output - candidate.output >= needed:
        #         c.unconnect(candidate)
        #         c.connect(h, bat)
        #         return True
    return False
if __name__ == "__main__":

    best = (100000, None)

    while best[0] > 3517:
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
        check = set()
        loop = 0
        br = True
        while [h for h in grid.houses.values() if h.free]:
            if loop > 10:
                br = False
                break
            loop += 1
            # if tuple([h for h in grid.houses.values() if h.free]) in check:
            #     print("U fook up loop")
            #     exit(1)
            check.add(tuple([h for h in grid.houses.values() if h.free]))
            connect_them_bitches(grid)
            fitting(grid)
        connect_them_bitches(grid)
        c = Connections()
        if br:
            if [h for h in grid.houses.values() if h.free]:
                input('welp')
            c.ex_swapper(grid)
            #while make_sure_them_bitches_be_fitting(grid.houses, grid):
            #    connect_them_bitches(grid)
            # for i in range(10):
            #     for j in range(10):
            #         remove_them_inneficient_bitches(grid)
            #     connect_them_bitches(grid)
            print(grid)
            print(grid.score())
            for b in grid.batteries.values():
                print(b.color, ":", b.load, "of", b.max_load)
            if grid.score() < best[0]:
                best = (grid.score(), grid)
        Battery.color_generator = assign_color()
    print(best[0])
    hover_plot(best[1])
