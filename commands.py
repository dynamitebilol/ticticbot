from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🤖 Botni ishga tushurish"),
            types.BotCommand("help", "ℹ Yordam"),
            types.BotCommand("id", "🎮 O'yindagi ism"),
            types.BotCommand("game", "🎮 O'yinni boshlash")
        ]
    )