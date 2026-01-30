import argparse
from puzzle import Puzzle

# This code assumes that the default win condition is:

    # 1 2 3
    # 4 5 6
    # 7 8

# (in other words the blank is always bottom right)

# doesn't work for n * n, something to update in the future
def user_input():
    print("Enter your puzzle, using a 0 to represent the blank. ONLY enter valid 8-puzzle problems. Deliminating each term with a space")

    puzzle_r1 = input("Enter the first row: ").split()
    puzzle_r2 = input("Enter the second row: ").split()
    puzzle_r3 = input("Enter the third row: ").split()

    for i in range(0, 3):
        puzzle_r1[i] = int(puzzle_r1[i])
        puzzle_r2[i] = int(puzzle_r2[i])
        puzzle_r3[i] = int(puzzle_r3[i])

    return [puzzle_r1, puzzle_r2, puzzle_r3]


def main():
    parser = argparse.ArgumentParser(description="A script that does something with flags.")
    parser.add_argument("--default", action="store_true", help="Use default (seeded) puzzle")

    args = parser.parse_args()


    # Step 1: grab user input (otherwise use default seeded puzzle)
    if args.default:
        grid = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
    else:
        grid = user_input()

    p_to_solve = Puzzle(grid)
    p_to_solve.display() # verify

    


    # Step 2: run search
    #   2.1 find all of the possible neighbors
    #   2.2 write current state + other found states to dictionary (to prevent repeated states)
    #   2.3 check if any of the states are the goal state (if so return said state)
    #   2.4 otherwise, repeat from step 2.1 until queue is empty and/or goal state is found




# define print wrapper



if __name__ == "__main__":
    main()