from numpy import subtract

def assign_color():
    for color in ['on_green', 'on_blue', 'on_red', 'on_grey', 'on_yellow', 'on_magenta',
                  'cyan', 'white']:
        yield color

class Battery:
    ''' Battery class, initializes with tuple: coordinate and int: max_load

        attributes:
        - cord: coordinate as (x, y) Tuple
        - max_load: maximum load of the battery as Integer
        - load: current load as float
        - links: list of houses the battery is connected with
        - color: color the houses will get if connected with this battery
    '''
    color_generator = assign_color()

    def __init__(self, cord, max_load):
        self.cord = cord
        self.max_load = max_load
        self.load = 0
        self.links = []
        self.color = next(Battery.color_generator)

        print(self.cord, "Added")
