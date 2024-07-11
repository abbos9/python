from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lavash_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='mini 21,000', callback_data='mini_lavash'),
            InlineKeyboardButton(text='big 26,000', callback_data='big_lavash')
        ],
    ]
)
lavashmol_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='mini 26,000', callback_data='mini_lavash'),
            InlineKeyboardButton(text='big 31,000', callback_data='big_lavash')
        ],
    ]
)
trindwich_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='minus'),
            InlineKeyboardButton(text='1', callback_data='count'),
            InlineKeyboardButton(text='+', callback_data='plus')
        ],
        [
            InlineKeyboardButton(text='savatga qoshish',callback_data='savat')
        ]
    ]
)
second_trindwich_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='-'),
            InlineKeyboardButton(text='1', callback_data='++'),
            InlineKeyboardButton(text='+', callback_data='+')
        ],
        [
            InlineKeyboardButton(text='savatga qoshish',callback_data='savat')
        ]
    ]
)