import datetime
from datetime import datetime

weekday_names = {
    'Monday': 'Понеділок',
    'Tuesday': 'Вівторок',
    'Wednesday': 'Середа',
    'Thursday': 'Четвер',
    'Friday': 'Пʼятниця',
    'Saturday': 'Субота',
    'Sunday': 'Неділя'
}

class Answer:
	def one_day(data):

		to_return = ''

		for item in data:

			date = item[-1]
			weekday = date.strftime('%A')
			weekday_name = weekday_names.get(weekday)

			to_return += weekday_name + '\n'

			to_return += item[0] + ' ' + item[1] + '\n'

			to_return += item[2] + '\n'

			to_return += item[3] + '\n'

			to_return += item[4] + '\n'

			start_time = datetime.strptime(str(item[5]), "%H:%M:%S")
			start_time = start_time.strftime("%H:%M")

			end_time = datetime.strptime(str(item[6]), "%H:%M:%S")
			end_time = end_time.strftime("%H:%M")


			to_return += str(start_time) + ' ' + str(end_time) + '\n'




			# for info in item:
			# 	to_return += str(info) + '\n'


			to_return += '\n'

		return to_return

	def week(data):

		# grouped_data = {}
		# for entry in data:
		#     date = entry[-1] #дата
		#     if date in grouped_data:
		#         grouped_data[date].append(str(entry))
		#     else:
		#         grouped_data[date] = [str(entry)]


		# to_return = ''

		# for date, entries in grouped_data.items():
		# 	weekday = date.strftime('%A')
		# 	to_return += weekday_names.get(weekday)
		# 	for info in entries:
		# 		to_return += str(info) + '\n'
		# 	to_return += '\n'




		already = []

		to_return = ''

		for item in data:
			date = item[-1]
			weekday = date.strftime('%A')
			weekday_name = weekday_names.get(weekday)


			if item[2] in already:
				pass
			else:
				already.append(item[2])
				to_return += item[2] + '     ' + str(item[-1]) + '\n'


			if weekday_name in already:
				pass
			else:
				already.append(weekday_name)
				to_return += '\n' + weekday_name + ' ' + '\n'




			to_return += item[0] + ' ' + item[1] + ' - ' + item[4] + '\n'

			#to_return += item[2] + '\n'

			to_return += item[3] + ' - '


			start_time = datetime.strptime(str(item[5]), "%H:%M:%S")
			start_time = start_time.strftime("%H:%M")

			end_time = datetime.strptime(str(item[6]), "%H:%M:%S")
			end_time = end_time.strftime("%H:%M")

			to_return += str(start_time) + ' - ' + str(end_time) + '\n'


			# for info in item:
			# 	to_return += str(info) + '\n'

			to_return += '\n'

		return to_return