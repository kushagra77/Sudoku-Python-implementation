from sys import implementation
import copy
import matrix_classes as mc

def main():
	# Initialise map
	my_map = mc.Map()

	# Reading in the file to store the initial puzzle
	with open("puzzle.txt") as puzzle:
		linelist = puzzle.readlines()
        
	# Fills in original entries from given puzzle
	for row in range(9):
		for column in range(9):
			my_map.Add(mc.Point(int(linelist[row][column])), row, column)

	mainloop(my_map)

def mainloop(my_map, recursed=False):
	
	
	count = 0
	while my_map.solved < 81:
		if my_map.Lost():
			return False

		count += 1
		if count % 5 == 0: # the 5 can be changed to something higher, 4 doesn't work in some cases, yet to determine
							# ideal number
			if not recursed:
				guess(my_map)
			else:
				return True
		for row in range(9):
			for column in range(9):
				point = my_map.rows[row][column]
				
				if not point.fixed:
					for value in range(1, 10):
						if value not in point.values:
							continue
						if my_map.CrossCheck(value, row, column):
							my_map.solved += my_map.rows[row][column].Pop(value)	
						elif my_map.OutCheck(value, row, column):
							my_map.solved += 1
							my_map.RemoveInstance(value, row, column)
							break
	if recursed:
		return True
	my_map.Print()
	print("No. of iterations:", count)
	
	
def guess(old_map):
	fullbreak = False
	my_map = copy.deepcopy(old_map)
	old_point, first, second = None, None, None
	row, column = 0, 0
	for i in range(9):
		for j in range(9):
			point = my_map.rows[i][j]
			if len(point.values) == 2:
				for k in point.values:
					first = second
					second = k
				old_point = old_map.rows[i][j]
				point.Pop(first)
				old_point = old_map.rows[i][j]
				row, column = i, j
				fullbreak = True
				break
		if fullbreak:
			break
	if not mainloop(my_map, True):
		
		old_map.solved += old_point.Pop(second)
		
		old_map.RemoveInstance(first, row, column)
	else:
		old_map.solved += old_point.Pop(first)
		
		old_map.RemoveInstance(second, row, column)
	
							
if __name__ == "__main__":
    main()

