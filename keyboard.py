from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from poliglot import Poliglot

class Keyboard:

    def after_start():

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton(Poliglot.get('as_academic')),
            types.KeyboardButton(Poliglot.get('as_student'))
        )

        keyboard.row(
            types.KeyboardButton(Poliglot.get('help'))
        )
        return keyboard


    def academic_choose(data_list):
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=5)

        buttons = []

        for item in data_list:
            name = ''
            callback = 'academic_id:' + str(item[3])
            #for names in item:
            name += item[0] + ' ' + item[1] + ' ' + item[2]

            button = types.InlineKeyboardButton(text=name, callback_data=callback)
            buttons.append(button)


        rows = [buttons[i:i+3] for i in range(0, len(buttons), 3)]  # Разделите список кнопок на ряды по три кнопки

        for row in rows:
            keyboard.add(*row)

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


    def group_choose_trigger():
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        callback = Poliglot.get('group_change')
        button = types.InlineKeyboardButton(text='змінити групу', callback_data=callback)
        keyboard.add(button)

        return keyboard


    def academic_choose_trigger():
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        callback = Poliglot.get('academic_change')
        button = types.InlineKeyboardButton(text='змінити викладача', callback_data=callback)
        keyboard.add(button)

        return keyboard


    def academic_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton(Poliglot.get('academic_today')),
            types.KeyboardButton(Poliglot.get('academic_tomorrow'))
        )

        keyboard.row(
            types.KeyboardButton(Poliglot.get('academic_week')),
            types.KeyboardButton(Poliglot.get('academic_next_week')),
            types.KeyboardButton(Poliglot.get('academic_previous_week'))
        )

        keyboard.row(
            types.KeyboardButton(Poliglot.get('academic')),
            types.KeyboardButton(Poliglot.get('mode_change'))
        )

        return keyboard


    def student_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard.row(
            types.KeyboardButton(Poliglot.get('student_today')),
            types.KeyboardButton(Poliglot.get('student_tomorrow'))
        )

        keyboard.row(
            types.KeyboardButton(Poliglot.get('student_week')),
            types.KeyboardButton(Poliglot.get('student_next_week')),
            types.KeyboardButton(Poliglot.get('student_previous_week'))
        )

        keyboard.row(
            types.KeyboardButton(Poliglot.get('group')),
            types.KeyboardButton(Poliglot.get('mode_change'))
        )

        return keyboard