from Algorithms.Helpers.connect import connect


def get_bound(grid, lower=True):
    """
        This function gets either the lower or the upper bound of a grid.

        Takes
            house1, house2: House instances from two seperate batteries

        Returns
            Int: lower or upper bound of a grid
    """
    for h in grid.houses.values():
        if lower:
            b = h.closest_battery(grid, True)
        else:
            b = h.find_furthest_battery(grid)
        connect(h, b, True)
    return grid.score()


def upper_bound(grid):
    """Runs get_bound for the upper bound"""
    return get_bound(grid, False)


def lower_bound(grid):
    """Runs get_bound for the lower bound"""
    return get_bound(grid)
