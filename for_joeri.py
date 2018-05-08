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
