from Algorithms.Helpers.connect import connect

def get_bound(grid, lower=True):
    for h in grid.houses.values():
        if lower:
            b = h.closest_battery(grid, True)
        else:
            b = h.find_furthest_battery(grid)
        connect(h, b, True)

def upper_bound(grid):
    return get_bound(grid, False)

def lower_bound(grid):
    return get_bound(grid)
