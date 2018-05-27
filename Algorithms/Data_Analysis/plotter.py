import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from Algorithms.Helpers.bounds import lower_bound, upper_bound
import matplotlib.patches as mpatches
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

    plt.hist(s1)
    plt.hist(s2)
    plt.title('Costs found by RC and BC')
    plt.ylabel('Occurence')
    plt.xlabel('Cost')

    blue_patch = mpatches.Patch(color='blue', label='Random Connect')
    green_patch = mpatches.Patch(color='green', label='Battery Cycler')
    red_patch = mpatches.Patch(color='red', label='Bounds')
    plt.legend(handles=[blue_patch, green_patch, red_patch])

    plt.axvspan(lb - 500, lb, alpha=0.5, color='red')
    plt.axvspan(ub, ub + 500,
                alpha=0.5, color='red')

    fig_name = 'Results/' + str(grid.nbh) + '/' + str(min(s2))
    for b in grid.batteries.values():
        fig_name += '\n' + b.type + ': ' + str(b.cord)
    plt.savefig(fig_name + '\n.png', bbox_inches='tight')

def plotter(nbh):
    nbh_min = [3132, 2252, 1957]
    nbh_max = [8670, 7019, 8459]
    #nbh_best = [3486, 2292, 2069] #best
    nbh_best = [25000 + 9 * 4062, 25000 + 9 * 2470, 9 * 2507 + 25000] #BB
    #nbh_best = [3486, 2292, 2069] #rbc+hc
    #nbh_best = [3517, 2302, 2073] #rbc

    plt.title('Costs found by RC and BC')
    plt.ylabel('Occurence')
    plt.xlabel('Cost')

    blue_patch = mpatches.Patch(color='blue', label='Random Connect')
    green_patch = mpatches.Patch(color='green', label='Branch & Bound')
    red_patch = mpatches.Patch(color='red', label='Bounds')
    plt.legend(handles=[blue_patch, green_patch, red_patch])

    with open('Results/Solspaces/SSB' + nbh + '.csv') as df:
        data = [int(line) for no, line in enumerate(df)]

        print("Making figure...")
        fig = sns.distplot(data)
        #plt.xlim((nbh_min[int(nbh) - 1] - 500, nbh_max[int(nbh) - 1] + 500))
        plt.axvline(x=nbh_best[int(nbh) - 1], color='green')
        #plt.axvspan(nbh_min[int(nbh) - 1] - 500, nbh_min[int(nbh) - 1], alpha=0.5, color='red')
        #plt.axvspan(nbh_max[int(nbh) - 1], nbh_max[int(nbh) - 1] + 500, alpha=0.5, color='red')
        plt.show()
        print('done!')
    return
