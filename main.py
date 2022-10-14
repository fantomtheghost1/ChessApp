import sys
from Classes.pawn import *
from Functions.board import *
from Functions.pieces import *
from Functions.input import *

main_board = [['-'] * 8 for i in range(8)]
pieces = []
pieces = piecesOnBoard(pieces)
main_board = populateBoard(pieces, main_board)

while True:

	displayBoard(main_board)

	answer = input("Which piece would you like to move? (e.g. C4): ")
	piece = getInputLocation(answer, pieces) 

	if piece != None:

		break

available_moves = []

answer = input("Where would you like to move to? (e.g. C4) ")
answer = inputToCoord(answer)

for i in range(0, len(piece.possible_moves), 2):

	'''breakpoint()'''
	if piece.possible_moves[i] < 8 and piece.possible_moves[i] >= 0 and piece.possible_moves[i + 1] < 8 and piece.possible_moves[i + 1] >= 0 and piece.possible_moves[i] == answer[0] and piece.possible_moves[i + 1] == answer[1]:

		movePiece(piece, main_board, answer)
		print("move good")

	else:

		print("move bad")

populateBoard(pieces, main_board)
displayBoard(main_board)

if __name__ == '__main__':
    sys.exit()