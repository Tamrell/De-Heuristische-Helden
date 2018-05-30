import plotly.plotly as py
from Classes.house import House
from Classes.battery import Battery, assign_color
from Algorithms.Helpers.connect import unconnect
from numpy import subtract
import csv
import copy
import statistics as st
import sys
import termcolor


class Grid:
    '''
        atrributes:
        - grid_list: dict containing: coordinates:Grid_Point
        - houses: dict containing: coordinate:House
        - batteries: dict containing: coordinate:Battery
    '''

    def __init__(self, nbh, houses, batteries=[], dimensions=(50, 50)):
        '''
            Constructor, needs a file with information about the houses and
            optional dimensions of the Grid (default islf.houses = {} 50x50).

            Args:
                file: A csv file containing the information about the houses,
                one house per row. Each row contains (in order): x-coordinate,
                y-coordinate, maximum capacity.

                nbh: Neighbourhood number (can be 1, 2 or 3)

                dimensions (Tuple): A tuple containing the x- and y-coordinates
                of the Grid, defaults to 50x50.
        '''
        # Reset color_generator
        Battery.color_generator = assign_color()

        self.nbh = nbh
        self.x_dim = dimensions[0]
        self.y_dim = dimensions[1]
        self.houses = houses
        self.batteries = {}
        self.initial_batteries = {}
        self.grid_list = {}
        self.total_probability = 0
        self.total_loc_probability = 0
        self.initial_houses = copy.deepcopy(self.houses)
        for b in batteries:
            self.add_battery(b)

    # defuq is met deze?
    def __lt__(self, other):
        return True

    def copy(self):
        new_grid = copy.deepcopy(self)
        self.recalc()
        return new_grid

    def add_battery(self, bat):
        self.batteries[bat.cord] = bat
        self.initial_batteries[bat.cord] = copy.copy(bat)
        self.recalc()

    def move_battery(self, bat, new_cord, linked_only=True):
        try:
            self.batteries[new_cord] = self.batteries.pop(bat.cord)
        except:
            print(self.batteries, new_cord, bat.cord)
        bat.cord = new_cord
        if linked_only:
            for h in bat.links:
                h.dists[bat] = self.distance(h.cord, bat.cord)
        else:
            for h in self.houses.values():
                h.dists[bat] = self.distance(h.cord, bat.cord)

    def light_reset(self):
        for b in self.batteries.values():
            for h in list(b.links):
                unconnect(h)

    def recalc(self):
        for h in self.houses.values():
            h.dists.clear()
            for b in self.batteries.values():
                h.dists[b] = self.distance(b.cord, h.cord)

    def reset(self):
        # print('Reset')
        self.houses.clear()
        self.batteries.clear()
        self.houses = copy.deepcopy(self.initial_houses)
        self.batteries = copy.deepcopy(self.initial_batteries)
        self.recalc()

    def update(self, other):
        self.initial_houses.clear()
        self.initial_batteries.clear()
        self.initial_houses.update(other.initial_houses)#= copy.copy(other.initial_houses)
        self.initial_batteries.update(other.initial_batteries)
        self.houses.clear()
        self.batteries.clear()
        self.houses = copy.copy(other.houses)
        self.batteries = copy.copy(other.batteries)
        # self.reset()

    def legal(self):
        if [h for h in self.houses.values() if h.free]:
            return False
        for b in self.batteries.values():
            if b.load > b.max_load:
                return False
        return True

    def score(self):
        costs = {'Powerstar': 900,
                 'Imerse-II': 1350,
                 'Imerse-III': 1800,
                 'Default': 5000}
        score = 0
        for b in self.batteries.values():
            for h in b.links:
                score += h.dists[b] * 9
            score += costs[b.type]
        return score

    def print_stats(self, alg):
        print("\===============================================\ ")
        print("| Neighbourhood:", self.nbh,           "\t\t\t\t|")
        print("| Algorithm:", alg,                      "\t\t\t|")
        print("|===============================================|")
        print("| Battery    \t: load    \t\t: max           \t\t|")
        print("|-----------------------------------------------|")
        for b in self.batteries.values():
            print("|", b.color[3:] + '  ', "\t:", round(b.load, 4),
                  "\t:", b.max_load, "\t|")
        print("|-----------------------------------------------|")
        print("| total capacity:", self.total_capacity(), "\t\t\t|")
        print("| total output  :", round(self.total_output()), "\t\t\t\t|")
        print("| total deff.   :", int(self.defficiency()), "\t\t\t\t|")
        print("|===============================================|")
        print("| total houses  :", len(self.houses), "\t\t\t\t|")
        print("| average output:",
                 round(self.total_output()/len(self.houses)), "\t\t\t\t|")
        # if pre:
        #     print("| vanilla-cost\t:", pre, "\t\t\t\t|")
        print("| final-cost\t:", self.score(), "\t\t\t\t|")
        print("\===============================================\ ")

    def total_output(self):
        output = 0
        for h in self.houses.values():
            output += h.output
        return output

    def total_capacity(self):
        capacity = 0
        for b in self.batteries.values():
            capacity += b.max_load
        return capacity

    def standard_deviation(self):
        return st.stdev([h.output for h in self.houses.values()])

    def mean_distance_shortest(self):
        return st.mean([h.dists[h.closest_battery(self)]
                       for h in self.houses.values()])

    def mean_distance(self):
        return st.mean([d for h in self.houses.values()
                          for d in h.dists.values()])

    def std_distance_shortest(self):
        return st.stdev([h.dists[h.closest_battery(self)]
                        for h in self.houses.values()])

    def std_distance(self):
        return st.stdev([d for h in self.houses.values()
                           for d in h.dists.values()])

    def defficiency(self):
        # calculates how inefficient all the batteries are used.
        deff = 0
        for b in self.batteries.values():
            deff += abs(b.max_load - b.load)
        return deff

    def __str__(self):
        '''
            Returns a string that represents the Grid. Each '_' represents
            an empty spot, each 'B' represents a battery and each 'H'
            represents a house.
        '''
        s = ""
        for y in range(self.y_dim + 1):
            for x in range(self.x_dim + 1):
                if (x, y) in self.houses:
                    color = self.houses[(x, y)].color
                    if color == 'white':
                        s += termcolor.colored("H", color)
                    else:
                        s += termcolor.colored("H", 'grey', color)
                    s += " "
                elif (x, y) in self.batteries:
                    color = self.batteries[(x, y)].color
                    s += termcolor.colored("B", 'grey', color,
                                            attrs=['reverse', 'blink'])
                    s += " "
                else:
                    s += "_ "
            s += "\n"
        return s

    def distance(self, cord1, cord2):
        (x1, y1) = cord1
        (x2, y2) = cord2
        return (abs(int(x1) - int(x2)) + abs(int(y2) - int(y1)))


class Grid_Point:

    def __init__(self, x, y, houses):
        ''' Constructor, takes an x-coordinate, y-coordinate and a dictionary
            of houses and calculates the sum of distances to all the houses
            from that point.

            Args:
                x (Integer): x-coordinate of the Grid_Point.

                y (Integer): y-coordinate of the Grid_Point.

                houses (Dictionary): A dictionary of Houses on the grid, key is
                given by a tuple (x, y).
        '''
        self.probability = 0
        self.distance = 0
        self.loc_distance = 0
        self.loc_probability = 0

        for house in houses:
            dist_to_house = house.distance((x, y), house.cord)
            if dist_to_house:
                self.loc_distance += 1 / dist_to_house
            else:
                self.loc_distance += 1
            self.distance += dist_to_house
        self.x = x
        self.y = y
