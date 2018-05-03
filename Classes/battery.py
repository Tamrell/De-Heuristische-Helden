from numpy import subtract

def assign_color():
    for color in ['on_green', 'on_blue', 'on_red', 'on_cyan', 'on_yellow',
                  'on_magenta', 'on_white']:
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
        self.links = set()
        self.color = next(Battery.color_generator)

    def __lt__(self, other):
        '''For sorting purposes, value is equal to the load. '''
        if self.load < other.load:
            return True
        return False

    def fits(self, output):
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
        #
        # best = grid.x_dim + grid.y_dim
        # best_cord = ()
        #
        # for h in house_list:
        #     housyboi = grid.houses[h]
        #     if self.max_load >= self.load + housyboi.output:
        #         dist = grid.distance(self.cord, h)
        #         if best > dist:
        #             best = dist
        #             best_cord = h
        # return best_cord

    def find_cheapest_house(self):
        ''' Returns the House object with the lowest output in self.links.

        Args:
            None

        Returns:
            House: 'cheapest' House
        '''
        cheapest = list(self.links)[0]
        for h in self.links:
            if h.output < cheapest.output:
                cheapest = h
        return cheapest

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
