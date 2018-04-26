def connect(house, battery, overload=False):
    """This function connects a house to a battery in the grid and in the
        local representation. Also checks if battery does not get
        overconnected by connecting house
    Takes
        house: a House instance
        battery: the Battery instance house must be connected to
    Returns
        True if battery could be connected; else False"""
    # check for overloadedness
    if (not battery.fits(house.output) and not overload) or not house.free:
        return False

    battery.load += house.output
    # connect in grid
    house.bat = battery
    house.color = battery.color
    house.free = False
    battery.links.add(house) ##doesnot happen
    return True

def unconnect(house):
    """Disconnects the house from its battery"""
    try:
        house.bat.load -= house.output
        house.bat.links.remove(house)
        house.color = 'white'
        house.bat = None
        house.free = True
    except:
        print("HAHA GETREKT unconnect")
        input(grid)

def hard_swap(h1, h2, overload=False):
    """This function swaps two houses from two seperate batteries
    Takes
        house1, house2: House instances from two seperate batteries
    Returns
        Bool: True if swap was succesfull else false."""
    if h1 == h2:
        return False
    b1 = h1.bat
    b2 = h2.bat
    if overload or b1.max_load >= b1.load - h1.output + h2.output:
        if overload or b2.max_load >= b2.load - h2.output + h1.output:
            unconnect(h1)
            unconnect(h2)
            connect(h1, b2)
            connect(h2, b1)
            return True
    else:
        return False

def calculate_distance(battery, house): ## remove from grid and house
    """This function calculates the distance between a battery and a house
    Takes:
        battery: Battery instance as starting point of connection
        house: House instance as endpoint
    Returns:
        distance between battery and house"""
    (x1, y1) = battery.cord
    (x2, y2) = house.cord
    return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
