from contest import *
from plots import *

def procrastinate(grid):
    for h in grid.houses.values():
        b = h.find_closest_battery(grid, True)
        connect(h, b, True)

def reluctantly_sort_it_out(grid):
    pass

def best_fit(grid):
    # for all connections, connect the one with the least cost that causes the
    # deficiency score to go down until the grid is legal.
    pass

def defficiency_score(grid):
    # calculates how inefficient all the batteries are used.
    deff = 0
    for b in grid.values():
        deff += abs(b.max_load - b.load)
    return deff

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
    ex_swapper(grid)

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
