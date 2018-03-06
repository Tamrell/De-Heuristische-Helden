class Grid:

    def __init__(self, houses):
        self.grid_list = []
        self.total_distance = 0
        self.total_probability = 0
        for x in range(50):
            for y in range(50):
                self.grid_list.append(Grid_Point(x, y, houses))
                for house in houses:
                    self.total_distance += abs(house["x"] - x)
                    + abs(house["y"] - y)
        for point in self.grid_list:
            self.total_probability += (self.total_distance / point.distance)
        for point in self.grid_list:
            point.probability = (self.total_distance / point.distance) / self.total_probability

class Grid_Point:

    def __init__(self, x, y, houses):
        self.probability = 0
        self.distance = 0
        for house in houses:
            self.distance += abs(house["x"] - x) + abs(house["y"] - y)
        self.x = x
        self.y = y




grid = Grid([{"x": 48, "y": 48}, {"x": 24, "y": 24}])
sum = 0

for point in grid.grid_list:
    sum += point.probability

print(sum)
# print(grid.grid)
