from aiogram import types


async def my_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('random_int', 'random number'),
            types.BotCommand('start', 'start'),
            types.BotCommand('random', 'random int')
        ]

    )
