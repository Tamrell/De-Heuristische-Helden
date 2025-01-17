from numpy import subtract


def assign_color():
    ''' For debugging reasons, we give batteries a color.

        Args:
            None
        Returns:
            str: next color
    '''
    for color in ['on_green', 'on_blue', 'on_red', 'on_cyan', 'on_yellow',
                  'on_magenta', 'on_white', 'on_grey',
                  'on_green', 'on_blue', 'on_red', 'on_cyan', 'on_yellow',
                  'on_magenta', 'on_white', 'on_grey',
                  'on_green', 'on_blue', 'on_red', 'on_cyan', 'on_yellow',
                  'on_magenta', 'on_white', 'on_grey','on_green', 'on_blue',
                  'on_red', 'on_cyan', 'on_yellow', 'on_magenta', 'on_white',
                  'on_grey',]:
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

    def __init__(self, cord, max_load, btype='Default'):
        self.cord = cord
        self.max_load = max_load
        self.load = 0
        self.type = btype
        self.links = set()
        self.color = next(Battery.color_generator)

    def __lt__(self, other):
        '''For sorting purposes, value is equal to the load. '''
        if self.load < other.load:
            return True
        return False

    def fits(self, output):
        ''' Returns True if the output fits on the battery else False'''
        if self.max_load >= self.load + output:
            return True
        return False

    def find_closest_house(self, grid, houses):
        ''' Returns the closest House object

            Args:
                Grid: grid that contains batteries
                List: list containing houses on the grid

            Returns:
                House: closest House
        '''
        options = [(h.dists[self], h) for h in houses if self.fits(h.output)]
        if options:
            return min(options)[1]

    def fits_max(self, output, max_load):
        ''' Returns True if the output fits on the battery if it had
            a max_load equal to the third argument else False
        '''
        if max_load >= self.load + output:
            return True
        return False

    def find_closest_house_max(self, grid, houses, max_load):
        options = [(h.dists[self], h) for h in houses if self.fits_max(h.output, max_load)]
        if options:
            return min(options)[1]

    def find_furthest_house(self, grid):
        ''' Returns the furthest House object in self.links.

        Args:
            Grid: grid object containing the houses

        Returns:
            House: furthest House in the self.links
        '''
        best = 0
        best_house = None
        for house in self.links:
            dist = grid.distance(house.cord, self.cord)
            if dist > best:
                best = dist
                best_house = house
        return best_house
