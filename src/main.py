import argparse

from puzzle import *
from search import *
import operator
from functools import reduce

# doesn't work for n * n, something to update in the future
def user_input():
    # grabbed parts of this code from the assignment description pdf
    print("Enter your puzzle, using a 0 to represent the blank. ONLY enter valid 8-puzzle problems. Deliminating each term with a space")

    puzzle_r1 = input("Enter the first row: ").split()
    puzzle_r2 = input("Enter the second row: ").split()
    puzzle_r3 = input("Enter the third row: ").split()

    for i in range(0, 3):
        puzzle_r1[i] = int(puzzle_r1[i])
        puzzle_r2[i] = int(puzzle_r2[i])
        puzzle_r3[i] = int(puzzle_r3[i])

    return [puzzle_r1, puzzle_r2, puzzle_r3]

def zero_hueristic(node = None):
    return 0

# from my understanding (and professors explanation), this heuristic has a min of 1 (assuming before reaching goal state) 
# and a max of 8, where we calculate the number of tiles that do not match the goal state.
def missing_tile_heuristic(node):
    return node.puzzle.misplaced_tile_sum()


def manhatten_heuristic(node):
    # the strat with this is to grab the coordinates of the value we're looking for (using the find_value() func)
    # Then, we find the value of where the number should be originally, and we can use the distance formula

    flat_grid = reduce(operator.add, grid)

    total_distance = 0
    
    for i in flat_grid:
        x1, y1 = node.puzzle.find_value(i)
        x2, y2 = Puzzle(grid).find_value(i)

        total_distance += abs((x1 - x2) + (y1 - y2))

    return total_distance


# This code assumes that the default win condition is:

    # 1 2 3
    # 4 5 6
    # 7 8

# (in other words the blank is always bottom right)

parser = argparse.ArgumentParser(description="A script that does something with flags.")
parser.add_argument("-s", "--simple", action="store_true", help="Use default (seeded) puzzle")
parser.add_argument("-d", "--debug", action="store_true", help="Debug mode to print")

args = parser.parse_args()

DEBUG = args.debug

# Step 1: grab user input (otherwise use default seeded puzzle)
if args.simple:
    grid = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
else:
    grid = user_input()

p_to_solve = Puzzle(grid)

print(f"You created the following {p_to_solve.get_size()} * {p_to_solve.get_size()} puzzle:\n")
p_to_solve.display() # simple print to verify

print(f"\nNow Running UCS (A* with h(n) = 0)")

# TODO Calculate time metrics

solution_node, solution_depth = a_star(p_to_solve, zero_hueristic, DEBUG)
print(f"Solution found at {solution_depth} depth:")
solution_node.puzzle.display()


print(f"\nNow Running A* with Missing Tile Heuristic")
solution_node_missing_tile, solution_depth_missing_tile = a_star(p_to_solve, missing_tile_heuristic, DEBUG)
print(f"Solution found at {solution_depth_missing_tile} depth:")
solution_node_missing_tile.puzzle.display()

# TODO Manhatten distance