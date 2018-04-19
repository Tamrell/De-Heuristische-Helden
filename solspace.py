from tryhard import *
from random import shuffle, choice

def random_connect(grid):
    houses = [h for h in grid.houses.values() if h.free]
    shuffle(houses)
    c = Connections()
    for h in houses:
        bats = [b for b in h.dists if b.fits(h.output)]
        if bats:
            c.connect(h, choice(bats))
        else:
            return False
    if [h for h in grid.houses.values() if h.free]:
        return False
    else:
        c.ex_swapper(grid)
        print(grid.score())
        for i in range(10):
            c.true_ex_swapper(grid)
            print(grid.score()) 
        return True

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

    i = 0
    scores = {}
    best = (100000000, None)
    while i < 1:
        grid = Grid(file1, file2)
        if random_connect(grid):
            if grid.score() in scores:
                scores[grid.score()] += 1
            else:
                scores[grid.score()] = 1
            print(i, grid.score())
            i += 1
            if grid.score() < best[0]:
                best = (grid.score(), grid)
        Battery.color_generator = assign_color()
    line_plot(scores)
    for i in range(100000000):
        i += 1
        i -= 1
    print(best[0])
    hover_plot(best[1])
