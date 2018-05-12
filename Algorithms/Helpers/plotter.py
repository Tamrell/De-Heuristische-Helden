import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from Algorithms.Helpers.bounds import lower_bound, upper_bound
sns.set(color_codes=True)

def custom_plotter(grid, s1, s2):
    '''s1 = scores list 1
       s2 = scores list 2
       makes a plot of the problem space of a grid'''

    lower_bound(grid)
    lb = grid.score()
    grid.reset()
    upper_bound(grid)
    ub = grid.score()
    grid.reset

    fig2 = plt.hist(s2)
    fig = plt.hist(s1)
    plt.axvspan(lb - 500, lb, alpha=0.5, color='red')
    plt.axvspan(ub, ub + 500,
                alpha=0.5, color='red')

    fig_name = 'Results/' + str(grid.nbh) + '/' + str(min(s2))
    for b in grid.batteries.values():
        fig_name += '\n' + b.type + ': ' + str(b.cord)
    plt.savefig(fig_name + '\n.png')

def plotter(nbh):
    nbh_min = [3132, 2252, 1957]
    nbh_max = [8670, 7019, 8459]
    #nbh_best = [3486, 2292, 2069]
    nbh_best = [4062, 2470, 2507]

    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        data = [int(line) for no, line in enumerate(df)]

        print('p-value on normality test:', p)
        fig = sns.distplot(data)
        plt.axvline(x=nbh_best[int(nbh) - 1], color='green')
        plt.axvspan(0, nbh_min[int(nbh) - 1], alpha=0.5, color='red')
        plt.axvspan(nbh_max[int(nbh) - 1], nbh_max[int(nbh) - 1] + 1000,
                    alpha=0.5, color='red')
        plt.show()
        print('done!')
    return
