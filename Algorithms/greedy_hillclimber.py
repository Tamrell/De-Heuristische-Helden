from Algorithms.contest import hard_swap

def greedy_hillclimber(grid):
    check = True
    while check:
        swaps = [(h1, h2) for h1 in grid.houses.values() for h2 in grid.houses.values()]
        check = False
        best = (0, None, None)
        for h1, h2 in swaps:
            b1 = h1.bat
            b2 = h2.bat
            if b1.max_load >= b1.load - h1.output + h2.output:
                if b2.max_load >= b2.load - h2.output + h1.output:
                    diff = h1.dists[b2] + h2.dists[b1] - h1.dists[b1] - h2.dists[b2]
                    if diff < 0:
                        if diff < best[0]:
                            best = (diff, h1, h2)
        if best[1] and best[2]:
            swap(best[1], best[2])
            check = True
    print("tried it all...")
    return True
