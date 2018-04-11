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
        self.bat = None

    def __lt__(self, other):
        '''For sorting purposes, there is no need to differentiate. '''
        return True

    def find_closest_battery(self, grid, free=True):
        ''' Returns the closest battery object or None

        Args:
            Grid: grid that contains batteries
            Bool(optional): False if the batteries may be overloaded

        Returns:
            Battery: closest battery
        '''
        batteries = grid.batteries

        bat = None
        best = grid.x_dim + grid.y_dim
        for b in batteries.values():
            if not free or b.max_load >= b.load + self.output:
                cur_bat = b
                dist = grid.distance(self.cord, cur_bat.cord)
                if bat is None or best > dist:
                    bat= cur_bat
                    best = dist

        return bat
