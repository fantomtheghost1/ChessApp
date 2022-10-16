class Knight:

	letter = 'K'
	piece_type = 'knight'
	old_pos_x = -1
	old_pos_x = -1

	def __init__(self, pos_x, pos_y):

		self.pos_x = pos_x
		self.pos_y = pos_y
		self.possible_moves = [self.pos_x + 1, self.pos_y + 2, self.pos_x - 1, self.pos_y + 2, self.pos_x + 2, self.pos_y + 1, self.pos_x - 2, self.pos_y + 1, self.pos_x + 1, self.pos_y - 2, self.pos_x - 1, self.pos_y - 2, self.pos_x + 2, self.pos_y - 1, self.pos_x - 2, self.pos_y - 1]

	def updateMove(self):

		self.possible_moves = [self.pos_x + 1, self.pos_y + 2, self.pos_x - 1, self.pos_y + 2, self.pos_x + 2, self.pos_y + 1, self.pos_x - 2, self.pos_y + 1, self.pos_x + 1, self.pos_y - 2, self.pos_x - 1, self.pos_y - 2, self.pos_x + 2, self.pos_y - 1, self.pos_x - 2, self.pos_y - 1]
