def letterToNumber(letter):

	if letter.lower() == 'a':

		letter = 0

	elif letter.lower() == 'b':

		letter = 1

	elif letter.lower() == 'c':

		letter = 2

	elif letter.lower() == 'd':

		letter = 3

	elif letter.lower() == 'e':

		letter = 4

	elif letter.lower() == 'f':

		letter = 5

	elif letter.lower() == 'g':

		letter = 6

	elif letter.lower() == 'h':

		letter = 7

	else:

		letter = -1

	return letter

def numberToLetter(number):

	if number == 0:

		letter = 'A'

	elif number == 1:

		letter = 'B'

	elif number == 2:

		letter = 'C'

	elif number == 3:

		letter = 'D'

	elif number == 4:

		letter = 'E'

	elif number == 5:

		letter = 'F'

	elif number == 6:

		letter = 'G'

	elif number == 7:

		letter = 'H'

	else:

		letter = -1

	return letter

def inputToCoord(coordinates):

	letter = int(letterToNumber([*coordinates][0]))
	number = int([*coordinates][1]) - 1
	output = []
	output.append(letter)
	output.append(number)

	return output

def getInputLocation(location, pieces):

	coords = inputToCoord(location)

	if coords[1] >= 8 or coords[1] <= -1 or coords[0] >= 8 or coords[0] <= -1:

		return None

	else:

		for i in range(len(pieces)):

			if pieces[i].pos_x == coords[0] and pieces[i].pos_y == coords[1]:

				return pieces[i]