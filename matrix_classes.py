# Stores solutions to a coordinate
class Point():
    def __init__(self, value=0):
        # A point is fixed when it is solved
        self.fixed = (value != 0)

        if not self.fixed:   
            # Not solved so initialise with all possible numbers
            self.values = {1,2,3,4,5,6,7,8,9}
        else:
            self.values = {}
        self.value = value

    # ToDo: CHANGE POP TO REMOVE
    def Pop(self, value):
        if not self.fixed:
            # Remove value for values set
            self.values.discard(value)
            if len(self.values) == 1:
                # There is only 1 value remaining
                # This point is solved
                self.value = self.values.pop()
                self.fixed = True

# Stores a 3x3 grid of Points
class Grid():

    def __init__(self):
        self.map = [[{} for i in range(3)] for j in range(3)]
        # Stores all numbers in the grid
        self.values = []    # Maybe change to set

    # Adds a point to self at coordinates (row, column)
    def Add(self, point, row, column):
        self.map[row][column] = point
        if point.fixed:
            # Point is solved
            self.values.append(point.value)
            self.solved += 1
            return 1
        return 0

    # Returns if a grid contains a value
    def Contains(self, value):
        return value in self.values

# Stores a 3x3 grid of Grid
class Map():

    def __init__(self):
        self.map = [[Grid() for i in range(3)] for j in range(3)]
        self.rows = [[] for i in range(9)]
        self.columns = [[] for i in range(9)]
        self.solved = 0
    
    # Add a point to self at (row, column)
    def Add(self, point, row, column):
        self.rows[row].append(point)
        self.columns[column].append(point)
        self.solved += self.map[row // 3][column // 3].Add(point, row % 3, column % 3)
    
    # Check if a Map contains value in row, column and grid
    def CrossCheck(self, value, row, column):
        for i in self.rows[row]:
            if value == i.value():
                return True
        for i in self.columns[column]:
            if value == i.value():
                return True
        return self.map[row // 3][column // 3].Contains(value)