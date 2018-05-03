def reset_global_density(grid, house_list):

    for y in range(grid.y_dim):
            for x in range(grid.x_dim):
                grid.grid_list[x, y] = Grid_Point(x, y, house_list)

    for point in grid.grid_list:
        grid.total_probability += (1 / grid.grid_list[point].distance)
        grid.total_sq_probability += grid.grid_list[point].rel_distance
    for point in grid.grid_list:
        if point in house_list:
            grid.grid_list[point].probability = 0
            grid.grid_list[point].rel_probability = 0
            continue
        grid.grid_list[point].probability = (1
            / grid.grid_list[point].distance) / grid.total_probability
        grid.grid_list[point].rel_probability = (
        grid.grid_list[point].rel_distance / grid.total_sq_probability)
