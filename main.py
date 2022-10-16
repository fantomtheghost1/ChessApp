import sys
from Functions.board import *
from Functions.pieces import *
from Functions.input import *

def resource_path(relative_path):
    
    try:
        
        base_path = sys._MEIPASS

    except Exception:

        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

main_board = [['-'] * 8 for i in range(8)]
pieces = []
pieces = piecesOnBoard(pieces)
main_board = populateBoard(pieces, main_board)

while True:

	while True:

		displayBoard(main_board)

		answer = input("Which piece would you like to move? (e.g. C4): ")
		piece = getInputLocation(answer, pieces) 

		if piece != None:

			break

	count = 0
	print('')
	print('Possible Moves:')
	for i in range(0, len(piece.possible_moves), 2):

		if checkValidMove(pieces, piece.possible_moves[i], piece.possible_moves[i + 1]):

			count += 1
			let = numberToLetter(piece.possible_moves[i])
			num = piece.possible_moves[i + 1] + 1
			move = let + str(num)
			print(str(count) + ". " + move)
			'''show the possible moves on the board itself'''

	print('')
	answer = input("Where would you like to move to? (e.g. C4) ")
	answer = inputToCoord(answer)

	if checkValidMove(pieces, answer[0], answer[1]):

		movePiece(piece, main_board, answer)
		populateBoard(pieces, main_board)
		piece.updateMove()

	else: 

		print("\nThat was an invalid move, please try again!")

if __name__ == '__main__':
    sys.exit()