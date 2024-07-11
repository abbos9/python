from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('lavash',callback_data='lavash'),
            InlineKeyboardButton('fanta', callback_data='fanta'),
        ],    [
            InlineKeyboardButton('trindwich',callback_data='trindwich'),
            InlineKeyboardButton('burger', callback_data='burger'),
        ],    [
            InlineKeyboardButton('sneklar',callback_data='sneklar'),
            InlineKeyboardButton('cola', callback_data='cola'),
        ]
    ]
)