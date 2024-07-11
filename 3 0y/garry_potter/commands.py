from aiogram import types


async def my_commands(dp):
    await dp.bot.set_my_commands(

        [
            types.BotCommand('start', ' 💫 boshlash commandasi'),
            types.BotCommand('names', ' 💫 20 amta ism'),
            types.BotCommand('house','🏘 20 mata uylar'),
            types.BotCommand('random', 'random inf'),


        ]

    )
