import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

nbh = input("which neighbourhood do you want the distribution plot of?"\n)
with open('SS' + nbh + '.csv') as df:
    data = [int(line) for line in df]
    fig = sns.distplot(data)
    plt.show()

    print('done!')
