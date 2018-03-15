import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

class Grid:

    def __init__(self, houses):
        self.grid_list = []
        self.total_probability = 0
        for y in range(50):
            for x in range(50):
                self.grid_list.append(Grid_Point(x, y, houses))
        for point in self.grid_list:
            self.total_probability += (1 / point.distance)
        for point in self.grid_list:
            point.probability = (1 / point.distance) / self.total_probability

    def y_list(self, y):
        start_index = (y - 1) * 50
        end_index = start_index + 50
        dist_list = []
        for i in range(start_index, end_index):
            dist_list.append(self.grid_list[i].probability)
        return dist_list

class Grid_Point:

    def __init__(self, x, y, houses):
        self.probability = 0
        self.distance = 0
        for house in houses:
            self.distance += abs(house["x"] - x) + abs(house["y"] - y)
        self.x = x
        self.y = y


grid = Grid([{"x": 15, "y": 28}, {"x": 45, "y": 45}, {"x": 44, "y": 44}])

trace = go.Heatmap(z = [grid.y_list(i) for i in range(1, 51)])

data = [trace]

plot(data, filename='labelled-heatmap.html')

# sum = 0

# for point in grid.grid_list:
#     sum += point.probability
#     print(point.probability)

# print(sum)
