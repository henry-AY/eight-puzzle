import argparse

from puzzle import *
from search import *
import time


# doesn't work for n * n, something to update in the future
def user_input():
    # grabbed parts of this code from the assignment description pdf
    print("Enter your puzzle, using a 0 to represent the blank. Deliminating each term with a space")

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

# the idea with this is to grab the coordinates of the value we're looking for.
# Then, we find the value of where the number should be originally, and we can use the distance formula
def manhatten_heuristic(node):
    total_distance = 0

    for i in range(0, 3):
        for j in range(0, 3):
            val = node.puzzle.state[i][j]
            if val != 0:
                x1, y1 = goal_puzzle_pos[val]
                total_distance += abs(i - x1) + abs(j - y1)
    return total_distance

# from my understanding, this only works for an 8-puzzle, so something that would need to be updated for a n-puzzle
def is_solvable(grid):
    flat_grid = reduce(operator.add, grid)

    inversion_count = 0

    for i in range(len(flat_grid)):
        for j in range(i + 1, len(flat_grid)):
            if flat_grid[i] != 0 and flat_grid[j] != 0 and flat_grid[i] > flat_grid[j]:
                inversion_count += 1
    if DEBUG:
        print(f"is_solvable: {inversion_count} and returning {inversion_count % 2}.")

    return (inversion_count % 2 == 0) # verify its even, otherwise the eight puzzle is not solvable

def run_a_star_helper(text, heuristic, puzzle):
    print(f"\nNow Running {text}")
    start = time.time()

    solution_node, solution_depth, nodes_expanded = a_star(puzzle, heuristic, DEBUG)

    end = time.time()
    length = end - start

    if not solution_node:
        print(f"No solution found for: {puzzle.display()}")
    else:
        print(f"Solution found at {solution_depth} depth with a duration of ~{length:.5f}, and {nodes_expanded} nodes expanded:")
        solution_node.puzzle.display()



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
    while True:
        grid = user_input()

        if not is_solvable(grid):
            print("\nUnfotunately this puzzle has an even number of inversions, and therefore is not solvable, please enter a new puzzle:")
        else:
            break

p_to_solve = Puzzle(grid)

# This list represents the expected coordinates of the numbers in a 3x3 matrix. 
# This exists, for a much faster lookup time, which helps improve the speed of the manhattan alg.
goal_puzzle_pos = { 1: (0,0), 2: (0,1), 3: (0,2),
                    4: (1,0), 5: (1,1), 6: (1,2),
                    7: (2,0), 8: (2,1)
                }

print(f"You created the following {p_to_solve.get_size()} * {p_to_solve.get_size()} puzzle:\n")
p_to_solve.display() # simple print to verify

# running UCS
run_a_star_helper("UCS (A* with h(n) = 0)", zero_hueristic, p_to_solve)

# running A* w/ missing tile heuristic
run_a_star_helper("A* with Missing Tile Heuristic", missing_tile_heuristic, p_to_solve)

# running A* w/ Manhattan heuristic
run_a_star_helper("A* with Manhattan Distance Heuristic", manhatten_heuristic, p_to_solve)