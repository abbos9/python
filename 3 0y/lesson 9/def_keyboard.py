from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧮 Hisoblash', )
        ],
        [
            KeyboardButton(text='alamalar')
        ],

    ], resize_keyboard=True
)
calculator_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ],
        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
        ],
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
            KeyboardButton(text='0'),

        ],
    ], resize_keyboard=True
)
