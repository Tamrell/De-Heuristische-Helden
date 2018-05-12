from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from Algorithms.k_means import k_means
from Algorithms.random_battery_cycler import battery_cycler
from Algorithms.Helpers.bounds import lower_bound, upper_bound
from tqdm import tqdm

def k_visualize(grid):
    p = figure()
    for alg in [lower_bound, upper_bound, battery_cycler]:
        data = []
        iterations = []
        for i in range(20):
            print(grid)
            alg(grid)
            data.append(grid.score())
            iterations.append(i)
            grid.reset()
            k_means(grid)
            grid.reset
        p.line(iterations, data)
    show(p)
