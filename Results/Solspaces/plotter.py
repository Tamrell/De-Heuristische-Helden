import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


def plotter(nbh):
    with open('Results/Solspaces/SS' + nbh + '.csv') as df:
        data = [int(line) for line in df]
        fig = sns.distplot(data)
        plt.show()
        print('done!')
