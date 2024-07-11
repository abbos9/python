from aiogram import Bot, Dispatcher, types, executor

from config import API_TOKEN
from utils import get_all_name, get_all_house, random_inf

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
from commands import my_commands


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    name = f"aslomu aleykum {message.from_user.full_name} "
    # animation = message.s
    await message.answer(text=name)


@dp.message_handler(commands='names')
async def get_names_handler(message: types.Message):
    all_names = get_all_name()
    await message.answer(text=all_names)


@dp.message_handler(commands='house')
async def get_house_handler(message: types.Message):
    houses = get_all_house()
    await message.answer(text=houses)


@dp.message_handler(commands='random')
async def random_name_handler(message: types.Message):
    rand = random_inf()
    await message.answer(text=rand)


@dp.message_handler(commands='randomizer')
async def random_intergere(message: types.Message):
    interger = 'random int'
    await  message.answer(interger)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
