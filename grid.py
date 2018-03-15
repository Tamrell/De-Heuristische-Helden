import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
from numpy import subtract
import csv
from house import House


class Grid:

    def __init__(self, file, dimensions=(50, 50)):

        self.grid_list = {}
        self.total_probability = 0
        self.houses = {}
        self.x_dim = dimensions[0]
        self.y_dim = dimensions[1]

        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                self.houses[(int(row[0]), int(row[1]))] = House(row)

        for y in range(self.y_dim):
            for x in range(self.x_dim):
                self.grid_list[x, y] = Grid_Point(x, y, self.houses)
        for point in self.grid_list:
            self.total_probability += (1 / self.grid_list[point].distance)
        for point in self.grid_list:
            self.grid_list[point].probability = (1 / self.grid_list[point].distance) / self.total_probability

    def y_list(self, y):
        """
        Helper function for print_heatmap. Returns the probabilities of row y
        """
        dist_list = []

        for i in range(self.x_dim):
            dist_list.append(self.grid_list[(i, y)].probability)

        return dist_list

    def print_heatmap(self):

        trace = go.Heatmap(z = [self.y_list(i) for i in range(self.x_dim)])
        data = [trace]
        plot(data, filename='labelled-heatmap.html')

    def __str__(self):
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
        self.probability = 0
        self.distance = 0
        for house in houses:
            self.distance += abs(house[0] - x) + abs(house[1] - y)
        self.x = x
        self.y = y
