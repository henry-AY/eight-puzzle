
# heapq functionality / understanding from: https://stackoverflow.com/questions/12749622/understanding-how-to-create-a-heap-in-python
import heapq
# from heapq import heappush, heappop, heappushpop, heapify, heapreplace
# deepcopy functionality from https://docs.python.org/3/library/copy.html
import copy

from puzzle import *

class Node:
    def __init__(self, puzzle, parent=None, cost=0, depth=0):
        self.puzzle = puzzle
        self.parent = parent
        self.cost = cost
        self.depth = depth
    
    # ran into '<', '>', '=' not supported between node instances, and found this helpful article on how to fix it
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
        # deepcopy functionality from https://docs.python.org/3/library/copy.html
        new_puzzle = copy.deepcopy(puzzle.state)

        # swap the possible moves with the blank / 0
        new_puzzle[x_zero_coord][y_zero_coord], new_puzzle[x_coord][y_coord] = new_puzzle[x_coord][y_coord], new_puzzle[x_zero_coord][y_zero_coord]
        children.append(Puzzle(new_puzzle)) # now that it's swapped, append it

    return children

def a_star(puzzle, heuristic, DEBUG=False, VERBOSE=False):
    queue = []
    expanded = 0 # num of nodes expanded, this lets us visually see how well each algorithm is performing beyond just time stamps.

    visited = set()
    initial_node = Node(puzzle, cost=0)

    heapq.heappush(queue, (heuristic(initial_node), initial_node))

    while queue:
        f_n , node = heapq.heappop(queue) # pop both the quee and the node, however, we can omit the queue

        expanded += 1

        if DEBUG:
            print(f"\nPopped min node with f(n) = {f_n} and g(n) = {node.cost}")
            node.puzzle.display()

        if node.puzzle.solved():
            if DEBUG:
                print("Solved, exiting")
            return node, node.depth, expanded # solved puzzle
        
        visited.add(node.puzzle) # append the state of the puzzle

        for child_puzzle in get_puzzle_children(node.puzzle): # look at every possible child node, and IFF not already visited, then we append the new node with the new cost
            if child_puzzle not in visited:
                new_node = Node(child_puzzle, parent=node, cost=node.cost + 1, depth=node.depth + 1)

                if VERBOSE: # Print for debugging flag + new line
                    print(f"\nChild Puzzle @ Depth {node.depth}")
                    child_puzzle.display()

                new_cost = new_node.cost + heuristic(new_node)
                heapq.heappush(queue, (new_cost, new_node))

    if DEBUG:
        print("Queue empty, exiting")
    return None # return "failure"