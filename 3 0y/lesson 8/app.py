from aiogram import Bot, Dispatcher, executor, types

from commands import my_commands
from def_keyboard import main_commands
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states import SendMessage
from aiogram.types import ReplyKeyboardRemove

from config import API_TOKEN

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
users = list()


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message, ):
    text = f"aslomu aleykum{message.from_user.full_name}"
    await message.answer(text=text, reply_markup=main_commands)


@dp.message_handler(text="birinchi raqamni qiriting")
async def letter_handler1(message: types.Message):
    text = "raqamimngizni yozing"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await SendMessage.letter.set()


@dp.message_handler(state=SendMessage.letter)
async def get_message_handler1(message: types.Message, state: FSMContext):
    text = message.text
    await dp.bot.send_message(chat_id=1358470521, text=text)
    text1 = 'sizning habaringiz qabul qilindi'
    await message.answer(text=text1, reply_markup=main_commands)


@dp.message_handler(text="ikkinchi raqamni qiriting")
async def letter_handler2(message: types.Message):
    text = "raqamimngizni yozing"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await SendMessage.letter2.set()


@dp.message_handler(state=SendMessage.letter2)
async def get_message_handler2(message: types.Message, state: FSMContext):
    text = message.text
    await dp.bot.send_message(chat_id=1358470521, text=text)
    text1 = 'sizning habaringiz qabul qilindi'
    await message.answer(text=text1, reply_markup=main_commands)
    print(SendMessage.letter2)


@dp.message_handler(text="operatorni kiriting")
async def letter_handler3(message: types.Message):
    text = "arifmetik nimadirni yozing"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await SendMessage.counter.set()


@dp.message_handler(state=SendMessage.counter)
async def get_message_handler3(message: types.Message, state: FSMContext):
    text = message.text
    await dp.bot.send_message(chat_id=1358470521, text=text)
    text1 = 'sizning habaringiz qabul qilindi'
    await message.answer(text=text1, reply_markup=main_commands)

    await state.finish()


if __name__ == '__main__':
    print('https://t.me/enemy_in_shadowBot')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
