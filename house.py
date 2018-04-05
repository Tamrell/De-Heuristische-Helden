import imports
class House:
    ''' House class, initializes with tuple: coordinate and int: output
        atrributes:
        - cord: Coordinate as (x, y) Tuple
        - output: output as float
        - free: true if not connected to a battery
        - color: color in which the house will be printed
    '''

    def __init__(self, info):
        self.cord = (info[0], info[1])
        self.output = float(info[2])
        self.free = True
        self.color = 'white'

    def __lt__(self, other):
        return True

    def find_closest_battery(self, grid):
        ''' Returns the closest battery object or None

        Args:
            Grid: grid that contains batteries

        Returns:
            Battery: closest battery
        '''
        batteries = grid.batteries

        bat = None
        best = grid.x_dim + grid.y_dim
        for battery in batteries:
            b = batteries[battery]
            if b.max_load >= b.load + self.output:
                cur_bat = b
                dist = grid.distance(self.cord, cur_bat.cord)
                if bat is None or best > dist:
                    bat= cur_bat
                    best = dist
        return bat
