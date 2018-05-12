from Algorithms.Helpers.connect import connect

def k_means(grid):
    """
        tries to find ideal k-means configurations for all combinations of
        4-10(?) batteries and then compares them to find the cheapest
        and best configuration

    Takes
        Grid: grid containing the houses used for the k-means

    Returns
        ?????
    """
    for b in grid.batteries.values():
        cluster_mean(grid, b)
    grid.light_reset()

def restricted_k_means(grid):
    """
        Calculates k-means with the restriction that it only calculates the
        closest houses which fit on the battery.

    Takes
        Grid: grid containing the houses used for the k-means

    Returns
        ?????
    """
    for b in grid.batteries.values():
        houses = [h for h in grid.houses.values() if h.free if h.closest_battery(grid) == b]
        if houses:
            yes = True
            while yes and houses:
                h = b.find_closest_house(grid, houses)
                if connect(h, b):
                    houses.remove(h)
                else:
                    yes = False
                print(grid)
            cluster_mean(grid, b, True)
    grid.light_reset()

def cluster_mean(grid, bat, restricted=False):
    '''
        Calculates new location for battery, this being the mean of its current
        cluster. currently also moves the battery.

    Takes
        Grid: grid containing houses
        Battery: battery for which the new location will be calculated

    Returns
        None
    '''
    # note that this mean may already be containing a house.
    x_val = 0
    y_val = 0
    if restricted:
        houses = [h.cord for h in bat.links]
    else:
        houses = [h.cord for h in grid.houses.values() if h.closest_battery(grid) == bat]
    if houses:
        for x, y in houses:
            x_val += x
            y_val += y
        x_val = int(x_val / len(houses))
        y_val = int(y_val / len(houses))
        for i in [0, 1, -1]:
            if not (x_val + i, y_val) in grid.houses:
                grid.move_battery(bat ,(x_val + i, y_val))
                break
            if not (x_val, y_val + i) in grid.houses:
                grid.move_battery(bat ,(x_val, y_val + i))
                break
