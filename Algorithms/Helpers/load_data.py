from Classes.house import House
from Classes.battery import Battery
import csv

def get_houses(data):
    '''
        Takes a .csv file and add the houses in the file to a
        dictionary with coordinate(tuple): house(House) as key: value.

        Args:
            file: A csv file containing the information about the houses,
            one house per row. Each row contains (in order): x-coordinate,
            y-coordinate, maximum capacity.
    '''
    houses = {}
    with open(data, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            cord, output = (int(row[0]), int(row[1])), float(row[2])
            houses[cord] = House(cord, output)
    return houses


def get_batteries(data):
    '''
        Takes a .csv file and adds the batteries in the file to a
        dictionary with coordinate(tuple): battery(Battery) as key: value.

        Args:
            file: A csv file containing the information about the houses,
            one house per row. Each row contains (in order): x-coordinate,
            y-coordinate, maximum capacity.
    '''
    batteries = []
    with open(data) as f:
        lines = csv.reader(f, delimiter = ",")
        next(lines)
        for line in lines:
            location, capacity = (int(line[0]), int(line[1])), float(line[2])
            batteries.append(Battery(location, capacity))
    return batteries
