from aiogram import Bot, Dispatcher, executor, types
from utils import get_data_nbu, get_one_cur, get_kop_cur

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    name = message.from_user.full_name
    data = f'aslomu aleykum {name}'
    await message.answer(text=data)


@dp.message_handler(commands='cerrancy')
async def get_cerrancy_of_NBU(message: types.Message):
    data = get_data_nbu()
    await message.answer(data)


#
# @dp.message_handler()
# async def get_one_currency(message: types.Message):
#     code = message.text
#     data = get_one_cur(code)
#     await message.answer(text=data)


@dp.message_handler()
async def get_one_currency(message: types.Message):
    text = message.text.split(' ')[0]
    price = message.text.split(" ")[1]
    res = get_kop_cur(text, float(price))
    await message.answer(text=res)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
