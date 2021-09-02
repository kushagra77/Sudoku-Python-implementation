from sys import implementation
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
	
	while my_map.solved < 81:
		for row in my_map.rows:
			for point in row:
				print(point.value, " ", end="")
			print("")
		print("")
		print("")
		print("--------------------")
		print("")
		print("")
		for row in range(9):
			for column in range(9):
				point = my_map.rows[row][column]
				if not point.fixed:
					for value in range(9):
						if my_map.CrossCheck(value, row, column):
							point.Pop(value)

	

							
if __name__ == "__main__":
    main()

