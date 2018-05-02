from Algorithms.contest import *
from random import choice

def shortest_depthest_first(grid):
    if [h for h in grid.houses.values() if h.free]:
        # for each length, connection in [(length, (House, Battery))]
        for _, con in sorted([(h.dists[h.find_closest_battery(grid)],
                              (h, h.find_closest_battery(grid)))
                              for h in grid.houses.values()
                              if h.free if h.find_closest_battery(grid)]):
                connect(con[0], con[1])
                if shortest_depthest_first(grid):
                    return True
                else:
                    print(str(grid).replace(" ", "").replace("_", "").replace("\n", "").replace("B", ""))
                    unconnect(con[0])
        return False
    else:
        return True
        # connections = sorted([(h.dists[h.find_closest_battery(grid)],
        #                       (h, h.find_closest_battery(grid)))
        #                       for h in grid.houses.values()
        #                       if h.free if h.find_closest_battery(grid)])
        # if connections:
        #     for _, con in connections:
        #         if tuple(path + [con]) in visited:
        #             print('fooked')
        #         else:
        #             connect(con[0], con[1])
        #             visited.add(tuple(path + [con]))
        #             if shortest_depthest_first(grid, path + [con], visited):
        #                 return True
        #             unconnect(con[0])
        # else:
        #     return False
