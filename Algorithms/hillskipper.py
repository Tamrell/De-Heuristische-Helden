from Algorithms.contest import hard_swap

def hillskipper(grid):
    houses = [h for h in grid.houses.values()]
    best = (grid.score(), [])
    for h1 in houses:
        for h2 in houses:
            if hard_swap(h1, h2):
                for h3 in [h1, h2]: # in houses necessary?
                    for h4 in houses:
                        if hard_swap(h3, h4):
                            if grid.score() < best[0]:
                                best = (grid.score(), [h1, h2, h3, h4])
                            hard_swap(h3, h4)
                hard_swap(h1, h2)
    if best[1]:
        hard_swap(best[1][0], best[1][1])
        hard_swap(best[1][2], best[1][3])
        return True
    else:
        return False
