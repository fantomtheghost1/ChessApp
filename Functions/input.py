def movePiece(piece):
	
	if piece.piece_type == 'pawn' && piece.team == 1:

		piece.pos_y += 1

	elif piece.piece_type == 'pawn' && piece.team == 2:

		piece.pos_y -= 1