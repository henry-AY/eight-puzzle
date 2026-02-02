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
        print(self.state)
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # hard-coded for rn, should be AOK.

        return (self.state == goal_state)
    
    def get_size(self):
        return len(self.state)
    
    def find_zero(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if self.state[i][j] == 0:
                    return i, j
        raise Exception("Sorry, puzzle most contain a 0") # hard fail, because there's not a point in running if the puzzle doesn't contain a 0
    
    def find_neighbors(self):
    # Possible neighbors are (+1, 0), (0, +1), (-1, 0) & (0, -1)
        neighbors = []
        x, y = self.find_zero()

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