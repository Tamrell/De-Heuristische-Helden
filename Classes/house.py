import math
class House:
    ''' House class, initializes with tuple: coordinate and int: output
        atrributes:
        - cord: Coordinate as (x, y) Tuple
        - output: output as float
        - free: true if not connected to a battery
        - color: color in which the house will be printed
        - dists: dict with Battery:distance
    '''

    def __init__(self, info, batteries):
        self.cord = (int(info[0]), int(info[1]))
        self.output = float(info[2])
        self.free = True
        self.color = 'white'
        self.bat = None
        self.dists = {b: self.distance(self.cord, b.cord) for b in batteries}

    def __lt__(self, other):
        '''For sorting purposes, there is no need to differentiate. '''
        return True

    def distance(self, cord1, cord2, euclidian=False):
        if euclidian:
            return self.euclidian(cord1, cord2)
        (x1, y1) = cord1
        (x2, y2) = cord2
        return (abs(int(x1) - int(x2)) + abs(int(y2) - int(y1)))

    def euclidian(self, cord1, cord2):
        (x1, y1) = cord1
        (x2, y2) = cord2
        return math.sqrt(abs(int(x1) - int(x2))**2 + abs(int(y2) - int(y1))**2)

    def find_closest_battery(self, grid, overload=False):
        ''' Returns the closest battery object or None

        Args:
            Grid: grid that contains batteries
            Bool(optional): True if the batteries may be overloaded

        Returns:
            Battery: closest battery
        '''
        return min([(d, b) if (overload or b.fits(self.output))
                    else (100, None) for b, d in self.dists.items()])[1]

    def find_furthest_battery(self, grid):
        ''' Returns the furthest battery object or None

        Args:
            Grid: grid that contains batteries
            Bool(optional): True if the batteries may be overloaded

        Returns:
            Battery: closest battery
        '''
        return max([(d, b) for b, d in self.dists.items()])[1]
