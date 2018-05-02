import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

def count_data(nbh):
    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        return len([0 for line in df])


def plotter(nbh):
    nbh_min = [3132, 2252, 1957]
    nbh_max = [8670, 7019, 8459]


    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        data = [int(line) for no, line in enumerate(df) if no < 10000]
        print(len(data))
        k2, p = stats.normaltest(data)
        print('p-value on normality test:', p)
        fig = sns.distplot(data)
        plt.axvline(x=nbh_best[nbh - 1], color='green')
        plt.axvline(x=nbh_min[nbh - 1], color='red')
        plt.axvline(x=nbh_max[nbh - 1], color='red')
        plt.show()
        print('done!')
    return
