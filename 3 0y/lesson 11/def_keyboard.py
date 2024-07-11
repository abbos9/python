from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='®️ Regist'),
            KeyboardButton(text='👤 profile')

        ]
    ], resize_keyboard=True

)
