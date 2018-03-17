import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
from numpy import subtract
import csv
from house import House
import sys

class Grid:

    def __init__(self, file, dimensions=(50, 50)):
        """ Constructor, needs a file with information about the houses and
            optional dimensions of the Grid (default is 50x50).

            Args:
                file: A csv file containing the information about the houses,
                one house per row. Each row contains (in order): x-coordinate,
                y-coordinate, maximum capacity.

                dimensions (Tuple): A tuple containing the x- and y-coordinates
                of the Grid, defaults to 50x50.
        """

        self.grid_list = {}
        self.total_probability = 0
        self.houses = {}
        self.x_dim = dimensions[0]
        self.y_dim = dimensions[1]
        self.set_houses(file)
        self.set_global_density()

    def set_global_density(self):
        """ Goes through all the Grid_Points on the Grid and calculates the
            "global density" of each point. This is done by first calculating
            the sum of the distances to every house on the grid from that
            point. Then the reciprocal (1 divided by the value) is taken. The
            density for each point is calculated by dividing its own reciprocal
            by the sum of all reciprocals on the board.
        """

        for y in range(self.y_dim):
            for x in range(self.x_dim):
                self.grid_list[x, y] = Grid_Point(x, y, self.houses)
        for point in self.grid_list:
            self.total_probability += (1 / self.grid_list[point].distance)
        for point in self.grid_list:
            self.grid_list[point].probability = (1
                / self.grid_list[point].distance) / self.total_probability

    def set_houses(self, file):
        """ Takes a .csv file and add the houses in the file to the houses
            dictionary of the Grid. Keys of the houses are the x-y-coordinates
            in a tuple.

            Args:
                file: A csv file containing the information about the houses,
                one house per row. Each row contains (in order): x-coordinate,
                y-coordinate, maximum capacity.
        """

        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                self.houses[(int(row[0]), int(row[1]))] = House(row)

    def y_list(self, y):
        """ Helper function for print_heatmap. Returns the probabilities
            of row y.
        """

        dist_list = []
        for i in range(self.x_dim):
            dist_list.append(self.grid_list[(i, y)].probability)

        return dist_list

    def print_heatmap(self):
        """ Prints out the global density heatmap in a file called
            'labelled-heatmap.html' using Plotly.
        """

        trace = go.Heatmap(z = [self.y_list(i) for i in range(self.x_dim)])
        data = [trace]
        plot(data, filename='labelled-heatmap.html')

    def __str__(self):
        """ Returns a string that represents the Grid. Each '_' represents an
            empty spot and each 'H' represents a house.
        """

        string = ""
        for y in range(self.y_dim):
            for x in range(self.x_dim):
                if (x, y) in self.houses:
                    string += "H "
                else:
                    string += "_ "
            string += "\n"
        return string


class Grid_Point:

    def __init__(self, x, y, houses):
        """ Constructor, takes an x-coordinate, y-coordinate and a dictionary
            of houses and calculates the sum of distances to all the houses
            from that point.

            Args:
                x (Integer): x-coordinate of the Grid_Point.

                y (Integer): y-coordinate of the Grid_Point.

                houses (Dictionary): A dictionary of Houses on the grid, key is
                given by a tuple (x, y).
        """

        self.probability = 0
        self.distance = 0
        for house in houses:
            self.distance += abs(house[0] - x) + abs(house[1] - y)
        self.x = x
        self.y = y
