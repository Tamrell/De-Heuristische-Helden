from numpy import subtract

class Battery:
    ''' Battery class, initializes with tuple: coordinate and int: max_load

        attributes:
        - cord: coordinate as (x, y) Tuple
        - max_load: maximum load of the battery as Integer
        - load: current load as float
        - links: list of houses the battery is connected with
        - color: color the houses will get if connected with this battery
    '''

    def __init__(self, cord, max_load):
        self.cord = cord
        self.max_load = max_load
        self.load = 0
        self.links = []
        self.color = self.__assign_color()

    def __assign_color(self):
        for color in ['green', 'blue', 'red', 'grey', 'yellow', 'orange']:
            yield color
