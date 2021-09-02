class Point():
    def __init__(self, value=0):
        self.fixed = (value != 0)
        if not self.fixed:   
            self.values = {1,2,3,4,5,6,7,8,9}
        else:
            self.values = {value}
        self.value = value

    def Pop(self, value):
        if not self.fixed:
            self.values.discard(value)
            if len(self.values) == 1:
                self.value = self.values.pop()
                self.fixed = True

class Grid():
    def __init__(self):
        self.map = [[{} for i in range(3)] for j in range(3)]
        self.values = []

    def Add(self, point, row, column):
        self.map[row][column] = point
        if point.fixed:
            self.values.append(point.value)

    def Contains(self, value):
        return value in self.values
            
class Map():
    def __init__(self):
        self.map = [[Grid() for i in range(3)] for j in range(3)]
        self.rows = [[] for i in range(9)]
        self.columns = [[] for i in range(9)]
    
    def Add(self, point, row, column):
        self.rows[row].append(point)
        self.columns[column].append(point)
        self.map[row // 3][column // 3].Add(point, row % 3, column % 3)
    
    def RowColumn(self, value, row, column):
        for i in self.rows[row]:
            if value == i.value():
                return False
        for i in self.columns[column]:
            if value == i.value():
                return False
        return True