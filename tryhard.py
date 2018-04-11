from imports import *
from connections import *
from bokeh.plotting import figure, show

def shortest_first(h_dict, grid):
    nordered = []
    houses = [h_dict[cord] for cord in h_dict if h_dict[cord].free]
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

def make_sure_them_bitches_be_fitting(h_dict, grid):
    houses = [h_dict[cord] for cord in h_dict if h_dict[cord].free]
    pass

def overload_them_bitches(grid):
    c = Connections()
    for h in grid.houses.values():
        b = h.find_closest_battery(grid)
        if not b:
            input(grid)
        c.connect(h, b, True)

def optimize_them_bitches(grid):
    # need to make sure everything is connected
    # then run hill climber for a time on a longest first.
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
    overload_them_bitches(grid)
    print(grid)
    # for i in range(10):
    #     for j in range(10):
    #         remove_them_inneficient_bitches(grid)
    #     connect_them_bitches(grid)
    print(grid)
    for b in grid.batteries.values():
        print(b.color, ":", b.load)

    x_h = []
    y_h = []
    x_b = []
    y_b = []
    for cord in grid.houses:
        x_h.append(cord[0])
        y_h.append(cord[1])
    for cord in grid.batteries:
        x_b.append(cord[0])
        y_b.append(cord[1])
    p = figure()
    p.cross(x=x_h, y=y_h)
    p.circle(x=x_b, y=y_b)
    show(p)
