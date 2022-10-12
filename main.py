import sys
from Classes.pawn import *
from Functions.board import displayBoard, populateBoard
from Functions.pieces import piecesOnBoard

main_board = [['-'] * 8 for i in range(8)]
pieces = []
pieces = piecesOnBoard(pieces)
main_board = populateBoard(pieces, main_board)
displayBoard(main_board)

answer = input("Which piece would you like to move? (e.g. C4): ")

if __name__ == '__main__':
    sys.exit()