from aiogram import Bot, Dispatcher, executor, types
import random
from config import API_TOKEN
from commands import my_commands
from utils import randomizer

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands='start')
async def strat_handler(message: types.Message):
    user_name = message.from_user.full_name
    await message.answer(user_name)


@dp.message_handler()
async def random_intergere(message: types.Message):
    rand_num = random.randint(1, 100)
    text = int(message.text)
    live = 5
    son = ''
    if rand_num == text:
        son = 'togri'
    else:
        live -= 1
        son = f'no it was{rand_num}'

    if live == 0:
        son = 'tugadi'
    await message.answer(text=son)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
