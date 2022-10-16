class Bishop:

	letter = 'B'
	piece_type = 'bishop'
	old_pos_x = -1
	old_pos_x = -1
	first_move = True

	def __init__(self, pos_x, pos_y, team):

		self.pos_x = pos_x
		self.pos_y = pos_y
		self.team = team
		self.possible_moves = []

		for i in range(8):

			self.possible_moves.append(pos_x + i)
			self.possible_moves.append(pos_y + i)
			self.possible_moves.append(pos_x - i)
			self.possible_moves.append(pos_y + i)
			self.possible_moves.append(pos_x + i)
			self.possible_moves.append(pos_y - i)
			self.possible_moves.append(pos_x - i)
			self.possible_moves.append(pos_y - i)

	def updateMove(self):

		self.possible_moves.clear()

		for i in range(8):

			self.possible_moves.append(self.pos_x + i)
			self.possible_moves.append(self.pos_y + i)
			self.possible_moves.append(self.pos_x - i)
			self.possible_moves.append(self.pos_y + i)
			self.possible_moves.append(self.pos_x + i)
			self.possible_moves.append(self.pos_y - i)
			self.possible_moves.append(self.pos_x - i)
			self.possible_moves.append(self.pos_y - i)
		
