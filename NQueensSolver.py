#Puzzle solver for the N Queens Problem
#Outputs all solutions

#initialize board of size NxN
def initBoard():
	board = [[0 for y in range(size)] for x in range(size)]
	return board

#print out board
def output(board):
	for i in range(size):
		print(board[i])
	print()

#check if queen can be placed on board
def checkBoard(board, row, col):
	for i in range(size):
		if board[row][i] == 1:
			return False

	i = 0
	while row-i >= 0 and col-i >= 0:
		if board[row-i][col-i] == 1:
			return False
		i += 1

	i = 0
	while row+i < size and col-i >= 0:
		if board[row+i][col-i] == 1:
			return False
		i += 1

	return True

#solve with backtracking, print out solution if found
def solve(board, col):
	if col >= size:
		return

	for i in range(size):
		if checkBoard(board, i, col):
			board[i][col] = 1
			if col == size-1:
				output(board)
				board[i][col] = 0
				return

			solve(board, col+1)
			board[i][col] = 0


#main driver
size = int(input('Enter size of board (4 or higher): '))

board = initBoard()

solve(board, 0)

