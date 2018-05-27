from Classes.grid import Grid_Point

def set_global_density(grid, house_list):
    """
    For each point on the Grid, calculates the sum of the distances to all
    houses on the Grid. The reciprocate of this sum is added to the
    grid.total_probability. The global density for each point is calculated by
    dividing it's reciprocate sum by grid.total_probabilty. The sum of all of
    these probabilities adds up to 1. Higher means more dense.

    Note: Where set_local_density() looks at the reciprocate of the distances,
    set_global_density() treats all distances equally.

    Takes
        Grid: grid containing the houses that have to be connected later on

        List: A list of batteries (capacity, battery type) that will be
        placed on the Grid.

    Returns
        None
    """

    for y in range(grid.y_dim):
            for x in range(grid.x_dim):
                grid.grid_list[x, y] = Grid_Point(x, y, house_list)

    for point in grid.grid_list.values():
        if point.distance:
            grid.total_probability += (1 / point.distance)
    for cord, point in grid.grid_list.items():
        if cord in grid.houses:
            point.probability = 0
            continue
        point.probability = (1 / point.distance) / grid.total_probability

def set_local_density(grid, house_list):
    """
    For each point on the grid, calculates the sum of the reciprocate distances
    to all houses on the grid. This sum is added to the
    grid.total_loc_probability. The local density for each point is calculated
    by dividing it's sum by grid.total_loc_probabilty. The sum of all of
    these probabilities adds up to 1. Higher means more dense.

    Note: Where set_global_density() treats all distances equally,
    set_local_density() looks at the reciprocate of these distances.

    Takes
        Grid: grid containing the houses that have to be connected later on

        List: A list of batteries (capacity, battery type) that will be
        placed on the Grid.

    Returns
        None
    """

    for y in range(grid.y_dim):
            for x in range(grid.x_dim):
                grid.grid_list[x, y] = Grid_Point(x, y, house_list)

    for point in grid.grid_list.values():
        if point.distance:
            grid.total_loc_probability += point.loc_distance

    for cord, point in grid.grid_list.items():
        if cord in grid.houses:
            point.loc_probability = 0
            continue
        point.loc_probability = (
            point.loc_distance / grid.total_loc_probability)

def move_to_middle(grid, bat):
    """
    Moves the given battery to the most optimal position based on it's current
    linked houses.

    Takes
        Grid: grid object with batteries and houses that are already connected.

        Battery: battery object that is currently on the Grid

    Returns
        None
    """

    houses = [h for h in bat.links]
    set_global_density(grid, houses)
    sorted_list = sorted(grid.grid_list.values(), key=lambda x: x.probability,
                         reverse=True)
    loc = (sorted_list[0].x, sorted_list[0].y)
    grid.move_battery(bat, loc)
