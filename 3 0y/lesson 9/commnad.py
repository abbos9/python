from aiogram import types


async def my_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", 'korishish komandasi')
        ],
    )