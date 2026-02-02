
# heapq functionality / understanding from: https://stackoverflow.com/questions/12749622/understanding-how-to-create-a-heap-in-python
import heapq
# from heapq import heappush, heappop, heappushpop, heapify, heapreplace
# deepcopy functionality from https://docs.python.org/3/library/copy.html
import copy

from puzzle import *

class Node:
    def __init__(self, puzzle, parent=None, cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.cost = cost
    
    # ran into '<' not supported between node instances, and found this helpful article on how to fix it
    # https://stackoverflow.com/questions/66198575/typeerror-not-supported-between-instances-of-node-and-node

    def __eq__(self, value):
        return (self.puzzle.state == value.puzzle.state)
    
    def __lt__(self, value):
        return (self.puzzle.state < value.puzzle.state)
    
    def __gt__(self, value):
        return (self.puzzle.state > value.puzzle.state)
    

def get_puzzle_children(puzzle):
    x_zero_coord, y_zero_coord, neigbors =  puzzle.find_neighbors()
    children = []

    for x_coord, y_coord in neigbors:
        new_puzzle = copy.deepcopy(puzzle.state)

        # swap the values
        new_puzzle[x_zero_coord][y_zero_coord], new_puzzle[x_coord][y_coord] = new_puzzle[x_coord][y_coord], new_puzzle[x_zero_coord][y_zero_coord]
        children.append(Puzzle(new_puzzle)) # now that it's swapped, append it

    return children

def a_star(puzzle, heuristic):
    queue = []

    visited = set()
    start_node = Node(puzzle, cost=0)

    heapq.heappush(queue, (heuristic(start_node), start_node))

    while True:
        if not queue:
            print("Queue empty, exiting")
            return None # equivalent to return "failure"
        
        _ , node = heapq.heappop(queue)

        if node.puzzle.solved():
            print("Solved, exiting")
            return node # solved puzzle
        
        visited.add(str(node.puzzle.state)) # append the state of the puzzle

        for child_puzzle in get_puzzle_children(node.puzzle):
            if str(child_puzzle.state) not in visited:
                new_node = Node(child_puzzle, parent=node, cost=node.cost + 1)

                print("\n")
                child_puzzle.display()

                new_cost = new_node.cost + heuristic(new_node)
                heapq.heappush(queue, (new_cost, new_node))