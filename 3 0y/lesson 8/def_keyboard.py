from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_commands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='birinchi raqamni qiriting'),
            KeyboardButton(text='ikkinchi raqamni qiriting')
        ],
        [
            KeyboardButton(text='operatorni kiriting')
        ]
    ], resize_keyboard=True
)
