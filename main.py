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

# Main loop to sift through all the basic strategies (sufficient for easy puzzles), takes in an optional
# argument specifying whether it is going through a guess check (for harder puzzles)
def mainloop(my_map, recursed=False):
	
	# Keeps track of how many times the main loop has been recursed through
	count = 0
	# To check if to guess
	change = True
	# Main loop, ends only when every position is solved, returns a boolean
	while my_map.solved < 81:
		
		# Only returns 0 if current map violates a rule
		# The map won't ever violate a rule unless it is going through a guess check (recursed map)
		if recursed and my_map.Lost():
			return 0

		# Increment for every iteration of main loop
		count += 1
		

		# After every 4 iterations of the main loop, if unsolved, this initiates a guesscheck
		# The 4 can be changed to something higher or lower to improve efficiency
		# the ideal number (trial and error and line 48) has not been figured out yet
		if not change:
			if recursed:
				if guess(my_map):
					break
		change = False

		# Loop to check basic conditions starting from top left of map to bottom right
		for row in range(9):
			for column in range(9):

				# declaring the point for this iteration
				point = my_map.rows[row][column]

				# Only changes point if its value is undecided
				if not point.fixed:

					# Loop with every possible value
					for value in range(1, 10):

						# Check if the point allows this value
						if value not in point.values:
							continue

						# If the value is in the same row, column or grid as the point,
						# it is discarded from allowed values of the point
						if my_map.CrossCheck(value, row, column):
							my_map.solved += my_map.rows[row][column].Pop(value) #Pop() returns 1 if the point is now fixed
							change = True
						# If the value can not be anywhere else in the same row, column or grid (any one),
						# it is fixed
						elif my_map.OutCheck(value, row, column):
							my_map.solved += 1
							my_map.RemoveInstance(value, row, column)
							change = True
							break

	# If when puzzle is solved, it is in a guess check, returns -1 to withhold from further analysis
	if recursed:
		return -1

	my_map.Print()
	print("No. of non-guess iterations:", count)
	


def guess(old_map):
	fullbreak = False #to break out from nested loop
	my_map = copy.deepcopy(old_map) # Clone for guessing
	
	# Used to reference data of guessing point, declaring outside of small scope
	old_point, first, second, row, column = None, None, None, None, None

	# Loop to find one point which has only 2 possible values
	# By now there should be at least one point of such kind for puzzles with a unique solution
	for i in range(9):
		for j in range(9):
			point = my_map.rows[i][j]
			if len(point.values) == 2:
				# To refer to possible values
				for k in point.values:
					first = second
					second = k
				point.Pop(first) # Guess takes place
				old_point = old_map.rows[i][j]
				row, column = i, j 
				fullbreak = True
				break
		# Completely breaking out of the nest
		if fullbreak:
			break
	# Running mainloop with our new guess and cloned map, setting recursed True
	mainreturn = mainloop(my_map, True)

	# Choose to either copy over solution (if reached), accept guess or reject guess
	if mainreturn == -1:
		old_map.solved = 81
		# Changing every entry in original map to cloned solution
		for i in range(9):
			for j in range(9):
				point = old_map.rows[i][j]
				point.fixed = True
				point.values = set()
				point.value = my_map.rows[i][j]
		return True

	elif mainreturn == 0:
		old_map.solved += old_point.Pop(second) # Reject guess
		old_map.RemoveInstance(first, row, column)
	else:#Never gonna happen now but still there
		old_map.solved += old_point.Pop(first) # Accept guess
		old_map.RemoveInstance(second, row, column)



if __name__ == "__main__":
    main()

