from aiogram import types


async def set_my_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🚀 Botni ishga tushurish")
        ]
    )