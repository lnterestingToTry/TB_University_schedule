class Poliglot:
	all_phrases = {
		'as_academic': '👨‍🏫 як викладач',
		'as_student': '🎓 як студент',
		'help': 'ℹ️ що це?',

		'group': '🎓 група',
		'academic': '👨‍🏫 викладач',
		'mode_change': '🔁 змінити режим',

		'group_change': 'змінити групу',
		'academic_change': 'змінити викладача',

		'student_today': '📖 сьогодні 🎓',
		'student_tomorrow': '📕 завтра 🎓',
		'student_week': '📚 цей тиждень 🎓',
		'student_next_week': '📔 наступний тиждень 🎓',
		'student_previous_week': '📒 попередній тиждень 🎓',

		'academic_today': '📖 сьогодні 👨‍🏫',
		'academic_tomorrow': '📕 завтра 👨‍🏫',
		'academic_week': '📚 цей тиждень 👨‍🏫',
		'academic_next_week': '📔 наступний тиждень 👨‍🏫',
		'academic_previous_week': '📒 попередній тиждень 👨‍🏫'
	}

	def get(phrase_str):
		return Poliglot.all_phrases[phrase_str]