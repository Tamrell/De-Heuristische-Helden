from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from Algorithms.k_means import k_means
from Algorithms.random_connect import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Algorithms.Helpers.bounds import lower_bound, upper_bound
from bokeh.models import Title
from tqdm import tqdm

def k_visualize(grid):
    p = figure(title="Cost per k-bats iteration",)
    p.add_layout(Title(text="Iterations", align="center"), "below")
    p.add_layout(Title(text="Cost", align="center"), "left")
    lower = []
    # upper = []
    cycler = []
    rand = []
    scitt = []
    iterations = []
    s_size = 100
    for i in tqdm(range(20)):
        lower_bound(grid)
        lower.append(grid.score())
        # grid.reset()
        # upper_bound(grid)
        # upper.append(grid.score())
        grid.reset()
        for j in range(s_size):
            battery_cycler(grid)
            cycler.append(grid.score())
            grid.reset()
            random_sampler(grid)
            rand.append(grid.score())
            grid.reset()
        iterations.append(i)
        for j in range(s_size):
            scitt.append(i)
        k_means(grid)
        grid.reset()
    p.scatter(scitt, rand, color="blue", legend="Random Connect")
    p.scatter(scitt, cycler, color="green", legend="Battery Cycler")
    p.line(iterations, lower, color="red", legend="Lower bound")
    # p.line(iterations, upper)
    show(p)
