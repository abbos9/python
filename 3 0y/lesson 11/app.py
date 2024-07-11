from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from commnd import my_commands

from config import Second_bot
from def_keyboard import user_main_menu

from states import RegistState, CourseState

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
            await message.answer(text=text, reply_markup=user_main_menu)
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
    await message.answer(text='jinsizni keriting')
    await RegistState.jins.set()


@dp.message_handler(state=RegistState.jins)
async def get_gender_handler(message: types.Message, state: FSMContext):
    jins = message.text
    await state.update_data({
        'jins': jins
    })
    await message.answer(text='tugulgan sanezni keriting')
    await RegistState.birth_day.set()


@dp.message_handler(state=RegistState.birth_day)
async def get_birth_day_handler(message: types.Message, state: FSMContext):
    birth_day = message.text
    await state.update_data(
        {"birth_day": birth_day
         })
    await message.answer(text='manzilizni uy kiriting')
    await RegistState.address.set()


@dp.message_handler(state=RegistState.address)
async def get_address_handler(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(
        {"address": address
         })
    await message.answer(text='kimligizni kiriting kiriting')
    await RegistState.who_is_people.set()


@dp.message_handler(state=RegistState.who_is_people)
async def get_who_is_people_handler(message: types.Message, state: FSMContext):
    who_is_people = message.text
    await state.update_data(
        {"who_is_people": who_is_people
         })
    await message.answer(text='metirkezni yoki passportni kiriting')
    await RegistState.metrics.set()


@dp.message_handler(state=RegistState.metrics)
async def get_metrics_handler(message: types.Message, state: FSMContext):
    metrics = message.text
    await state.update_data(
        {"metrics": metrics
         })
    await message.answer(text='balandligizni kiriting')
    await RegistState.long.set()


@dp.message_handler(state=RegistState.long)
async def get_long_handler(message: types.Message, state: FSMContext):
    long = message.text
    await state.update_data(
        {"long": long
         })
    await message.answer(text='vesingizni kiriting')
    await RegistState.weight.set()


@dp.message_handler(state=RegistState.weight)
async def get_weight_handler(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(
        {"weight": weight
         })
    await message.answer(text='yoshingizni kiriting')
    await RegistState.age.set()


@dp.message_handler(state=RegistState.age)
async def get_age_handler(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data({
        'age': age
    })
    data = await state.get_data()
    with open('users.txt', 'a') as appender:
        users = f"{data['full_name']} | {data['phone_number']} | {data['jins']} | {data['birth_day']}" \
                f"| {data['metrics']} | {data['who_is_people']} |{data['address']} | {data['age']} " \
                f"| {data['weight']} | {data['long']} | {message.chat.id}\n"
        appender.write(users)
    await message.answer(text='siz royhattadan otdingiz')
    await state.finish()


@dp.message_handler(text='®️ Regist')
async def regist_handler(message: types.Message):
    await message.answer(text=' full name keriting')
    await CourseState.full_name.set()


@dp.message_handler(state=CourseState.full_name)
async def full_name_regist_handler(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data({
        'full_name': full_name
    })
    await message.answer(text='phone_numberni keriting')
    await CourseState.phone_number.set()


@dp.message_handler(state=CourseState.phone_number)
async def phone_num_regist_handler(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data({
        'phone_number': phone_number
    })
    await message.answer(text='age keriting')
    await CourseState.age.set()


@dp.message_handler(state=CourseState.age)
async def age_regist_handler(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data({
        'age': age
    })
    await message.answer(text='free time keriting')
    await CourseState.free_time.set()


@dp.message_handler(state=CourseState.free_time)
async def free_time_regist_handler(message: types.Message, state: FSMContext):
    free_time = message.text
    await state.update_data({
        'free_time': free_time
    })
    await message.answer(text='reason of study keriting')
    await CourseState.reason_study.set()


@dp.message_handler(state=CourseState.reason_study)
async def reason_study_regist_handler(message: types.Message, state: FSMContext):
    reason_study = message.text
    await state.update_data({
        'reason_study': reason_study
    })
    await message.answer(text='branch keriting')
    await CourseState.branch.set()


@dp.message_handler(state=CourseState.branch)
async def branch_regist_handler(message: types.Message, state: FSMContext):
    branch = message.text
    await state.update_data({
        'branch': branch
    })
    data = await state.get_data()
    with open('course.txt', 'a') as appender:
        users = f"{data['full_name']} | {data['phone_number']} | {data['age']} | {data['free_time']} | " \
                f" {data['reason_study']} | {data['branch']} | {message.chat.id} \n"
        appender.write(users)
    await message.answer(text='kursga royxatdan otdingiz')
    await state.finish()


@dp.message_handler(text='👤 profile')
async def profile_handler(message: types.Message, state: FSMContext):
    with open('users.txt', 'r') as reader:
        users = reader.readlines()
        for line in users:
            user = line.split('|')
            if user[-1].strip() == str(message.chat.id):
                text = f"""
Full name: {user[0]}
phone num: {user[1]}
age: {user[2]}
gender: {user[3]}
birth_day: {user[4]}
address: {user[5]}
who_is_people: {user[6]}
metrics: {user[7]}
long: {user[8]}
weight: {user[9]}
"""
                await message.answer(text=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
