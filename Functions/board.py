from Classes.pawn import *

def displayBoard(board):

	print("")
	print("   A B C D E F G H")

	count = 1
	for i in range(8):

		print(" " + str(count), end=" ")

		for j in range(8):

			print(board[j][i], end=" ")

		print("")
		count += 1

	print("")

def populateBoard(pieces, board):

	for i in range(len(pieces)):

		board[pieces[i].pos_x][pieces[i].pos_y] = pieces[i].letter
		
	return board