from config import *

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from keyboard import Keyboard
from database import Database

import re

bot = Bot(TOKEN)
dp = Dispatcher(bot)


db = Database()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

	if(not db.user_exists(message.from_user.id)):
		insert_data = db.add_user(message.from_user.id)

	await message.answer(text='im alive', reply_markup=Keyboard.after_start())


@dp.message_handler(lambda message: message.text == 'як викладач' or message.text == 'як студент')
async def mode_selection(message: types.Message):

	keyboard = None

	if message.text == 'як викладач':
		data = db.academics_select()
		keyboard = Keyboard.academic_choose(data)
		print(data)
		print('academic')

	elif message.text == 'як студент':
		data = db.faculty_select()
		keyboard = Keyboard.faculty_choose(data)
		print(data)
		print('student')

	await message.delete()

	await message.answer(text='mode selected', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'що це?')
async def about(message: types.Message):

	keyboard = Keyboard.after_start()

	await message.delete()

	await message.answer(text='about section', reply_markup=keyboard)



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('faculty_id:'))
async def faculty_select(callback_query: types.CallbackQuery):
	message = callback_query.message

	faculty_id = re.match(r'^faculty_id:(\d+)$', callback_query.data).group(1)

	data = db.group_select(faculty_id)
	keyboard = Keyboard.group_choose(data)

	await message.delete()

	await message.answer(text=faculty_id, reply_markup=keyboard)



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('group_id:'))
async def group_update(callback_query: types.CallbackQuery):
	message = callback_query.message

	group_id = re.match(r'^group_id:(\d+)$', callback_query.data).group(1)

	#select_group_by_user

	data_update = db.group_update(callback_query.from_user.id, group_id)

	keyboard = Keyboard.student_keyboard()

	print('group_update' + ' message.from_user.id ' + str(callback_query.from_user.id) + ' group_id ' + str(group_id))

	await message.delete()

	await message.answer(text=group_id, reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('academic_id:'))
async def academic_update(callback_query: types.CallbackQuery):
	message = callback_query.message

	academic_id = re.match(r'^academic_id:(\d+)$', callback_query.data).group(1)

	#select_group_by_user

	data_update = db.academic_update(callback_query.from_user.id, academic_id)

	keyboard = Keyboard.academic_keyboard()

	print('academic_update' + ' message.from_user.id ' + str(callback_query.from_user.id) + ' academic_id ' + str(academic_id))

	await message.delete()

	await message.answer(text=academic_id, reply_markup=keyboard)




@dp.message_handler(lambda message: message.text == 'група')
async def group_change(message: types.Message):

	data = db.faculty_select()
	keyboard = Keyboard.faculty_choose(data)

	await message.delete()

	await message.answer(text='group_change', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'викладач')
async def academic_change(message: types.Message):

	data = db.academics_select()
	keyboard = Keyboard.academic_choose(data)

	await message.delete()

	await message.answer(text='academic_change', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'змінити режим')
async def mode_change(message: types.Message):

	keyboard = Keyboard.after_start()

	await message.delete()

	await message.answer(text='mode_change', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'розклад на сьогодні')
async def today(message: types.Message):

	keyboard = Keyboard.student_keyboard()


	answer = ''

	user_info = db.select_group_by_user(message.from_user.id)

	group_id = user_info[0][0]
	print(group_id)

	today_schadule_info = db.today_select_group(group_id)


	print(today_schadule_info)

	await message.delete()

	await message.answer(text='сьогодні', reply_markup=keyboard)






@dp.callback_query_handler()
async def db_string_check(callback_query: types.CallbackQuery):
	message = callback_query.message


	print('db_string_check')

	await message.answer(text=message.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)