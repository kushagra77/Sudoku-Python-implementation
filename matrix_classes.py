# Stores solutions to a coordinate
class Point():
    def __init__(self, value=0):
        # A point is fixed when it is solved
        self.fixed = (value != 0)

        if not self.fixed:   
            # Not solved so initialise with all possible numbers
            self.values = {1,2,3,4,5,6,7,8,9}
        else:
            self.values = set()
        self.value = value

    # Removes value from values and returns 1 if point is now fixed
    def Pop(self, value):
        # Remove value for values set
        self.values.discard(value)
        if len(self.values) == 1 and not self.fixed:
            # There is only 1 value remaining
            # This point is solved
            self.value = self.values.pop()
            self.fixed = True
            return 1
        return 0

# Stores a 3x3 grid of Points
class Grid():

    def __init__(self):
        self.map = [[set() for i in range(3)] for j in range(3)]
          
        

    # Adds a point to self at coordinates (row, column)
    def Add(self, point, row, column):
        self.map[row][column] = point
        if point.fixed:
            # Point is solved
            
            return 1
        return 0
    
    # Removes the possibility of value from every point in the grid
    # returns how many more points are now fixed
    def Rectify(self, value):
        
        count = 0
        for i in range(3):
            for j in range(3):
                count += self.map[i][j].Pop(value)

        return count
        

    # Returns if a grid contains a value
    def Contains(self, value):
        for row in self.map:
            for point in row:
                if point.value == value:
                    return True
        return False

    # Returns True if the game is Lost due to repition in this grid
    def Lost(self):
        values = []
        for row in self.map:
            for point in row:
                if point.fixed:
                    values.append(point.value)
        if len(values) > len(set(values)):
            return True
        return False

    # If every other point in grid can't have value this returns True, otherwise False
    def OutCheck(self, value, row, column):
        
        for i in range(3):
            for j in range(3):
                if (i != row or j != column) and value in self.map[i][j].values:
                    return False        
        return True
        
        
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
            
            if value == i.value:
                return True
        for i in self.columns[column]:
            
            if value == i.value:
                return True

        return self.map[row // 3][column // 3].Contains(value)

            

    # Print out map fancily(for solution)
    def Print(self):
        print("|-----------------------|")
        for i in range(9):
            print("|", end = " ")
            for j in range(9):
                print(self.rows[i][j].value, end=" ")
                if j % 3 == 2:
                    print("|", end = " ")
            print("")
            if i % 3 == 2:
                print("|-----------------------|")

    # Removes the possibility of value from every point in row and column and grid
    # Increments self.solve for any new points now fixed
    def RemoveInstance(self, value, row, column):
        for point in self.rows[row]:
            self.solved += point.Pop(value)
                
        for point in self.columns[column]:
            self.solved += point.Pop(value)
                
        self.solved += self.map[row // 3][column // 3].Rectify(value)

    # Returns True if a value is not in possible values of any point in row
    def RowCheck(self, value, row):
        for i in range(9):
            if i != row and value in self.rows[row][i].values:
                return False
        return True

    # Returns True if a value is not in possible values of any point in column
    def ColumnCheck(self, value, column):
        for i in range(9):
            if i != column and value in self.columns[column][i].values:
                return False
        return True
        
    # Calls functions to check if a value can be fixed at row,column of map
    # Returns True if it can
    def OutCheck(self, value, row, column):
        point = self.map[row//3][column//3].map[row%3][column%3] 

        # Condition checking if value is possible anywhere in row and column and grid
        condition = self.RowCheck(value, row) or self.ColumnCheck(value, column)
        condition = condition or self.map[row//3][column//3].OutCheck(value, row%3, column%3)

        if condition:
            point.value = value
            point.values &= set()
            point.fixed = True
            return True
        return False

    # Check if game is Lost, for wrong guesses
    def Lost(self):
        for i in range(9):

            row = [j.value for j in self.rows[i] if j.fixed]            
            if len(row) > len(set(row)):
                return True # since row repetition

            column = [j.value for j in self.columns[i] if j.fixed]            
            if len(column) > len(set(column)):
                return True # since column repetition

            if self.map[i//3][i%3].Lost():
                return True #since grid repetition

        return False # not lost
                