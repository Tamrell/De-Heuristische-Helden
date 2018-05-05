import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from Algorithms.bounds import lower_bound, upper_bound
sns.set(color_codes=True)

def count_data(nbh):
    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        return len([0 for line in df])

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

    fig = sns.distplot(s1)
    fig2 = sns.distplot(s2)
    plt.axvspan(lb - 1000, lb, alpha=0.5, color='red')
    plt.axvspan(ub, ub + 1000,
                alpha=0.5, color='red')
    plt.show()

def plotter(nbh):
    nbh_min = [3132, 2252, 1957]
    nbh_max = [8670, 7019, 8459]
    nbh_best = [3488, 2292, 2069]

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
