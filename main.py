import sys
from grid import *

if __name__ == "__main__":

    file = sys.argv[1]
    if file == '1':
        file = 'Data/wijk1_huizen.csv'
    elif file == '2':
        file = 'Data/wijk2_huizen.csv'
    elif file == '3':
        file = 'Data/wijk3_huizen.csv'

    grid = Grid(file)
    grid.print_heatmap(1)
    print(grid)
