class Battery:
    ''' Battery class, initializes with tuple: coordinate and int: max_load'''

    def __init__(self, (x, y), max_load):
        self.cord = (x, y)
        self.max_load = max_load
        self.load = 0
        self.links = []
