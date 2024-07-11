from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from commnad import my_commands
from config import API_TOKEN
from def_keyboard import main_menu, calculator_menu
from states import CalculatorState
from inline_keyboard import main

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    text = f"Assalomu alaykum{message.from_user.full_name}"
    await message.answer(text=text,reply_markup=main_menu)


@dp.message_handler(text="🧮 Hisoblash")
async def calculate_handler(message: types.Message):
    text = "Iltimos, birinchi raqamni kiriting"
    await message.answer(text=text, reply_markup=calculator_menu)
    await CalculatorState.num1.set()


# @dp.message_handler(text="🧮 Hisoblash")
# async def calculate_handler(message: types.Message):
#     text = "Iltimos, birinchi raqamni kiriting"
#     await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
#     await CalculatorState.num1.set()


@dp.message_handler(state=CalculatorState.num1)
async def get_num1_handler(message: types.Message, state: FSMContext):
    num1 = message.text
    await state.update_data({
        "num1": num1
    })
    text = "Iltimos, ikkinchi raqamni kiriting."
    await message.answer(text=text)
    await CalculatorState.num2.set()


@dp.message_handler(state=CalculatorState.num2)
async def get_num2_handler(message: types.Message, state: FSMContext):
    num2 = message.text
    await state.update_data({
        "num2": num2
    })
    text = "Iltimos, amalni kiriting. | + | - | * | / |"
    await message.answer(text=text)
    await CalculatorState.sign.set()


@dp.message_handler(state=CalculatorState.sign)
async def calculate_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    sign = message.text
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    if sign == "+":
        result = num1 + num2
        text = f"Natija: {num1} {sign} {num2} = {result}"
    elif sign == "-":
        result = num1 - num2
        text = f"Natija: {num1} {sign} {num2} = {result}"
    elif sign == "*":
        result = num1 * num2
        text = f"Natija: {num1} {sign} {num2} = {result}"
    elif sign == "/":
        result = num1 / num2
        text = f"Natija: {num1} {sign} {num2} = {result}"
    else:
        text = "Bunday operatsiyani amalga oshirish mumkin emas."

    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
