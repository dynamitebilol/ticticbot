from aiogram import types
from aiogram.utils import executor

from loader import db, dp

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🤖 Botni ishga tushurish"),
            types.BotCommand("help", "ℹ Yordam"),
            types.BotCommand("id", "🎮 O'yindagi ism"),
            types.BotCommand("game", "🎮 O'yinni boshlash")
        ]
    )



async def on_startup(dispatcher):
    await db.create()
    # await db.drop_users()
    await db.create_table_users()
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp)