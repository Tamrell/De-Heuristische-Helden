import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

def count_data(nbh):
    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        return len([0 for line in df])


def plotter(nbh):
    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        data = [int(line) for line in df]
        print(len(data))
        fig = sns.distplot(data)
        plt.show()
        print('done!')
