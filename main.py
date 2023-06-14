from config import *

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from keyboard import Keyboard
from database import Database

from answers_list import Answer
from poliglot import Poliglot

import re


bot = Bot(TOKEN)
dp = Dispatcher(bot)


db = Database()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

	if(not db.user_exists(message.from_user.id)):
		insert_data = db.add_user(message.from_user.id)

	await message.answer(text='start description', reply_markup=Keyboard.after_start())


@dp.message_handler(lambda message: message.text == Poliglot.get('as_academic') or message.text == Poliglot.get('as_student'))
async def mode_selection(message: types.Message):

	keyboard = None
	text = None

	if message.text == Poliglot.get('as_academic'):
		data = db.academics_select()
		keyboard = Keyboard.academic_choose(data)
		text = 'Викладач:'
		print(data)
		print('academic')

	elif message.text == Poliglot.get('as_student'):
		data = db.faculty_select()
		keyboard = Keyboard.faculty_choose(data)
		text = 'Факультет:'
		print(data)
		print('student')

	await message.delete()

	await message.answer(text=text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == Poliglot.get('help'))
async def about(message: types.Message):

	keyboard = Keyboard.after_start()

	await message.delete()

	await message.answer(text='about section', reply_markup=keyboard)



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('faculty_id:'))
async def faculty_select(callback_query: types.CallbackQuery):
	message = callback_query.message

	faculty_id = re.match(r'^faculty_id:(\d+)$', callback_query.data).group(1)

	faculty_name = db.faculty_name(faculty_id)[0][0]

	data = db.group_select(faculty_id)
	keyboard = Keyboard.group_choose(data)

	await message.delete()

	await message.answer(text=faculty_name, reply_markup=keyboard)



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('group_id:'))
async def group_update(callback_query: types.CallbackQuery):
	message = callback_query.message

	group_id = re.match(r'^group_id:(\d+)$', callback_query.data).group(1)

	group_name = db.group_name(group_id)[0][0]

	print('group_update' + ' message.from_user.id ' + str(callback_query.from_user.id) + ' group_id ' + str(group_id))

	data_update = db.group_update(callback_query.from_user.id, group_id)

	keyboard = Keyboard.student_keyboard()

	print('group_update' + ' message.from_user.id ' + str(callback_query.from_user.id) + ' group_id ' + str(group_id))

	await message.delete()

	await message.answer(text=group_name, reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('academic_id:'))
async def academic_update(callback_query: types.CallbackQuery):
	message = callback_query.message

	academic_id = re.match(r'^academic_id:(\d+)$', callback_query.data).group(1)

	name = db.academic_name(academic_id)
	academic_name = name[0][0] + ' ' + name[0][1] + ' ' + name[0][2]

	data_update = db.academic_update(callback_query.from_user.id, academic_id)

	keyboard = Keyboard.academic_keyboard()

	print('academic_update' + ' message.from_user.id ' + str(callback_query.from_user.id) + ' academic_id ' + str(academic_id))

	await message.delete()

	await message.answer(text='Викладач: ' + academic_name, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == Poliglot.get('group'))
async def group_info(message: types.Message):

	group_id = db.select_group_by_user(message.from_user.id)

	group_name = db.group_name(group_id[0][0])[0][0]

	#data = db.faculty_select()
	keyboard = Keyboard.group_choose_trigger()

	await message.delete()

	await message.answer(text='Група: ' + str(group_name), reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == Poliglot.get('group_change'))
async def group_change(callback_query: types.CallbackQuery):
	message = callback_query.message

	data = db.faculty_select()
	keyboard = Keyboard.faculty_choose(data)

	await message.delete()

	await message.answer(text='group_change', reply_markup=keyboard)
	

@dp.message_handler(lambda message: message.text == Poliglot.get('academic'))
async def academic_info(message: types.Message):

	academic_id = db.select_academic_by_user(message.from_user.id)

	name = db.academic_name(academic_id[0][0])
	academic_name = name[0][0] + ' ' + name[0][1] + ' ' + name[0][2]

	#data = db.academics_select()
	keyboard = Keyboard.academic_choose_trigger()

	await message.delete()

	await message.answer(text=academic_name, reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == Poliglot.get('academic_change'))
async def academic_change(callback_query: types.CallbackQuery):
	message = callback_query.message

	data = db.academics_select()
	keyboard = Keyboard.academic_choose(data)

	await message.delete()

	await message.answer(text='academic_change', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == Poliglot.get('mode_change'))
async def mode_change(message: types.Message):

	keyboard = Keyboard.after_start()

	await message.delete()

	await message.answer(text='Переглянути розклад: ', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == Poliglot.get('student_today') or message.text == Poliglot.get('student_tomorrow'))
async def one_day(message: types.Message):

	keyboard = Keyboard.student_keyboard()

	answer = ''

	user_info = db.select_group_by_user(message.from_user.id)

	group_id = user_info[0][0]
	print(group_id)


	schadule_info = None
	if message.text == Poliglot.get('student_today'):
		schadule_info = db.today_select_group(group_id)

	elif message.text == Poliglot.get('student_tomorrow'):
		schadule_info = db.tomorrow_select_group(group_id)

	if schadule_info != None:
		if len(schadule_info) != 0:
			answer += Answer.week(schadule_info)
		else:
			answer += 'день вільний'
	else:
		answer += 'None'


	print(schadule_info)

	await message.delete()

	await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == Poliglot.get('student_week') or message.text == Poliglot.get('student_next_week') or message.text == Poliglot.get('student_previous_week'))
async def week(message: types.Message):

	keyboard = Keyboard.student_keyboard()


	answer = ''

	user_info = db.select_group_by_user(message.from_user.id)

	group_id = user_info[0][0]
	print(group_id)


	schadule_info = None
	if message.text == Poliglot.get('student_week'):
		schadule_info = db.this_week_select_group(group_id)

	elif message.text == Poliglot.get('student_next_week'):
		schadule_info = db.next_week_select_group(group_id)

	elif message.text == Poliglot.get('student_previous_week'):
		schadule_info = db.previous_week_select_group(group_id)

	if schadule_info != None:
		if len(schadule_info) != 0:
			answer += Answer.week(schadule_info)
		else:
			answer += 'тиждень вільний'
	else:
		answer += 'None'


	print(schadule_info)

	await message.delete()

	await message.answer(text=answer, reply_markup=keyboard)







@dp.message_handler(lambda message: message.text == Poliglot.get('academic_today') or message.text == Poliglot.get('academic_tomorrow'))
async def one_day_academics(message: types.Message):

	keyboard = Keyboard.academic_keyboard()


	answer = ''

	user_info = db.select_academic_by_user(message.from_user.id)

	academic_id = user_info[0][0]
	print(academic_id)


	schadule_info = None
	if message.text == Poliglot.get('academic_today'):
		schadule_info = db.today_select_academic(academic_id)

	elif message.text == Poliglot.get('academic_tomorrow'):
		schadule_info = db.tomorrow_select_academic(academic_id)

	if schadule_info != None:
		if len(schadule_info) != 0:
			answer += Answer.week(schadule_info)
		else:
			answer += 'день вільний'
	else:
		answer += 'None'


	print(schadule_info)

	await message.delete()

	await message.answer(text=answer, reply_markup=keyboard)







@dp.message_handler(lambda message: message.text == Poliglot.get('academic_week') or message.text == Poliglot.get('academic_next_week') or message.text == Poliglot.get('academic_previous_week'))
async def week(message: types.Message):

	keyboard = Keyboard.academic_keyboard()


	answer = ''

	user_info = db.select_academic_by_user(message.from_user.id)

	academic_id = user_info[0][0]
	print(academic_id)


	schadule_info = None
	if message.text == Poliglot.get('academic_week'):
		schadule_info = db.this_week_select_academic(academic_id)

	elif message.text == Poliglot.get('academic_next_week'):
		schadule_info = db.next_week_select_academic(academic_id)

	elif message.text == Poliglot.get('academic_previous_week'):
		schadule_info = db.previous_week_select_academic(academic_id)

	if schadule_info != None:
		if len(schadule_info) != 0:
			answer += Answer.week(schadule_info)
		else:
			answer += 'тиждень вільний'
	else:
		answer += 'None'


	print(schadule_info)

	await message.delete()

	await message.answer(text=answer, reply_markup=keyboard)



















@dp.callback_query_handler()
async def db_string_check(callback_query: types.CallbackQuery):
	message = callback_query.message


	print('db_string_check')

	await message.answer(text=message.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)