import csv
from battery import *

def get_x(string):
    """gets the first element of [x, y]
    Args:
        string: string of form [x, y]
    Returns:
        int(end_string): x coordinate"""

    end_string = ""

    # find index of ","
    string_end = string.find(",")
    if string_end == -1:
        return string_end

    # seperate all int-type characters
    for char in string[:string_end]:
        if char.isdigit():
            end_string += char


    return int(end_string)

def get_y(string):
    """gets the second element of [x, y]
    Args:
        string: string of form [x, y]
    Returns:
        int(end_string): y coordinate"""

    end_string = ""

    # find index of ","
    string_end = string.find(",")
    if string_end == -1:
        return string_end

    # seperate all int-type characters
    for char in string[string_end:]:
        if char.isdigit():
            end_string += char

    return int(end_string)

def get_coordinates(string):
    """get the tuple (x, y) from string '[x, y]'"""
    (x, y) = get_x(string), get_y(string)
    return(x, y)

def process_line(line):
    """extract from a string the position and capacity of a battery
    Args:
        line: list of form [[x, y], "", capacity]]
    Returns:
        location: (x, y)-tuple as coordinates of battery
        capacity: maximum load of battery"""

    # first element of array
    location = get_coordinates(line[0])

    # last element of array
    capacity = float(line[-1])

    return(location, capacity)

def load_batteries(filename):
    """reads batteries from a file and places them in a grit"""

    battery_grid = {}

    # open file
    with open(filename) as f:
        # get list of batteries
        lines = csv.reader(f, delimiter = "\t")

        # skip header
        next(lines)

        for line in lines:
            location, capacity = process_line(line)

            # place batteries in a grid
            battery_grid[location] = Battery(location, capacity)
        return battery_grid
