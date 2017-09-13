from utils import *
import pdb

def find_starting_node(puzzle):
    node = ('', '')
    for box, value in puzzle.items():
        if not node[1]:
            node = (box, value)
            continue
        if len(value) < len(node[1]):
            node = (box, value)
    return node


def search(values):
    print("What are me values", values)
    dict_vals = grid_values(values)
    reduced_puz = reduce_puzzle(dict_vals)

    # Choose one of the unfilled squares with the fewest possibilities
    start_node = find_starting_node(reduced_puz)

    # Now use recursion to solve each one of the resulting sudokus


if __name__ == "__main__":
    grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    answer = search(grid2)

