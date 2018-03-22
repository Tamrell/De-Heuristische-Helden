class Battery:
    ''' Battery class, initializes with tuple: coordinate and int: max_load
    
        atributes:
        - cord: coordinate as (x, y) Tuple
        - max_load: maximum load of the battery as Integer
        - load: current load as float
        - links: list of houses the battery is connected with
    '''

    def __init__(self, cord, max_load):
        self.cord = cord
        self.max_load = max_load
        self.load = 0
        self.links = []
