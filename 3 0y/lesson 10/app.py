from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from command import my_commands

from config import Second_bot
# from def_keyboard import
# from inline_keyboard import
from states import RegistState

storage = MemoryStorage()
bot = Bot(token=Second_bot)
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    with open('users.txt', 'r') as reader:
        users = reader.read()
        if str(message.chat.id) in users:
            text = 'botga hush kelibsiz'

        else:
            text = f"Assalomu alaykum \n" \
                f"iltimos ismingizni kiriting"
        await message.answer(text=text)
        await RegistState.full_name.set()


@dp.message_handler(state=RegistState.full_name)
async def get_fullname_handler(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data({
        'full_name': full_name
    })
    text = 'raqamingizni kiriting'
    await message.answer(text=text)
    await RegistState.phone_number.set()


@dp.message_handler(state=RegistState.phone_number)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data({
        'phone_number': phone_number
    })
    await message.answer(text='yoshingizni keriting')
    await RegistState.free_days.set()


@dp.message_handler(state=RegistState.free_days)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    free_days = message.text
    await state.update_data({
        'free_days': free_days
    })
    await message.answer(text='boshkunlarizni keriting')
    await RegistState.what_you_want.set()


@dp.message_handler(state=RegistState.what_you_want)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    free_days = message.text
    await state.update_data({
        'free_days': free_days
    })
    await message.answer(text='boshkunlarizni keriting')
    await RegistState.what_you_want.set()


@dp.message_handler(state=RegistState.study)
async def get_what_you_want_handler(message: types.Message, state: FSMContext):
    study = message.text
    await state.update_data({
        'study': study
    })
    await message.answer(text=' bizda oldin oqiganmisiz?')
    await RegistState.age.set()


@dp.message_handler(state=RegistState.age)
async def get_age_handler(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data({
        'age': age
    })
    data = await state.get_data()
    with open('users.txt', 'a') as appender:
        user = f"{data['full_name']} | {data['phone_number']} | {data['age']} | {data['what_you_want']} | {data['free_days']} | {data['study']} | {message.chat.id}\n"
        appender.write(user)

    await message.answer(text='siz royhattadan otdingiz')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
