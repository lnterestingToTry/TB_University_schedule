class Answer:
	def one_day(data):

		to_return = ''

		for item in data:
			for info in item:
				to_return += str(info) + '\n'
			to_return += '\n'



		return to_return