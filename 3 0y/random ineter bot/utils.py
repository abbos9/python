from aiogram import types


def randomizer(message: types.Message):
    import random
    live = 5
    text = ''
    rand_num = random.randint(1, 100)
    if rand_num == message.text:
        text = 'good'
    else:
        live -= 1
    if live == 0:
        text = 'tugadi'
    return text


