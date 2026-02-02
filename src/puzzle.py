class Puzzle:

    def __init__(self, arr):
        """
        Init method to init the puzzle
        """
        self.state = arr

    def display(self):
        for row in self.state:
            print(" ".join(str(x) for x in row))


    def solved(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # hard-coded for rn, should be AOK.

        return (self.state == goal_state)
    
    def find_neighbors(self, x, y):
    # Possible neighbors are (+1, 0), (0, +1), (-1, 0) & (0, -1)
        neighbors = []

        # up
        if y > 0:
            neighbors.append(self.state[x][y - 1])

        if y < len(self.state[0]) - 1:
            neighbors.append(self.state[x][y + 1])

        # left    
        if x > 0:
            neighbors.append(self.state[x - 1][y])

        # right
        if x < len(self.state) - 1:
            neighbors.append(self.state[x + 1][y])
        
        return neighbors