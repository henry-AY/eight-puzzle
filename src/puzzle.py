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