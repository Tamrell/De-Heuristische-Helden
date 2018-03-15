import sys
import time

start_time = time.time()

if len(sys.argv) != 2:
    print("usage: python3 solver.py puzzle#.sudoku")
    exit(1)

s = []
sudictu = {(x, y): None for x in range(9) for y in range(9)}
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# =============================================================================
#                                 MAIN
# =============================================================================


def main():

    fill()
    print_sudoku()
    for i in {1, 2, 3, 4, 5}:
        reduce_ss()
    while not solved():
        DFS()
    return 0

# =============================================================================
#                                 FILL
# =============================================================================

def fill():
    """Fills sudictu with given information from file"""
    with open(sys.argv[1]) as input_sudoku:
        x = 0
        y = 0
        for line in input_sudoku:
            for character in line:
                try:
                    sudictu[(x, y)] = int(character)
                    if (x == 8):
                        x = 0
                        y += 1
                    else:
                        x += 1
                except ValueError:
                    pass
# =============================================================================
#                                 Solved
# =============================================================================


def solved():
    """Checks if the sudictu is filled with integers"""
    if all(isinstance(value, int) for value in sudictu.values()):
        print_sudoku()
        print("Solved!\nThe elapsed time is: ", time.time() - start_time)
        return 1
    return 0

# =============================================================================
#                          Reduce Search Space
# =============================================================================


def reduce_ss():
    """Minimizes the search space by eliminating possibilities"""
    for key in sudictu:

        # only act if 0 or set
        if isinstance(sudictu[key], int):
            if sudictu[key] > 0:
                continue
            else:
                missing_nums(*key)

        elif sudictu[key]:
            missing_check(key, 0)
    return 1



def missing_nums(x, y):
    """Finds all the possible numbers for coordinate"""

    # take the remainder of all possible numbers minus the ones already present
    missing = numbers_set - (row(y) | column(x) | quadrant(x, y))

    # if the remainder is a non-empty list, check if singularity
    if missing:

        # if singularity, fill it in for this coordinate
        if len(missing) == 1:
            sudictu[(x, y)] = missing.pop()
            return 2

        # if not singular, make coordinate its set of possibilities
        sudictu[(x, y)] = missing
    else:
        abort_mission()
    return 1

def missing_check(key, size):
    """Checks if sudicto key has less than size options"""

    # check if singular possibility
    if missing_nums(*key) == 2:
        return 1

    # check if amount of possibilities is smaller than or equal to size
    if len(sudictu[key]) <= size:
        branch(*key, sudictu[key])
        return 1

    return 0
# =============================================================================
#                        Depth-First-Search
# =============================================================================


def DFS():
    """Looks for coordinates with max_branches amount of possibilities."""
    for max_branches in [2]:
        for key in sudictu:

            # update search space
            reduce_ss()

            # if integer, do nothing
            if isinstance(sudictu[key], int):
                continue

            # if non-empty set, commence with missing_check
            elif sudictu[key]:
                missing_check(key, max_branches)

            # if empty list of posibilities, discard current branch
            else:
                abort_mission()
    return 1


def branch(x, y, missing):
    """Branches off for each possibility in missing and continue with
    one of them"""
    copydictu = sudictu.copy()
    for i in range(len(missing) - 1):
        copydictu[(x, y)] = missing.pop()
        s.append(copydictu)
    sudictu[(x, y)] = missing.pop()
    return 1


def abort_mission():
    """Discards current sudoku and continue with the last valid one"""
    sudictu.update(s.pop())
    return 1
# =============================================================================
#               Row, Quadrant, Column
# =============================================================================


def row_list(y):
    """Returns a list of the y+1th row"""
    return [sudictu[(x, y)] for x in range(9)]


def row(y):
    """Returns a set with all know numbers in the y+1th row"""
    return {sudictu[(x, y)] for x in range(9) if
            isinstance(sudictu[(x, y)], int)}


def column(x):
    """Returns a set with all know numbers in row x + 1"""
    return {sudictu[(x, y)] for y in range(9) if
            isinstance(sudictu[(x, y)], int)}


def quadrant(x, y):
    """Returns a set with all known numbers in it"""
    row = (x // 3) * 3
    col = (y // 3) * 3
    quad = set()
    for c_num in {col, col + 1, col + 2}:
        for r_num in {row, row + 1, row + 2}:
            if isinstance(sudictu[(r_num, c_num)], int):
                quad.add(sudictu[(r_num, c_num)])
    return quad
# =============================================================================
#                          Print Sudoku
# =============================================================================


def print_sudoku():
    """prints the sudoku in a human friendly representation"""
    for y in range(9):
        if y in [0, 3, 6]:
            print("          -------------------------")
        print_row(row_list(y))
    print("          -------------------------")


def print_row(row):
    print('          |', end=" ")
    for number in range(9):
        if not isinstance(row[number], int):
            print(".", end=" ")
        elif row[number] == 0:
            print(".", end=" ")
        else:
            print(row[number], end=" ")
        if number in [2, 5]:
            print('|', end=" ")
    print('|')


if __name__ == "__main__":
    main()
