from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class Keyboard:

    def after_start():

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton('як викладач'),
            types.KeyboardButton('як студент')
        )

        keyboard.row(
            types.KeyboardButton('що це?')
        )
        return keyboard


    def academic_choose(data_list):
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=5)

        for item in data_list:
            name = ''
            callback = 'academic_id:' + str(item[3])
            #for names in item:
            name += item[0] + ' ' + item[1] + ' ' + item[2]

            button = types.InlineKeyboardButton(text=name, callback_data=callback)
            keyboard.add(button)

        return keyboard


    def faculty_choose(data_list):
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=5)

        for item in data_list:
            name = item[1]
            callback = 'faculty_id:' + str(item[0])
            #for names in item:
            #name += item[0] + ' ' + item[1] + ' ' + item[2]

            button = types.InlineKeyboardButton(text=name, callback_data=callback)
            keyboard.add(button)

        return keyboard


    def group_choose(data_list):
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=5)

        for item in data_list:
            name = item[1]
            callback = 'group_id:' + str(item[0])
            #for names in item:
            #name += item[0] + ' ' + item[1] + ' ' + item[2]

            button = types.InlineKeyboardButton(text=name, callback_data=callback)
            keyboard.add(button)

        return keyboard



    def academic_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton('розклад на сьогодні'),
            types.KeyboardButton('розклад на завтра')
        )

        keyboard.row(
            types.KeyboardButton('розклад попереднього тижня'),
            types.KeyboardButton('розклад на цей тиждень'),
            types.KeyboardButton('розклад на наступний тиждень')
        )

        keyboard.row(
            types.KeyboardButton('викладач'),
            types.KeyboardButton('змінити режим')
        )


        return keyboard


    def student_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton('розклад на сьогодні'),
            types.KeyboardButton('розклад на завтра')
        )

        keyboard.row(
            types.KeyboardButton('розклад попереднього тижня'),
            types.KeyboardButton('розклад на цей тиждень'),
            types.KeyboardButton('розклад на наступний тиждень')
        )

        keyboard.row(
            types.KeyboardButton('група'),
            types.KeyboardButton('змінити режим')
        )

        return keyboard