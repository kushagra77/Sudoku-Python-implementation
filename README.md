# Sudoku-Python-implementation
Implementation and strategies for solving a 9x9 sudoku puzzle (with a unique solution)
# Strategies

Row check function
Column check function
Grid check function
^^^ These required two separate types of checks,
One to eliminate the possibility of a number in a position {CAN'T BE MORE THAN ONE INSTANCE}
Another exploiting the mandatory existence of every number in every row, column grid to push forced spots(most natural human strategy) {CAN'T BE LESS THAN ONE POSSIBILITY}


Recursion sweeps : Ended up using (double?) recursion with two functions mainloop and guess recursing through each other

guess checking was required to imitate humans thinking one step ahead, it was only enabled for a 50% probability but not limited to any number of steps


Special interpretations for greater difficulties: Wasn't required when an educated guess function was implemented and thorough checks were performed.

