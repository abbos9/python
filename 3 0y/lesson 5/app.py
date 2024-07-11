from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN
from commands import my_commands
from keyboars import main_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    await my_commands(dispatcher)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message, ):
    text = f"aslomu aleykum{message.from_user.full_name}"
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text='Pullingizni jami')
async def click_hanlder(message: types.Message):
    photo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQogXOk_UCRQLgFPkVzVBbEdpFiG_q3pjIs9r5Ul0Ux&s'
    await message.answer_photo(photo=photo)
    text = 'knopka bosildi'
    await message.answer(text=text)


@dp.message_handler(commands ='🌯 evos')
async def evos_handler(message: types.Message):
    photo = "https://static.tildacdn.com/tild6333-3963-4534-b062-636331353739/14.png"
    await message.answer_photo(photo=photo)
    text = "Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz? 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi."
    await message.answer(text=text)


@dp.message_handler(text="🍗 KEFSI")
async def kefsi_handler(message: types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/224414/2a00000186cf94c7fb8ac3d46bf7e59f2616/L_height"
    await message.answer_photo(photo=photo)
    text = "FC (Kentucky Fried Chicken) — shtab-kvartirasi Kentukki shtatining Luisvil shahrida joylashgan, qovurilgan tovuqqa ixtisoslashgan amerikalik tez ovqatlanish restoranlari tarmogʻidir. Bu McDonaldsdan keyin dunyodagi ikkinchi yirik restoranlar tarmogʻi (sotish boʻyicha) boʻlib, 2019-yil dekabr holatiga koʻra 150 ta mamlakatda 22 621 ta joyi mavjud[1]. KFC Yum! Brands nomli Pizza Hut, Taco Bell va WingStreet tarmoqlariga egalik qiluvchi restoran kompaniyasining shoʻba korxonasi hisoblanadi[2]."
    await message.answer(text=text)


@dp.message_handler(text="🍕 moscov pizza")
async def moscow_pizza(message: types.Message):
    photo = 'https://media-cdn.tripadvisor.com/media/photo-o/05/60/aa/94/getlstd-property-photo.jpg'
    await message.answer_photo(photo=photo)
    text = """Наша семья очень давно занимается ресторанной кулинарией. 

Мы известны великолепной аутентичной кухней, профессиональным шеф-поваром и преданным персоналом. Выберите любое блюдо из меню, которое поможет вам ощутить настоящий вкус пиццы"""
    await message.answer(text=text)


@dp.message_handler(text="🌭 archa kocha hottog")
async def moscow_pizza(message: types.Message):
    photo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1c24tZnoTNcftx1ppuSqL8nVrtiU_PBbjrHn50uRY&s'
    await message.answer_photo(photo=photo)
    text = "bizning hot-doglarimiz naturalni mahsullotlardan qilinadi bizda shashlikli va sosiskali hot-doglar bor hot-doglarni esa salat bilan toldiramiz"
    await message.answer(text=text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
