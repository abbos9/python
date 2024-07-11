from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery, InputFile
from config import API_TOKEN
from inline_keyboards import main_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    name = f'aslomu aleykum {message.from_user.full_name}'
    await message.answer(text=name, reply_markup=main_menu)


@dp.callback_query_handler(text='lavash')
async def lavash_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-44-17.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


@dp.callback_query_handler(text='fanta')
async def fanta_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-49-51.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


@dp.callback_query_handler(text='trindwich')
async def trindwich_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-49-22.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


@dp.callback_query_handler(text='burger')
async def burger_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-49-02.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


@dp.callback_query_handler(text='sneklar')
async def snek_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-48-37.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


@dp.callback_query_handler(text='cola')
async def cola_callback(call: CallbackQuery):
    text = 'hohlagan mahsulotni tanglang'
    photo = InputFile(path_or_bytesio="./phto/photo_2023-09-04_09-49-51.jpg")
    await call.message.answer_photo(photo=photo, caption=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
