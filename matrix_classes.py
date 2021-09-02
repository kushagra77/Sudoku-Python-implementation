class Point():
	
    def __init__(self, value=0):
        # A point is fixed when it is solved
        if value == 0:   
			# Not solved so initialise with all possible numbers
            self.values = {1,2,3,4,5,6,7,8,9}
        else:
            self.values = {}
	 
	def IsFixed(self):
		return (len(self.values) == 1)
		

    # ToDo: CHANGE POP TO REMOVE
    def Remove(self, value):
        if not IsFixed():
            # Remove value for values set
            self.values.discard(value)   

class Map():

	def __init__(self):
		self.map = [[Point() for i in range(9)] for j in range(9)]
		self.solved = 0

	def UpdatePoint(self, point, row, column):
		self.map[row][column] = point
	
	def CheckSegment(self, row, column):
		for i in range(row, row + 2):
			for j in range(column, column + 2):


	def CheckRow(self, row):
		for i in range(row):


	def CheckCol(self, col):
		for j in range(col):


	def CheckPoint(self, value, row, column):
		return CheckCol(col) and CheckRow(row) and CheckSegment(3 * (row // 3), 3 * (col // 3))

