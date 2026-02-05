class Puzzle:

    def __init__(self, arr):
        """
        Init method to init the puzzle
        """
        self.state = arr
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # hard-coded for rn, should be AOK.

    # ran into some issues with lists not being hashable, previous str solution was inefficient, so I switched to 
    # making a comparison + hash functions that hopefully are faster
    # https://stackoverflow.com/questions/6754102/typeerror-unhashable-type
    def __eq__(self, other_puzzle): 
        return self.state == other_puzzle.state
    
    def __hash__(self):
        return hash(tuple(tuple(x) for x in self.state))

    def display(self):
        for row in self.state:
            print(" ".join(str(x) for x in row))

    def solved(self):
        return (self.state == self.goal_state)
    
    def get_size(self):
        return len(self.state)
    
    def find_value(self, value):
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if self.state[i][j] == value:
                    return i, j
        raise Exception("Sorry, does not contain {value}") # hard fail, because there's not a point in running if the puzzle doesn't contain a 0
    
    # TODO Does the missing tile heuristic count the 0 as a missing tile?
    def misplaced_tile_sum(self):
        counter = 0

        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if self.state[i][j] != self.goal_state[i][j]:
                    counter += 1

        return counter
    
    def find_neighbors(self):
    # Possible neighbors are (+1, 0), (0, +1), (-1, 0) & (0, -1)
        EMPTY_SPACE = 0

        neighbors = []
        x, y = self.find_value(EMPTY_SPACE) # search for the empty space (in this case 0)

        # up
        if y > 0:
            neighbors.append((x, y - 1))

        # down
        if y < len(self.state[0]) - 1:
            neighbors.append((x, y + 1))

        # left    
        if x > 0:
            neighbors.append((x - 1, y))

        # right
        if x < len(self.state) - 1:
            neighbors.append((x + 1, y))
        
        return x, y, neighbors