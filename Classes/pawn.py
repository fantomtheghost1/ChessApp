class Pawn:

	letter = 'P'
	piece_type = 'pawn'
	old_pos_x = -1
	old_pos_x = -1
	first_move = True

	def __init__(self, pos_x, pos_y, team):

		self.pos_x = pos_x
		self.pos_y = pos_y
		self.team = team

