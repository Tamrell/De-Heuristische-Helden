import imports
class House:
    ''' House class, initializes with tuple: coordinate and int: output'''

    def __init__(self, info):
        self.cord = (info[0], info[1])
        self.output = info[2]

    def find_closest_battery(self, grid):
        ''' Returns the closest battery object or None

        Args:
            Grid: grid that contains batteries

        Returns:
            Battery: closest battery
        '''
        cords = grid.grid_list

        bat = None
        best = grid.x_dim + grid.y_dim
        for key in cords:
            if isinstance(cords[key], Battery): ## unnecesary if all batteries
                cur_bat = cords[key]
                dist = grid.distance(self.cord, cur_bat.cord)
                if bat is None or best > dist:
                    bat= cur_bat
        return bat
