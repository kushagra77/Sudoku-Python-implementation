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
		for row in range(9):
			for column in range(9):
				point = my_map.rows[row][column]
				if not point.fixed:
					for value in range(1, 10):
						if my_map.CrossCheck(value, row, column):
							my_map.solved += my_map.rows[row][column].Pop(value)
	my_map.Print()
	

							
if __name__ == "__main__":
    main()

