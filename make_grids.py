from Classes.grid import *
import pickle

house_files = ['Data/wijk1_huizen.csv', 'Data/wijk2_huizen.csv',
               'Data/wijk3_huizen.csv']

battery_files = ['Data/wijk1_batterijen.txt', 'Data/wijk2_batterijen.txt',
                 'Data/wijk3_batterijen.txt']

file_name_base = 'Data/Objects/grid_with_batteries_'

for i in range(len(house_files)):
    file_name = file_name_base + str(i) + '.pkl'
    with open(file_name, 'wb') as output:
        grid = Grid(house_files[i], battery_files[i], i)
        pickle.dump(grid, output, pickle.HIGHEST_PROTOCOL)
        Battery.color_generator = assign_color()
