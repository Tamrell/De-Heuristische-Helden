from imports import *
from connections import *
from plots import *
from random import choice

def overload_them_bitches(grid):
    c = Connections()
    for h in grid.houses.values():
        b = h.find_closest_battery(grid, True)
        if not b:
            input(grid)
        c.connect(h, b, True)
    print(c.calculate_score())

def correct_them_overloaded_bitches(grid):
    # for each underloaded battery, search for the most profitable switch in  house
    # connected to an overloaded battery, and switch the connection
    # most profitable: maybe closest house of an overloaded battery, maybe least increasement of length.
    b = max([(b.load, b) for b in grid.batteries.values()])
    while not b.fits():
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
    c = Connections()
    c.ex_swapper(grid)

    print(grid)
    b_count = 0
    for b in grid.batteries.values():
        b_count += b.max_load
        print(b.color, ":", b.load, "of", b.max_load)
    count = 0
    h_count = 0
    for h in grid.houses.values():
        count += h.output
        h_count += 1
    print(grid.score())
    print("total houses:", h_count)
    print("total output:", count)
    print("average output:", count/h_count)
    print("total capacity:", b_count)
    hover_plot(grid)
