
from aiogram.utils import executor
from commands import set_default_commands
from loader import db, dp




async def on_startup(dispatcher):
    await db.create()
    # await db.drop_users()
    await db.create_table_users()
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp)