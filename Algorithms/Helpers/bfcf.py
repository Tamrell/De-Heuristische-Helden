import queue

def all_combos(grid):
    """
        This function makes all combinations of batteries which have
        a summed capacity that first exceeds the sum of all the houses' output.

    Takes
        Grid: grid containing the houses that have to be connected later on

    Returns
        List: list containing tuples containing tuples: [(total_capacity, (capacity, battery_type).etc).etc]
    """
    all_batteries = [(450, 'Powerstar'),
                     (900, 'Imerse-II'),
                     (1800, 'Imerse-III')]
    q = queue.Queue()
    configurations = set()
    needed_capacity = grid.total_output()

    for b in all_batteries:
        q.put([b[0], b])

    while not q.empty():
        current = q.get()
        for b in all_batteries:
            new = current + [b]
            new[0] += b[0]
            if new[0] > needed_capacity:
                configurations.add(tuple(sorted(new[1:])))
            else:
                q.put(new)
    return configurations
