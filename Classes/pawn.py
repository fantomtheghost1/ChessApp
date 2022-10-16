class Pawn:

	letter = 'P'
	piece_type = 'pawn'
	old_pos_x = -1
	old_pos_x = -1

	def __init__(self, pos_x, pos_y, team):

		self.pos_x = pos_x
		self.pos_y = pos_y
		self.team = team

		if team == 1:

			self.possible_moves = [pos_x, pos_y + 1]

		else:

			self.possible_moves = [pos_x, pos_y - 1]

	def updateMove(self):

		if self.team == 1:

			self.possible_moves = [self.pos_x, self.pos_y + 1]

		else:

			self.possible_moves = [self.pos_x, self.pos_y - 1]
