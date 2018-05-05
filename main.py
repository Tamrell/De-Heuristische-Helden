import sys
from Classes.grid import Grid
from Algorithms.plots import hover_plot
from Algorithms.hill_leaper import hill_leaper
from Algorithms.evaluate_distribution import evaluate_distribution
from Algorithms.bounds import lower_bound, upper_bound
from Algorithms.Helpers.upper_bound import find_worst
from Algorithms.greedy_hillclimber import greedy_hillclimber
from Algorithms.a_smart import A_smart
from Algorithms.shortest_depth_first import shortest_depthest_first
from Algorithms.stochastic_hillclimber import *
from Algorithms.solspace import random_sampler
from Algorithms.random_battery_cycler import battery_cycler
from Results.Solspaces.plotter import custom_plotter
from Algorithms.branch_and_bound import *

def get_neighbourhood():
    legal = {'1', '2', '3'}
    print("\n For which neighbourhood do you want to run an algorithm?")
    nbh = input("\n(int): ")
    while not nbh in legal:
        print(nbh, "is an invalid choice, please choose 1, 2 or 3")
        nbh = input("\n(int): ")
    return nbh

def get_algorithm():
    print("\n Which algorithm do you want to run?")
    print("\n <key>: <algorithm>\n\n s: Solspace\n p: Procrastinator")
    print(" lower: Worst (illegal?) Config Finder")
    print(" upper: best (illegal?) Config Finder")
    print(" d: Shortest Depthest First")
    print(" e: evaluator")
    print(" r: Random Connect")
    print(" a: A-smart")
    print(" b: Battery Cycler")
    print(" n: Plot the distribution of the random solution space")
    print(" h: Print Heatmap")
    print(" bb: Branch and bound\n")
    return input("(alpha): ")

def run_algorithm(alg, grid):
    algorithms = {'s': ['Shortest DF', shortest_depthest_first],
                  'bb': ['branch & bound', branch_and_bound],
                  'r': ['Random Connect', random_sampler],
                  'b': ['battery cycler', battery_cycler],
                  'e': ['evaluate', evaluate_distribution],
                  'l': ['lower bound', lower_bound],
                  'u': ['upper bound', upper_bound],
                  'a': ['A-smart', A_smart]                           }
    algorithms[alg][1](grid)
    return algorithms[alg][0]

    if alg == 'bb':
        alg = 'branch & bound'
        grid = branch_and_bound(grid)

    # FIX SOLUTIONSPACE AND HEATMAP PRINTING
    if alg == 's':
        print("How many sample solutions do you want to generate?")
        print("(There are currently", count_data(nbh),
              "data points for this neighbourhood)\n")
        solutions = input("(int): ")
        random_sampler(grid, int(solutions))

    elif alg == 'h':
        print(" Press 'g' for global, 'r' for relative")
        rd = input(" 'g'/'r'\n")
        if rd == 'g':
            grid.print_heatmap(0)
        elif rd == 'r':
            grid.print_heatmap(1)

def mode():
    print("\n Which mode do you want to enter?")
    print("\n <key>: <mode>\n\n p: plot data\n a: run algorithms")
    print(" d: add data\n")
    return input("(alpha): ")

if __name__ == "__main__":

    nbh = get_neighbourhood()
    file1 = 'Data/wijk' + nbh + '_huizen.csv'
    file2 = 'Data/wijk' + nbh + '_batterijen.txt'
    grid = Grid(file1, file2, nbh)
    alg = get_algorithm()
    alg = run_algorithm(alg, grid)

    if alg == 'n':
        plotter(nbh)
        exit(1)
    print("\n Which iterative algorithm do you want to apply?\n\n")
    print(" Press return for none\n")
    print(" s: Stochastic Hillclimber")
    print(" g: Greedy Hillclimber")
    print(" l: Hill Leaper\n")

    itt = input("(alpha): ")


    if itt == 's':
        itt = 'stochastic climber'
        pre_score = grid.score()
        stochastic_hillclimber(grid)
    elif itt == 'g':
        itt = 'greedy climber'
        pre_score = grid.score()
        greedy_hillclimber(grid)
    elif itt == 'l':
        itt = 'hill leaper'
        pre_score = grid.score()
        hill_leaper(grid)
    else:
        pre_score = False
    if itt:
        grid.print_stats(alg, pre_score, itt)
    else:
        grid.print_stats(alg)
    print('Do you want to save the resulting grid?')
    option = input("y/n\n")
    if option == 'y':
        print(grid)

        grid.print_stats(alg, pre_score)
