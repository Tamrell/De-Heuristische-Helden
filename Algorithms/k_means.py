from Algorithms.Helpers.connect import connect

def k_means(grid):
    """
        Tries to find ideal k-means configuration for the grid.

    Takes
        Grid: grid containing the houses used for the k-means

    Returns
        None
    """
    moved = True
    while moved:
        moved = False
        for b in grid.batteries.values():
            if cluster_mean(grid, b):
                moved = True

def cluster_mean(grid, bat, restricted=False):
    '''
        Calculates new location for battery, this being the mean of its current
        cluster. currently also moves the battery.

    Takes
        Grid: grid containing houses
        Battery: battery for which the new location will be calculated

    Returns
        Bool: True if the battery has been moved, else False
    '''
    x_val = 0
    y_val = 0
    houses = [h.cord for h in grid.houses.values() if h.closest_battery(grid) == bat]
    if houses:

        # Calculate the mean coordinate of the cluster.
        for x, y in houses:
            x_val += x
            y_val += y
        x_val = int(x_val / len(houses))
        y_val = int(y_val / len(houses))

        # Move battery to the mean, or next to it if it contains a house.
        for i in [0, 1, -1]:
            if not (x_val + i, y_val) in grid.houses:
                grid.move_battery(bat ,(x_val + i, y_val))
                break
            if not (x_val, y_val + i) in grid.houses:
                grid.move_battery(bat ,(x_val, y_val + i))
                break
