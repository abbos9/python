from aiogram import Bot, Dispatcher, executor, types

import wikipedia

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_harndler(message: types.Message):
    name = message.from_user.full_name  # upper() .replace(' ','')
    text = f'asalomu aleykum {name}'
    await message.answer(text=text)


@dp.message_handler()
async def wikepedia_handler_ru(message: types.Message):
    try:
        text = message.text
        lang = text.split(" ")[0].replace("/", "")
        fruit = text.split(' ')[1]
        wikipedia.set_lang(lang)
        data = wikipedia.summary(fruit)
        await message.answer(text=data)
    except Exception as exs:
        print(exs)
        text = 'bunaqa malumot topilmadi'
        await message.answer(text=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
