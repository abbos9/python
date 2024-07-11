from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN
from keyboard import main_menu, products_menu, lavash_menu, trindvich_menu, shaurma_menu, burger_menu, Sub_menu
from keyboard import Kartoshka_menu, Hot_Dog_menu, Sneklar_menu, Salat_garnir_non_menu, souslar_menu, \
    desert_menu
from aiogram.types import InputFile
from utils import savat

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message, ):
    text = f"aslomu aleykum{message.from_user.full_name}"
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text='🍴 Menyu')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='🫔 Lavash')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-08-30_10-09-18.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=lavash_menu)


@dp.message_handler(text='🌮 Trindwich')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-08-30_10-10-23.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=trindvich_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='📥 Savat')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='⬅️ mahsulotlar')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text='🍲 Shaurma')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_19-18-08.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=shaurma_menu)


@dp.message_handler(text='🍔 Burger')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-16-12.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=burger_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Sub')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-24-32.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=Sub_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Kartoshka')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-28-30.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=Kartoshka_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Hot-Dog')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-31-46.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=Hot_Dog_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Sneklar')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-35-16.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=Sneklar_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Salat, garnir, non')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-03_23-41-06.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=Salat_garnir_non_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='souslar')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-04_09-54-57.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=souslar_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Setlar')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/setlar.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=souslar_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text='Desertlar')
async def menu_handler(message: types.Message):
    phto = InputFile(path_or_bytesio='./photo/photo_2023-09-06_09-03-31.jpg')
    text = 'holagan mahsulotni tanglang'
    await message.answer_photo(photo=phto, caption=text, reply_markup=desert_menu)


@dp.message_handler(text='⬅️ Ortga')
async def menu_handler(message: types.Message):
    text = 'holagan mahsulotni tanglang'
    await message.answer(text=text, reply_markup=products_menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
