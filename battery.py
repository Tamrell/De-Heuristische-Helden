class Battery:
    ''' Battery class, initializes with tuple: coordinate and int: max_load'''

    def __init__(self, cord, max_load):
        self.cord = cord
        self.max_load = max_load
        self.load = 0
        self.links = []
