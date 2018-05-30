from Algorithms.Helpers.connect import connect
from statistics import mean

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
        print('WOEEE')
        moved = False
        for b in grid.batteries.values():
            if cluster_mean(grid, b):
                moved = True

def restricted_k_means(grid):
    """
    Tries to find ideal k-means configuration for the grid,
    also taking the battery capacities into account.

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

def cluster_mean(grid, battery):
    '''
    Calculates new location for battery, this being the mean of its current
    cluster. Then moves the battery to that location

    Takes
        Grid: grid containing houses
        Battery: battery for which the new location will be calculated

    Returns
        Bool: True if the battery has been moved, else False
    '''
    houses = [h.cord for h in grid.houses.values()
              if h.closest_battery(grid) == battery]
    if houses:

        # Calculate the mean coordinate of the house cluster.
        x = int(mean([cord[0] for cord in houses]))
        y = int(mean([cord[1] for cord in houses]))

        # Move battery to the mean, or next to it if it contains a house.

        for i in [0, 1, -1]:
            for cord in [(x + i, y), (x, y + i)]:
                if not cord in grid.houses:
                    grid.move_battery(battery ,cord)
                    break


def cluster_mean2(grid, battery):
    '''
    Calculates new location for battery, this being the mean of its current
    cluster. Then moves the battery to that location

    Takes
        Grid: grid containing houses
        Battery: battery for which the new location will be calculated

    Returns
        Bool: True if the battery has been moved, else False
    '''
    houses = []
    for h in grid.houses.values():
        if h.closest_battery(grid) == battery:
            houses.append(h.cord)
            battery.load += h.output

    battery.load = 0

    if houses:

        # Calculate the mean coordinate of the house cluster.
        x = int(mean([cord[0] for cord in houses]))
        y = int(mean([cord[1] for cord in houses]))

        # Move battery to the mean, or next to it if it contains a house.

        for i in [0, 1, -1]:
            found = False
            for cord in [(x + i, y), (x, y + i)]:
                if not cord in grid.houses:
                    grid.move_battery(battery ,cord)
                    print(x)
                    found = True
                    break
            if found:
                break
