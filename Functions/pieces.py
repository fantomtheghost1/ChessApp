from Classes.pawn import *
from Classes.knight import *
from Functions.board import populateBoard

def movePiece(piece, board, move):
	
	piece.old_pos_x = piece.pos_x
	piece.old_pos_y = piece.pos_y
	piece.pos_y = move[1]
	piece.pos_x = move[0]
	board[piece.old_pos_x][piece.old_pos_y] = '-'

	'''elif piece.piece_type == 'knight':'''




def piecesOnBoard(piece_list):

	knight1 = Knight(7, 2)

	piece_list.append(knight1)
	'''pawn1 = Pawn(0, 1, 1)
	pawn2 = Pawn(1, 1, 1)
	pawn3 = Pawn(2, 1, 1)
	pawn4 = Pawn(3, 1, 1)
	pawn5 = Pawn(4, 1, 1)
	pawn6 = Pawn(5, 1, 1)
	pawn7 = Pawn(6, 1, 1)
	pawn8 = Pawn(7, 1, 1)

	piece_list.append(pawn1)
	piece_list.append(pawn2)
	piece_list.append(pawn3)
	piece_list.append(pawn4)
	piece_list.append(pawn5)
	piece_list.append(pawn6)
	piece_list.append(pawn7)
	piece_list.append(pawn8)'''

	return piece_list
